"""
This code sample shows Prebuilt US Tax 1040 operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-tax.us.1040", body=f
    )
tax1040 = poller.result()

for idx, document in enumerate(tax1040.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))
    
    tax_year = document.fields.get("TaxYear")
    if tax_year:
        print(
            "Tax Year: {} has confidence: {}".format(
                tax_year.value_string, tax_year.confidence
            )
        )

    print("--------------------------------------")
