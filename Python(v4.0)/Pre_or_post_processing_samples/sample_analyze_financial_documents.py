# coding: utf-8
# ---------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# ---------------------------------------------------------------------------
# Additional contributions Copyright (c) 2026 Ambreen Zaver, Callisto Tech.
# ---------------------------------------------------------------------------

"""
FILE:           sample_analyze_financial_documents.py
DESCRIPTION:
    This sample demonstrates how to extract, normalize, and reconcile
    structured key-value fields from financial documents using the
    Azure Document Intelligence prebuilt-document model.

    It covers five common IRS form types used in financial aid and tax
    reconciliation workflows:

        - IRS Form 1040 (individual income tax return)
        - W-2 (wage and tax statement)
        - Schedule C (self-employment / business income)
        - Schedule E (rental and royalty income)
        - Schedule K-1 Form 1065 (partnership income)

    After extraction, raw Azure DI string values are normalized to Python
    Decimal via a post-processing step that handles:

        - Currency symbols and comma separators   "$75,000"  → 75000
        - Parenthetical negatives                 "(12,500)" → -12500
        - Non-negative fields (e.g. W-2 boxes)   "(68,500)" →  68500
        - Percentage values                       "12.5%"    →  0.125
        - Blank / N/A markers                     "N/A", ""  →  None

    An optional reconciliation step computes field-level deltas against
    reference values from an authoritative system (e.g. FAFSA, a financial
    aid platform, or a tax transcript API) and assigns severity ratings:

        HIGH   — absolute delta >= $500
        MEDIUM — absolute delta >= $100
        LOW    — any non-zero delta below $100

PREREQUISITES:
    1. Python 3.8 or later.
       https://www.python.org/downloads/

    2. Install the Azure Document Intelligence client library:
       pip install azure-ai-documentintelligence

    3. Set the following environment variables:

       Windows:
           setx DOCUMENTINTELLIGENCE_ENDPOINT <your-endpoint>
           setx DOCUMENTINTELLIGENCE_API_KEY  <your-key>
           (Restart your terminal after setx.)

       macOS / Linux:
           export DOCUMENTINTELLIGENCE_ENDPOINT=<your-endpoint>
           export DOCUMENTINTELLIGENCE_API_KEY=<your-key>

       Your endpoint looks like:
           https://<resource-name>.cognitiveservices.azure.com/

       Your key is a 32-character hex string found in the Azure Portal
       under your Document Intelligence resource → Keys and Endpoint.

    4. (Optional) Install python-dotenv to load credentials from a .env file:
       pip install python-dotenv

USAGE:
    python sample_analyze_financial_documents.py

    The script runs against the bundled synthetic sample data in the
    Data/ folder. No real taxpayer information is used.

SAMPLE OUTPUT:
    --- Form 1040 ---
    FIELD                          EXTRACTED    REFERENCE      DELTA SEVERITY
    ------------------------------------------------------------------------
    agi                             83200.00      83200.00       0.00 LOW
    wages                           82000.00      82000.00       0.00 LOW
    total_tax                       11500.00      11500.00       0.00 LOW

    --- W-2 ---
    wages                           82000.00      82000.00       0.00 LOW
    federal_withheld                13200.00      13200.00       0.00 LOW

NOTE:
    Remember to remove keys from your code when done, and never post them
    publicly. For production, use Azure Key Vault or managed identity.
    https://aka.ms/azsdk/python/identity/credential
"""

import os
import re
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum
from pathlib import Path
from typing import Optional

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential

# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class Severity(str, Enum):
    HIGH   = "HIGH"
    MEDIUM = "MEDIUM"
    LOW    = "LOW"


@dataclass
class ExtractedField:
    """One normalized field extracted from a financial document."""
    field_name:       str
    raw_value:        str
    extracted_value:  Optional[Decimal]
    confidence:       Decimal
    source_doc_type:  str
    reference_value:  Optional[Decimal] = None
    delta:            Optional[Decimal] = None
    severity:         Optional[Severity] = None


# ---------------------------------------------------------------------------
# Field maps — Azure DI raw label → canonical field name
# ---------------------------------------------------------------------------

