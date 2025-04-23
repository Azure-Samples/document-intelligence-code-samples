# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Tax W-2 operations with the Azure AI Document Intelligence client library.
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from dotenv import find_dotenv, load_dotenv

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""

load_dotenv(find_dotenv())

endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]

# sample document
formUrl = "https://formrecognizer.appliedai.azure.com/documents/samples/prebuilt/w2-multiple.png"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

poller = document_intelligence_client.begin_analyze_document(
    "prebuilt-tax.us.w2", AnalyzeDocumentRequest(url_source=formUrl)
)
w2s = poller.result()

for idx, w2 in enumerate(w2s.documents):
    print("--------Recognizing W-2 #{}--------".format(idx + 1))
    for name, field in w2.fields.items():
        if name == "AdditionalInfo":
            print ("W-2 Additional Info:")
            for idy, item in enumerate(field.value_array):
                print("...Additional Info#{}".format(idy+1))
                for item_field_name, item_field in item.value_object.items():
                    if item_field_name == "LetterCode":
                        item_field_value = item_field.value_string
                    elif item_field_name == "Amount":
                        item_field_value = item_field.value_number
                    else:
                        item_field_value = None
                    print("......{}: {} has confidence {}".format(
                        item_field_name, item_field_value, item_field.confidence))
        if name == "Employee":
            print ("W-2 Employee Info:")
            for i, (item_field_name, item_field) in enumerate(field.value_object.items()):
                if item_field_name in ["SocialSecurityNumber", "Name"]:
                    item_field_value = item_field.value_string
                elif item_field_name == "Address":
                    item_field_value = item_field.value_address
                else:
                    item_field_value = None
                print("...{}: {} has confidence {}".format(item_field_name, item_field_value, item_field.confidence))
        if name == "Employer":
            print ("W-2 Employer Info:")
            for i, (item_field_name, item_field) in enumerate(field.value_object.items()):
                if item_field_name in ["Name", "IdNumber"]:
                    item_field_value = item_field.value_string
                elif item_field_name == "Address":
                    item_field_value = item_field.value_address
                else:
                    item_field_value = None
                print("...{}: {} has confidence {}".format(item_field_name, item_field_value, item_field.confidence))
        if name == "LocalTaxInfos":
            print ("W-2 Local Tax Info:")
            for idy, item in enumerate(field.value_array):
                print("...Local Tax Info#{}".format(idy+1))
                for item_field_name, item_field in item.value_object.items():
                    if item_field_name == "LocalityName":
                        item_field_value = item_field.value_string
                    elif item_field_name in ["LocalWagesTipsEtc", "LocalIncomeTax"]:
                        item_field_value = item_field.value_number
                    else:
                        item_field_value = None
                    print("......{}: {} has confidence {}".format(
                        item_field_name, item_field_value, item_field.confidence))
        if name == "StateTaxInfos":
            print ("W-2 State Tax Info:")
            for idy, item in enumerate(field.value_array):
                print("...State Tax Info#{}".format(idy+1))
                for item_field_name, item_field in item.value_object.items():
                    if item_field_name in ["State", "EmployerStateIdNumber"]:
                        item_field_value = item_field.value_string
                    elif item_field_name in ["StateWagesTipsEtc", "StateIncomeTax"]:
                        item_field_value = item_field.value_number
                    else:
                        item_field_value = None
                    print("......{}: {} has confidence {}".format(
                        item_field_name, item_field_value, item_field.confidence))
        else:
            print("{}: {} has confidence {}".format(name, field.content, field.confidence))
    print("----------------------------------------")
