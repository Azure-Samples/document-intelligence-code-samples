# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_custom_documents.py

DESCRIPTION:
    This sample demonstrates how to analyze a document with a custom
    built model. The document must be of the same type as the documents the custom model
    was built on. To learn how to build your own models, look at
    sample_build_model.py.

USAGE:
    python sample_analyze_custom_documents.py

    Set the environment variables with your own values before running the sample:
    1) DOCUMENTINTELLIGENCE_ENDPOINT - the endpoint to your Document Intelligence resource.
    2) DOCUMENTINTELLIGENCE_API_KEY - your Document Intelligence API key.
    3) CUSTOM_BUILT_MODEL_ID - the ID of your custom built model.
"""

"""
This code sample shows Custom Extraction Model operations with the Azure AI Document Intelligence client library.
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
model_id = os.environ["CUSTOM_BUILT_MODEL_ID"]
document_path = "YOUR_DOCUMENT_PATH"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
with open(document_path, "rb") as fd:
    document = fd.read()
    poller = document_intelligence_client.begin_analyze_document(
        model_id, AnalyzeDocumentRequest(bytes_source=document)
    )
result = poller.result()

for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))
    for name, field in document.fields.items():
        print("......found field of type '{}' with value '{}' and with confidence {}".format(field.type, field.content, field.confidence))


# iterate over tables, lines, and selection marks on each page
for page in result.pages:
    print("\nLines found on page {}".format(page.page_number))
    for line in page.lines:
        print("...Line '{}'".format(line.content.encode('utf-8')))
    for word in page.words:
        print(
            "...Word '{}' has a confidence of {}".format(
                word.content.encode('utf-8'), word.confidence
            )
        )
    if page.selection_marks:
        for selection_mark in page.selection_marks:
            print(
                "...Selection mark is '{}' and has a confidence of {}".format(
                    selection_mark.state, selection_mark.confidence
                )
            )

for i, table in enumerate(result.tables):
    print("\nTable {} can be found on page:".format(i + 1))
    for region in table.bounding_regions:
        print("...{}".format(i + 1, region.page_number))
    for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.row_index, cell.column_index, cell.content.encode('utf-8')
            )
        )
print("-----------------------------------")