FIELD_MAP_1040 = {
    "adjusted gross income":         "agi",
    "wages salaries tips":           "wages",
    "total income":                  "total_income",
    "taxable interest":              "taxable_interest",
    "ordinary dividends":            "dividends",
    "capital gain or loss":          "capital_gain",
    "total tax":                     "total_tax",
    "federal income tax withheld":   "tax_withheld",
}

FIELD_MAP_W2 = {
    "wages tips other compensation": "wages",
    "federal income tax withheld":   "federal_withheld",
    "social security wages":         "ss_wages",
    "social security tax withheld":  "ss_tax_withheld",
    "medicare wages and tips":       "medicare_wages",
    "medicare tax withheld":         "medicare_tax_withheld",
}

# W-2 box values are never negative even if printed in parentheses.
W2_NON_NEGATIVE = {
    "wages", "federal_withheld", "ss_wages",
    "ss_tax_withheld", "medicare_wages", "medicare_tax_withheld",
}

FIELD_MAP_SCHEDULE_C = {
    "gross receipts or sales":      "gross_receipts",
    "gross profit":                 "gross_profit",
    "gross income":                 "gross_income",
    "total expenses":               "total_expenses",
    "tentative profit or loss":     "net_profit",
    "net profit or loss":           "net_profit",
}

FIELD_MAP_SCHEDULE_E = {
    "rents received":               "rental_income",
    "royalties received":           "royalties",
    "total rental real estate":     "net_rental",
    "advertising":                  "expense_advertising",
    "insurance":                    "expense_insurance",
    "mortgage interest paid":       "expense_mortgage_interest",
}

FIELD_MAP_K1 = {
    "ordinary business income loss": "ordinary_income",
    "net rental real estate income": "rental_income",
    "interest income":               "interest_income",
    "ordinary dividends":            "dividends",
    "net short term capital gain":   "st_capital_gain",
    "net long term capital gain":    "lt_capital_gain",
}


# ---------------------------------------------------------------------------
# Normalization helpers
# ---------------------------------------------------------------------------

_CURRENCY_STRIP    = re.compile(r"[$,€£¥\s]")
_PARENS_NEGATIVE   = re.compile(r"^\(([0-9,.\s]+)\)$")
_TRAILING_ALPHA    = re.compile(r"[A-Za-z%\s]+$")
_PERCENT           = re.compile(r"^([0-9.]+)%$")
_BLANK_VALUES      = {"n/a", "na", "none", "-", "", "not applicable"}


def normalize_value(raw: str, allow_negative: bool = True) -> Optional[Decimal]:
    """
    Convert a raw Azure DI string value to a Python Decimal.

    Returns None for blank, N/A, or unparseable values.
    Handles: currency symbols, comma separators, parenthetical negatives,
    percentage notation, and trailing currency codes (e.g. "USD").
    """
    stripped = raw.strip()
    if stripped.lower() in _BLANK_VALUES:
        return None

    pct_match = _PERCENT.match(stripped)
    if pct_match:
        try:
            return Decimal(pct_match.group(1)) / Decimal("100")
        except InvalidOperation:
            pass

    paren_match = _PARENS_NEGATIVE.match(stripped)
    working     = paren_match.group(1) if paren_match else stripped
    negative    = paren_match is not None and allow_negative

    working = _CURRENCY_STRIP.sub("", working)
    working = _TRAILING_ALPHA.sub("", working).strip()

    try:
        value = Decimal(working)
        return -value if negative else value
    except InvalidOperation:
        return None


