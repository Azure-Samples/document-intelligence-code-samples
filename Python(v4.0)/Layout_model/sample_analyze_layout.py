# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_layout.py

DESCRIPTION:
    This sample demonstrates how to extract text, tables, figures, selection marks and document structure (e.g., sections) information 
    from a document given through a file.

PREREQUISITES:
    The following prerequisites are necessary to run the code. For more details, please visit the "Quickstart" link:
    https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python

    -------Python and IDE------
    1) Install Python 3.8 or later (https://www.python.org/), which should include pip (https://pip.pypa.io/en/stable/).
    2) Install the latest version of Visual Studio Code (https://code.visualstudio.com/) or your preferred IDE.

    ------Azure AI services or Document Intelligence resource------
    Create a single-service (https://aka.ms/single-service) or multi-service (https://aka.ms/multi-service) resource.
    You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.

    ------Get the key and endpoint------
    1) After your resource is deployed, select "Go to resource".
    2) In the left navigation menu, select "Keys and Endpoint".
    3) Copy one of the keys and the Endpoint for use in this sample.

    ------Set your environment variables------
    It is recommended to use environment variables to store your endpoint and key. 
    For example, in Linux or macOS:
        export DOCUMENTINTELLIGENCE_ENDPOINT=<yourEndpoint>
        export DOCUMENTINTELLIGENCE_API_KEY=<yourKey>
    For Windows:
        setx DOCUMENTINTELLIGENCE_ENDPOINT <yourEndpoint>
        setx DOCUMENTINTELLIGENCE_API_KEY <yourKey>

    ------Install the Document Intelligence library------
    pip install azure-ai-documentintelligence --pre

    ------Run this Python sample------
    Save the file as "sample_analyze_layout_v2.py" and run:
        python sample_analyze_layout_v2.py
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest


def analyze_layout_from_url():
    # Set your endpoint and key from environment variables
    # For how to set them, see PREREQUISITES above.
    endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
    key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a sample document layout using its URL
    formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-layout", AnalyzeDocumentRequest(url_source=formUrl)
    )
    result = poller.result()

    # Analyze styles (e.g., whether the document contains handwritten content)
    if result.styles:
        for idx, style in enumerate(result.styles):
            print(
                "Document contains {} content".format(
                    "handwritten" if style.is_handwritten else "no handwritten"
                )
            )

    # Analyze pages
    for page in result.pages:
        print(f"----Analyzing layout from page #{page.page_number}----")

        # Analyze lines
        if page.lines:
            for line_idx, line in enumerate(page.lines):
                print(
                    f"...Line #{line_idx} has text content '{line.content}'"
                )

        # Analyze selection marks
        if page.selection_marks:
            for selection_mark in page.selection_marks:
                print(
                    f"...Selection mark is '{selection_mark.state}' "
                    f"and has a confidence of {selection_mark.confidence}"
                )

    # Analyze tables
    if result.tables:
        for table_idx, table in enumerate(result.tables):
            print(
                f"Table #{table_idx} has {table.row_count} rows and {table.column_count} columns"
            )
            for cell in table.cells:
                print(
                    f"...Cell[{cell.row_index}][{cell.column_index}] has content '{cell.content}'"
                )

    print("----------------------------------------")


if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError

    try:
        analyze_layout_from_url()
    except HttpResponseError as error:
        # Examples of how to check an HttpResponseError
        if error.error is not None:
            if error.error.code == "InvalidImage":
                print(f"Received an invalid image error: {error.error}")
            elif error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            raise
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Uh-oh! Seems there was an invalid request: {error}")
        raise

# Next steps:
# Learn more about Layout model: https://aka.ms/di-layout
# Find more sample code: https://aka.ms/doc-intelligence-samples
