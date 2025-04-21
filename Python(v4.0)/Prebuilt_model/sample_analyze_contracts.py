# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt Contracts operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-contract", body=f
    )
contract = poller.result()

for idx, document in enumerate(contract.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    title = document.fields.get("Title")
    if title:
        print(
            "Title: {} has confidence: {}".format(
                title.value_string, title.confidence
            )
        )

    effective_date = document.fields.get("EffectiveDate")
    if effective_date:
        print(
            "Effective Date: {} has confidence: {}".format(
                effective_date.value_date, effective_date.confidence
            )
        )

    parties = document.fields.get("Parties")
    if parties:
        for party_idx, party in enumerate(parties.value_array):
            print(
                "Party #{}: {} has confidence: {}".format(
                    party_idx + 1, party.value_string, party.confidence
                )
            )

    jurisdictions = document.fields.get("Jurisdictions")
    if jurisdictions:
        for jurisdiction_idx, jurisdiction in enumerate(jurisdictions.value_array):
            print("Jurisdiction #{}:".format(jurisdiction_idx + 1))
            
            # Extracting Region and Clause
            region = jurisdiction.value_object.get("Region")
            if region:
                print(
                    "Region: {} has confidence: {}".format(
                        region.value_string, region.confidence
                    )
                )
            
            clause = jurisdiction.value_object.get("Clause")
            if clause:
                print(
                    "Clause: {} has confidence: {}".format(
                        clause.value_string, clause.confidence
                    )
                )

    print("--------------------------------------")
