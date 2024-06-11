# coding: utf-8

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: authenticate_with_user-assigned_managed_identity.py

DESCRIPTION:
    This sample demonstrates how to analyze document with user-assigned managed identity.

PREREQUISITES:
Set the environment variables with your own values before running the sample:
    1) DOCUMENTINTELLIGENCE_ENDPOINT - the endpoint to your Document Intelligence resource.

To obtain these parameters, please reference the document in (..\\..\\Doc\\Prerequisites For Authentication With User-Assigned Managed Identity.md)
    
USAGE:
    python authenticate_with_user-assigned_managed_identity.py
"""

import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import (
    AnalyzeResult,
    AnalyzeDocumentRequest,
)
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from dotenv import find_dotenv, load_dotenv


def authenticate_with_service_principal():
    endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=DefaultAzureCredential()
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-tax.us.w2",
        AnalyzeDocumentRequest(
            url_source="https://documentintelligence.ai.azure.com/documents/samples/prebuilt/w2-single.png"
        ),
    )

    result: AnalyzeResult = poller.result()

    if result.documents:
        for idx, document in enumerate(result.documents):
            print(f"--------Analyzing document #{idx + 1}--------")
            print(f"Document has type {document.doc_type}")
            print(f"Document has document type confidence {document.confidence}")
            print(f"Document was analyzed with model with ID {result.model_id}")
            if document.fields:
                for name, field in document.fields.items():
                    field_value = (
                        field.get("valueString")
                        if field.get("valueString")
                        else field.content
                    )
                    print(
                        f"......found field of type '{field.type}' with value '{field_value}' and with confidence {field.confidence}"
                    )

    print("----------------------------------------")


if __name__ == "__main__":

    try:
        load_dotenv(find_dotenv())
        authenticate_with_service_principal()
    except HttpResponseError as error:
        # Examples of how to check an HttpResponseError
        # Check by error code:
        if error.error is not None:
            if error.error.code == "InvalidImage":
                print(f"Received an invalid image error: {error.error}")
            if error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            # Raise the error again after printing it
            raise
        # If the inner error is None and then it is possible to check the message to get more information:
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Uh-oh! Seems there was an invalid request: {error}")
        # Raise the error again
        raise
