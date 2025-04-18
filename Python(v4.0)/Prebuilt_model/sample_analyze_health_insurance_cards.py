# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Health Insurance Card operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-healthInsuranceCard.us", body=f
    )
insurance_card = poller.result()

for idx, document in enumerate(insurance_card.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    insurer = document.fields.get("Insurer")
    if insurer:
        print(
            "Insurer: {} has confidence: {}".format(
                insurer.value_string, insurer.confidence
            )
        )

    group_number = document.fields.get("GroupNumber")
    if group_number:
        print(
            "Group Number: {} has confidence: {}".format(
                group_number.value_string, group_number.confidence
            )
        )

    id_number = document.fields.get("IdNumber")
    if id_number:
        number = id_number.value_object.get("Number")
        if number:
            print(
                "ID Number: {} has confidence: {}".format(
                    number.value_string, number.confidence
                )
            )
        prefix = id_number.value_object.get("Prefix")
        if prefix:
            print(
                "ID Number Prefix: {} has confidence: {}".format(
                    prefix.value_string, prefix.confidence
                )
            )

    member = document.fields.get("Member")
    if member:
        employer = member.value_object.get("Employer")
        if employer:
            print(
                "Employer: {} has confidence: {}".format(
                    employer.value_string, employer.confidence
                )
            )
        id_suffix = member.value_object.get("IdNumberSuffix")
        if id_suffix:
            print(
                "ID Number Suffix: {} has confidence: {}".format(
                    id_suffix.value_string, id_suffix.confidence
                )
            )
        name = member.value_object.get("Name")
        if name:
            print(
                "Member Name: {} has confidence: {}".format(
                    name.value_string, name.confidence
                )
            )

    plan = document.fields.get("Plan")
    if plan:
        plan_number = plan.value_object.get("Number")
        if plan_number:
            print(
                "Plan Number: {} has confidence: {}".format(
                    plan_number.value_string, plan_number.confidence
                )
            )
        plan_name = plan.value_object.get("Name")
        if plan_name:
            print(
                "Plan Name: {} has confidence: {}".format(
                    plan_name.value_string, plan_name.confidence
                )
            )

    copays = document.fields.get("Copays")
    if copays:
        for copay_idx, copay in enumerate(copays.value_array):
            benefit = copay.value_object.get("Benefit")
            amount = copay.value_object.get("Amount")
            if benefit and amount:
                print(
                    "Copay #{} - Benefit: {} with Amount: {} (confidence: {})".format(
                        copay_idx + 1,
                        benefit.value_string,
                        amount.value_number,
                        copay.confidence,
                    )
                )

    prescription_info = document.fields.get("PrescriptionInfo")
    if prescription_info:
        rx_bin = prescription_info.value_object.get("RxBIN")
        if rx_bin:
            print(
                "RxBIN: {} has confidence: {}".format(
                    rx_bin.value_string, rx_bin.confidence
                )
            )
        rx_grp = prescription_info.value_object.get("RxGrp")
        if rx_grp:
            print(
                "RxGrp: {} has confidence: {}".format(
                    rx_grp.value_string, rx_grp.confidence
                )
            )

    print("--------------------------------------")
