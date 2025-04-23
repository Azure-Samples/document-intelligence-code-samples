# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Marriage Certificate operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-marriageCertificate.us", body=f
    )
marriageCertificates = poller.result()

for idx, document in enumerate(marriageCertificates.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))
    
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))
    
    issue_date = document.fields.get("IssueDate")
    if issue_date:
        print(
            "Issue Date: {} has confidence: {}".format(
                issue_date.value_date, issue_date.confidence
            )
        )
    
    marriage_date = document.fields.get("MarriageDate")
    if marriage_date:
        print(
            "Marriage Date: {} has confidence: {}".format(
                marriage_date.value_date, marriage_date.confidence
            )
        )
    
    marriage_place = document.fields.get("MarriagePlace")
    if marriage_place:
        print(
            "Marriage Place: {} has confidence: {}".format(
                marriage_place.value_string, marriage_place.confidence
            )
        )
    
    # Spouse 1 details
    spouse1_first_name = document.fields.get("Spouse1FirstName")
    if spouse1_first_name:
        print(
            "Spouse 1 First Name: {} has confidence: {}".format(
                spouse1_first_name.value_string, spouse1_first_name.confidence
            )
        )
    
    spouse1_middle_name = document.fields.get("Spouse1MiddleName")
    if spouse1_middle_name:
        print(
            "Spouse 1 Middle Name: {} has confidence: {}".format(
                spouse1_middle_name.value_string, spouse1_middle_name.confidence
            )
        )
    
    spouse1_last_name = document.fields.get("Spouse1LastName")
    if spouse1_last_name:
        print(
            "Spouse 1 Last Name: {} has confidence: {}".format(
                spouse1_last_name.value_string, spouse1_last_name.confidence
            )
        )
    
    spouse1_age = document.fields.get("Spouse1Age")
    if spouse1_age:
        print(
            "Spouse 1 Age: {} has confidence: {}".format(
                spouse1_age.value_integer, spouse1_age.confidence
            )
        )
    
    spouse1_birth_place = document.fields.get("Spouse1BirthPlace")
    if spouse1_birth_place:
        print(
            "Spouse 1 Birth Place: {} has confidence: {}".format(
                spouse1_birth_place.value_string, spouse1_birth_place.confidence
            )
        )
    
    spouse1_address = document.fields.get("Spouse1Address")
    if spouse1_address:
        print(
            "Spouse 1 Address: {} has confidence: {}".format(
                spouse1_address.value_address, spouse1_address.confidence
            )
        )
    
    # Spouse 2 details
    spouse2_first_name = document.fields.get("Spouse2FirstName")
    if spouse2_first_name:
        print(
            "Spouse 2 First Name: {} has confidence: {}".format(
                spouse2_first_name.value_string, spouse2_first_name.confidence
            )
        )
    
    spouse2_middle_name = document.fields.get("Spouse2MiddleName")
    if spouse2_middle_name:
        print(
            "Spouse 2 Middle Name: {} has confidence: {}".format(
                spouse2_middle_name.value_string, spouse2_middle_name.confidence
            )
        )
    
    spouse2_last_name = document.fields.get("Spouse2LastName")
    if spouse2_last_name:
        print(
            "Spouse 2 Last Name: {} has confidence: {}".format(
                spouse2_last_name.value_string, spouse2_last_name.confidence
            )
        )
    
    spouse2_age = document.fields.get("Spouse2Age")
    if spouse2_age:
        print(
            "Spouse 2 Age: {} has confidence: {}".format(
                spouse2_age.value_integer, spouse2_age.confidence
            )
        )
    
    spouse2_birth_place = document.fields.get("Spouse2BirthPlace")
    if spouse2_birth_place:
        print(
            "Spouse 2 Birth Place: {} has confidence: {}".format(
                spouse2_birth_place.value_string, spouse2_birth_place.confidence
            )
        )
    
    spouse2_address = document.fields.get("Spouse2Address")
    if spouse2_address:
        print(
            "Spouse 2 Address: {} has confidence: {}".format(
                spouse2_address.value_address, spouse2_address.confidence
            )
        )
    
    print("--------------------------------------")
