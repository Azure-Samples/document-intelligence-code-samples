# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_read.py

DESCRIPTION:
    This sample demonstrates how to extract document information using "prebuilt-read"
    to analyze a given file.

PREREQUISITES:
    The following prerequisites are necessary to run the code. For more details, please visit the "How-to guides" link: https://aka.ms/how-to-guide

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
    At a command prompt, run the following commands, replacing <yourKey> and <yourEndpoint> with the values from your resource in the Azure portal.
    1) For Windows:
       setx DOCUMENTINTELLIGENCE_API_KEY <yourKey>
       setx DOCUMENTINTELLIGENCE_ENDPOINT <yourEndpoint>
       • You need to restart any running programs that read the environment variable.
    2) For macOS:
       export DOCUMENTINTELLIGENCE_API_KEY=<yourKey>
       export DOCUMENTINTELLIGENCE_ENDPOINT=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/set-environment-variables-for-macOS
    3) For Linux:
       export DOCUMENTINTELLIGENCE_API_KEY=<yourKey>
       export DOCUMENTINTELLIGENCE_ENDPOINT=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/set-environment-variables-for-Linux

    ------Set up your programming environment------
    At a command prompt, run the following code to install the Azure AI Document Intelligence client library for Python with pip:
    pip install azure-ai-documentintelligence

    ------Create your Python application------
    1) Create a new Python file called "sample_analyze_read.py" in an editor or IDE.
    2) Open the "sample_analyze_read.py" file and insert the provided code sample into your application.
    3) At a command prompt, use the following command to run the Python file: 
       python sample_analyze_read.py
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return "[{}, {}], [{}, {}], [{}, {}], [{}, {}]".format(
        bounding_box[0], bounding_box[1],
        bounding_box[2], bounding_box[3],
        bounding_box[4], bounding_box[5],
        bounding_box[6], bounding_box[7]
    )

def analyze_read():
    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
    key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a document at a URL:
    formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/read.png"

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-read", AnalyzeDocumentRequest(url_source=formUrl)
    )
    result = poller.result()

    print("Document contains content: ", result.content)

    for idx, style in enumerate(result.styles):
        print(
            "Document contains {} content".format(
                "handwritten" if style.is_handwritten else "no handwritten"
            )
        )

    for page in result.pages:
        print("----Analyzing Read from page #{}----".format(page.page_number))
        print(
            "Page has width: {} and height: {}, measured with unit: {}".format(
                page.width, page.height, page.unit
            )
        )

        for line_idx, line in enumerate(page.lines):
            print(
                "...Line # {} has text content '{}' within bounding box '{}'".format(
                    line_idx,
                    line.content,
                    format_bounding_box(line.polygon),
                )
            )

        for word in page.words:
            print(
                "...Word '{}' has a confidence of {}".format(
                    word.content, word.confidence
                )
            )

    print("----------------------------------------")

if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError
    from dotenv import find_dotenv, load_dotenv

    try:
        load_dotenv(find_dotenv())
        analyze_read()
    except HttpResponseError as error:
        if error.error is not None:
            print(f"Received service error: {error.error}")
            raise
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Invalid request: {error}")
        raise

# Next steps:
# Learn more about Layout model: https://aka.ms/di-read
# Find more sample code: https://aka.ms/doc-intelligence-samples
