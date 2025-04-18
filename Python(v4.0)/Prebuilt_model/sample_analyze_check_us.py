# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Checks operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]
filepath = "YOUR_FILE_PATH"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open(filepath, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-check.us", body=f
    )
uschecks = poller.result()

for idx, document in enumerate(uschecks.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))
    
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))
    
    bank_name = document.fields.get("BankName")
    if bank_name:
        print(
            "Bank Name: {} has confidence: {}".format(
                bank_name.value_string, bank_name.confidence
            )
        )
    
    check_date = document.fields.get("CheckDate")
    if check_date:
        print(
            "Check Date: {} has confidence: {}".format(
                check_date.value_date, check_date.confidence
            )
        )
    
    memo = document.fields.get("Memo")
    if memo:
        print(
            "Memo: {} has confidence: {}".format(
                memo.value_string, memo.confidence
            )
        )
    
    micr = document.fields.get("MICR")
    if micr:
        print(
            "MICR: {} with confidence: {}".format(
                micr.content, micr.confidence
            )
        )
        routing_number = micr.value_object.get("RoutingNumber")
        if routing_number:
            print(
                "Routing Number: {} with confidence: {}".format(
                    routing_number.value_string, micr.confidence
                )
            )
        account_number = micr.value_object.get("AccountNumber")
        if account_number:
            print(
                "Account Number: {} with confidence: {}".format(
                    account_number.value_string, micr.confidence
                )
            )
        check_number = micr.value_object.get("CheckNumber")
        if check_number:
            print(
                "Check Number: {} with confidence: {}".format(
                    check_number.value_string, micr.confidence
                )
            )
    
    number_amount = document.fields.get("NumberAmount")
    if number_amount:
        print(
            "Numeric Amount: {} has confidence: {}".format(
                number_amount.value_number, number_amount.confidence
            )
        )
    
    word_amount = document.fields.get("WordAmount")
    if word_amount:
        print(
            "Word Amount: {} has confidence: {}".format(
                word_amount.value_number, word_amount.confidence
            )
        )
    
    payer_name = document.fields.get("PayerName")
    if payer_name:
        print(
            "Payer Name: {} has confidence: {}".format(
                payer_name.value_string, payer_name.confidence
            )
        )
    
    payer_address = document.fields.get("PayerAddress")
    if payer_address:
        print(
            "Payer Address: {} has confidence: {}".format(
                payer_address.value_address, payer_address.confidence
            )
        )
    
    payer_signatures = document.fields.get("PayerSignatures")
    if payer_signatures:
        for sig_idx, signature in enumerate(payer_signatures.value_array):
            print(
                "Payer Signature #{}: {} has confidence: {}".format(
                    sig_idx + 1, signature.value_signature, signature.confidence
                )
            )
    
    pay_to = document.fields.get("PayTo")
    if pay_to:
        print(
            "Pay To: {} has confidence: {}".format(
                pay_to.value_string, pay_to.confidence
            )
        )
    
    print("--------------------------------------")