def resolve_field_name(raw_key: str, field_map: dict[str, str]) -> str:
    """
    Map an Azure DI raw label to a canonical field name.
    Falls back to snake_case of the raw key if no match found.
    """
    lower = raw_key.lower().strip()
    if lower in field_map:
        return field_map[lower]
    simplified = re.sub(r"[^a-z0-9 ]", "", lower).strip()
    if simplified in field_map:
        return field_map[simplified]
    return re.sub(r"\s+", "_", simplified)


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def extract_fields(
    client:           DocumentIntelligenceClient,
    pdf_bytes:        bytes,
    field_map:        dict[str, str],
    source_doc_type:  str,
    non_negative:     set[str] | None = None,
    confidence_floor: float = 0.5,
) -> list[ExtractedField]:
    """
    Submit PDF bytes to Azure Document Intelligence (prebuilt-document model),
    then normalize the returned key-value pairs into typed ExtractedField objects.

    Args:
        client:           Authenticated DocumentIntelligenceClient.
        pdf_bytes:        Raw PDF content.
        field_map:        Raw Azure DI label → canonical field name mapping.
        source_doc_type:  Human-readable form label (e.g. "IRS Form 1040").
        non_negative:     Set of canonical field names that must never be negative.
                          Use for W-2 box values and similar always-positive fields.
        confidence_floor: Drop KV pairs below this confidence score.

    Returns:
        List of ExtractedField objects with normalized Decimal values.
    """
    poller = client.begin_analyze_document(
        "prebuilt-document",
        analyze_request=AnalyzeDocumentRequest(bytes_source=pdf_bytes),
    )
    result = poller.result()

    fields: list[ExtractedField] = []
    if not result.key_value_pairs:
        return fields

    non_negative = non_negative or set()

    for pair in result.key_value_pairs:
        if not (pair.key and pair.value):
            continue
        confidence = pair.confidence or 0.0
        if confidence < confidence_floor:
            continue

        raw_key   = pair.key.content.strip()
        raw_value = pair.value.content.strip()
        canonical = resolve_field_name(raw_key, field_map)
        allow_neg = canonical not in non_negative
        value     = normalize_value(raw_value, allow_negative=allow_neg)

        fields.append(ExtractedField(
            field_name      = canonical,
            raw_value       = raw_value,
            extracted_value = value,
            confidence      = Decimal(str(round(confidence, 4))),
            source_doc_type = source_doc_type,
        ))

    return fields


# ---------------------------------------------------------------------------
# Reconciliation — delta + severity
# ---------------------------------------------------------------------------

def reconcile(
    fields:           list[ExtractedField],
    reference_values: dict[str, float | int | Decimal],
    high_threshold:   Decimal = Decimal("500"),
    medium_threshold: Decimal = Decimal("100"),
) -> list[ExtractedField]:
    """
    Compare extracted field values against reference values from an
    authoritative system and assign severity ratings.

    Args:
        fields:           Normalized ExtractedField list.
        reference_values: Canonical field name → known-correct value.
        high_threshold:   Absolute delta >= this → HIGH severity.
        medium_threshold: Absolute delta >= this → MEDIUM severity.

    Returns:
        Same list with delta and severity populated where a reference exists.
    """
    ref = {k: Decimal(str(v)) for k, v in reference_values.items()}
    for f in fields:
        if f.field_name in ref and f.extracted_value is not None:
            ref_val = ref[f.field_name]
            delta   = ref_val - f.extracted_value
            abs_d   = abs(delta)
            f.reference_value = ref_val
            f.delta           = delta
            f.severity        = (
                Severity.HIGH   if abs_d >= high_threshold   else
                Severity.MEDIUM if abs_d >= medium_threshold else
                Severity.LOW
            )
    return fields


# ---------------------------------------------------------------------------
# Display helper
# ---------------------------------------------------------------------------

def print_results(label: str, fields: list[ExtractedField]) -> None:
    print(f"\n--- {label} ---")
    print(f"{'FIELD':<30} {'EXTRACTED':>12} {'REFERENCE':>12} {'DELTA':>10}  SEVERITY")
    print("-" * 72)
    for f in fields:
        ext = f"{f.extracted_value:.2f}" if f.extracted_value is not None else "—"
        ref = f"{f.reference_value:.2f}" if f.reference_value is not None else "—"
        dlt = f"{f.delta:.2f}"           if f.delta is not None            else "—"
        sev = f.severity.value           if f.severity is not None         else "—"
        print(f"{f.field_name:<30} {ext:>12} {ref:>12} {dlt:>10}  {sev}")


