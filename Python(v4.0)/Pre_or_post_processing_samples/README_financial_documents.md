# Sample: Analyze Financial Documents

This sample demonstrates how to extract, normalize, and reconcile structured
key-value fields from financial documents using the Azure Document Intelligence
**prebuilt-document** model.

## Supported form types

| Form | Description |
|---|---|
| IRS Form 1040 | Individual income tax return |
| W-2 | Wage and tax statement |
| Schedule C | Self-employment / business income |
| Schedule E | Rental and royalty income |
| Schedule K-1 (Form 1065) | Partnership income |

## What this sample adds over basic extraction

Standard Azure DI output returns raw string KV pairs. Financial reconciliation
workflows need typed numeric values. This sample adds a post-processing layer:

**Normalization** — converts raw strings to Python `Decimal`:

| Raw Azure DI value | Normalized |
|---|---|
| `"$75,000"` | `75000` |
| `"(12,500)"` | `-12500` |
| `"75,000 USD"` | `75000` |
| `"12.5%"` | `0.125` |
| `"N/A"`, `""` | `None` |

**Non-negative field protection** — W-2 box values printed in parentheses are
positive amounts, not losses. The `non_negative` parameter suppresses negative
parsing for those fields.

**Reconciliation** — compares extracted values against reference values from an
authoritative system and assigns severity ratings:

| Severity | Condition |
|---|---|
| `HIGH` | Absolute delta ≥ $500 |
| `MEDIUM` | Absolute delta ≥ $100 |
| `LOW` | Any non-zero delta below $100 |

## Prerequisites

- Python 3.8+
- `pip install azure-ai-documentintelligence`
- `pip install python-dotenv` *(optional — for .env file support)*

## Setup

Set your Azure Document Intelligence credentials as environment variables:

**macOS / Linux:**
```bash
export DOCUMENTINTELLIGENCE_ENDPOINT=https://<resource>.cognitiveservices.azure.com/
export DOCUMENTINTELLIGENCE_API_KEY=<your-key>
```

**Windows:**
```cmd
setx DOCUMENTINTELLIGENCE_ENDPOINT https://<resource>.cognitiveservices.azure.com/
setx DOCUMENTINTELLIGENCE_API_KEY <your-key>
```
*(Restart terminal after `setx`.)*

## Run the sample

```bash
python sample_analyze_financial_documents.py
```

## Sample output

```
--- Form 1040 ---
FIELD                          EXTRACTED    REFERENCE      DELTA  SEVERITY
------------------------------------------------------------------------
agi                             83200.00      83200.00       0.00  LOW
wages                           82000.00      82000.00       0.00  LOW
total_tax                       11500.00      11500.00       0.00  LOW

--- W-2 ---
FIELD                          EXTRACTED    REFERENCE      DELTA  SEVERITY
------------------------------------------------------------------------
wages                           82000.00      82000.00       0.00  LOW
federal_withheld                13200.00      13200.00       0.00  LOW
```

## Sample data

The sample files in `Data/` were generated with entirely fictional data —
fictional names, masked SSNs (`XXX-XX-1234`), and invented dollar amounts.
No real taxpayer information was used.

## Key functions

| Function | Description |
|---|---|
| `normalize_value(raw, allow_negative)` | Parse a raw Azure DI string to `Decimal` |
| `resolve_field_name(raw_key, field_map)` | Map Azure DI label to canonical field name |
| `extract_fields(client, pdf_bytes, ...)` | Submit to Azure DI and normalize all KV pairs |
| `reconcile(fields, reference_values, ...)` | Compute delta and severity vs reference |

## Additional resources

- [Azure Document Intelligence documentation](https://aka.ms/azsdk/documentintelligence)
- [prebuilt-document model](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-general-document)
- [Python SDK reference](https://aka.ms/azsdk/python/documentintelligence/docs)
