# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Mortgage 1005 operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import find_dotenv, load_dotenv

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""

load_dotenv(find_dotenv())

endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]
filepath = "YOUR_FILE_PATH"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open(filepath, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-mortgage.us.1005", body=f
    )
mortgage1005 = poller.result()

for idx, document in enumerate(mortgage1005.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    # Document Type
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    # Applicant Name and Address
    applicant = document.fields.get("ApplicantNameAndAddress")
    if applicant:
        print(
            "Applicant Name and Address: {} has confidence: {}".format(
                applicant.value_string, applicant.confidence
            )
        )

    # Applicant Signature
    applicant_signature = document.fields.get("ApplicantSignature")
    if applicant_signature:
        print(
            "Applicant Signature: {} has confidence: {}".format(
                applicant_signature.value_signature, applicant_signature.confidence
            )
        )

    # Employer Name and Address
    employer = document.fields.get("EmployerNameAndAddress")
    if employer:
        print(
            "Employer Name and Address: {} has confidence: {}".format(
                employer.value_string, employer.confidence
            )
        )

    # Employer Signature
    employer_signature = document.fields.get("EmployerSignature")
    if employer_signature:
        print(
            "Employer Signature: {} has confidence: {}".format(
                employer_signature.value_signature, employer_signature.confidence
            )
        )

    # Lender Name and Address
    lender = document.fields.get("LenderNameAndAddress")
    if lender:
        print(
            "Lender Name and Address: {} has confidence: {}".format(
                lender.value_string, lender.confidence
            )
        )

    # Lender Signature
    lender_signature = document.fields.get("LenderSignature")
    if lender_signature:
        print(
            "Lender Signature: {} has confidence: {}".format(
                lender_signature.value_signature, lender_signature.confidence
            )
        )

    # Present Employment Details
    present_employment = document.fields.get("PresentEmployment")
    if present_employment:
        print("Present Employment Details:")
        current_gross_base_pay = present_employment.value_object.get("CurrentGrossBasePay")
        if current_gross_base_pay:
            print(
                "...Current Gross Base Pay: {} has confidence: {}".format(
                    current_gross_base_pay.value_number, current_gross_base_pay.confidence
                )
            )

        employment_date = present_employment.value_object.get("EmploymentDate")
        if employment_date:
            print(
                "...Employment Date: {} has confidence: {}".format(
                    employment_date.value_date, employment_date.confidence
                )
            )

        present_position = present_employment.value_object.get("PresentPosition")
        if present_position:
            print(
                "...Present Position: {} has confidence: {}".format(
                    present_position.value_string, present_position.confidence
                )
            )

        current_gross_base_pay_period = present_employment.value_object.get("CurrentGrossBasePayPeriod")
        if current_gross_base_pay_period:
            print(
                "...Current Gross Base Pay Period: {} has confidence: {}".format(
                    current_gross_base_pay_period.value_selection_group, current_gross_base_pay_period.confidence
                )
            )