# ---------------------------------------------------------------------------
# Sample runner — one function per form type
# ---------------------------------------------------------------------------

def analyze_form_1040(client: DocumentIntelligenceClient, pdf_path: Path) -> None:
    """Extract and reconcile IRS Form 1040 fields."""
    pdf_bytes = pdf_path.read_bytes()
    fields = extract_fields(client, pdf_bytes, FIELD_MAP_1040, "IRS Form 1040")
    fields = reconcile(fields, reference_values={
        "agi":          83200,
        "wages":        82000,
        "total_income": 83200,
        "total_tax":    11500,
        "tax_withheld": 13200,
    })
    print_results("Form 1040", fields)


def analyze_w2(client: DocumentIntelligenceClient, pdf_path: Path) -> None:
    """Extract and reconcile W-2 fields."""
    pdf_bytes = pdf_path.read_bytes()
    fields = extract_fields(
        client, pdf_bytes, FIELD_MAP_W2, "W-2",
        non_negative=W2_NON_NEGATIVE,
    )
    fields = reconcile(fields, reference_values={
        "wages":           82000,
        "federal_withheld": 13200,
        "ss_wages":        82000,
        "ss_tax_withheld":  5084,
        "medicare_wages":  82000,
    })
    print_results("W-2", fields)


def analyze_schedule_c(client: DocumentIntelligenceClient, pdf_path: Path) -> None:
    """Extract and reconcile Schedule C (self-employment income) fields."""
    pdf_bytes = pdf_path.read_bytes()
    fields = extract_fields(client, pdf_bytes, FIELD_MAP_SCHEDULE_C, "Schedule C")
    fields = reconcile(fields, reference_values={
        "gross_receipts": 45000,
        "gross_income":   45500,
        "total_expenses":  8100,
        "net_profit":     37400,
    })
    print_results("Schedule C", fields)


def analyze_schedule_e(client: DocumentIntelligenceClient, pdf_path: Path) -> None:
    """Extract and reconcile Schedule E (rental income) fields."""
    pdf_bytes = pdf_path.read_bytes()
    fields = extract_fields(client, pdf_bytes, FIELD_MAP_SCHEDULE_E, "Schedule E")
    fields = reconcile(fields, reference_values={
        "rental_income": 18000,
    })
    print_results("Schedule E", fields)


def analyze_k1(client: DocumentIntelligenceClient, pdf_path: Path) -> None:
    """Extract and reconcile Schedule K-1 (Form 1065) partnership income fields."""
    pdf_bytes = pdf_path.read_bytes()
    fields = extract_fields(client, pdf_bytes, FIELD_MAP_K1, "Schedule K-1 (1065)")
    fields = reconcile(fields, reference_values={
        "ordinary_income":  18400,
        "interest_income":    320,
    })
    print_results("Schedule K-1 (1065)", fields)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_all_samples() -> None:
    endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
    key      = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]
    client   = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Resolve the Data/ folder relative to this file's location in the repo.
    # Adjust the path if running from a different working directory.
    data_dir = Path(__file__).parent.parent.parent.parent / "Data"

    samples = [
        (analyze_form_1040,   data_dir / "f1040_filled.pdf"),
        (analyze_w2,          data_dir / "fw2_filled.pdf"),
        (analyze_schedule_c,  data_dir / "f1040sc_filled.pdf"),
        (analyze_schedule_e,  data_dir / "f1040se_filled.pdf"),
        (analyze_k1,          data_dir / "f1065sk1_filled.pdf"),
    ]

    for fn, path in samples:
        if path.exists():
            fn(client, path)
        else:
            print(f"\n[SKIP] Sample file not found: {path}")
            print("       Add the filled PDF to the Data/ folder and re-run.")


if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError

    try:
        from dotenv import find_dotenv, load_dotenv
        load_dotenv(find_dotenv())
    except ImportError:
        pass  # python-dotenv is optional

    try:
        run_all_samples()
    except HttpResponseError as error:
        print(f"HttpResponseError: {error.error}")
        if error.error:
            print(f"  Code:    {error.error.code}")
            print(f"  Message: {error.error.message}")
        raise
