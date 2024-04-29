# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_addon_languages.py

DESCRIPTION:
    This sample demonstrates how to detect languages from the document using the
    add-on 'LANGUAGES' capability.

    Add-on capabilities are available within all models except for the Business card
    model. This sample uses Layout model to demonstrate.

    Add-on capabilities accept a list of strings containing values from the `AnalysisFeature`
    enum class. For more information, see:
    https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.analysisfeature?view=azure-python.

    The following capabilities are free:
    - BARCODES
    - LANGUAGES

    The following capabilities will incur additional charges:
    - FORMULAS
    - OCR_HIGH_RESOLUTION
    - STYLE_FONT

    See pricing: https://azure.microsoft.com/pricing/details/ai-document-intelligence/.

PREREQUISITES:
    The following prerequisites are necessary to run the code. For more details, please visit the "How-to guides" link: https://aka.ms/How-toguides

    -------Python and IDE------
    1) Install Python 3.7 or later (https://www.python.org/), which should include pip (https://pip.pypa.io/en/stable/).
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
       setx DI_KEY <yourKey>
       setx DI_ENDPOINT <yourEndpoint>
       • Close the Command Prompt window after you set your environment variables. Restart any running programs that read the environment variable.
    2) For macOS:
       export key=<yourKey>
       export endpoint=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/V3.1-set-environment-variables-for-macOS
    3) For Linux:
       export DI_KEY=<yourKey>
       export DI_ENDPOINT=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/V3.1-set-environment-variables-for-Linux
       
    ------Set up your programming environment------
    At a command prompt,run the following code to install the Azure AI Document Intelligence client library for Python with pip:
    pip install azure-ai-formrecognizer==3.3.0
    
    ------Create your Python application------
    1) Create a new Python file called "sample_analyze_addon_languages.py" in an editor or IDE.
    2) Open the "sample_analyze_read.py" file and insert the provided code sample into your application.
    3) At a command prompt, use the following code to run the Python code: 
    python sample_analyze_addon_languages.py
"""

import os


# To learn the detailed concept of "polygon" in the following content, visit: https://aka.ms/V3.1-bounding-region
def format_bounding_region(bounding_regions):
    if not bounding_regions:
        return "N/A"
    return ", ".join(
        f"Page #{region.page_number}: {format_polygon(region.polygon)}"
        for region in bounding_regions
    )


def format_polygon(polygon):
    if not polygon:
        return "N/A"
    return ", ".join([f"[{p.x}, {p.y}]" for p in polygon])


def analyze_languages():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.formrecognizer import DocumentAnalysisClient, AnalysisFeature

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DI_ENDPOINT"]
    key = os.environ["DI_KEY"]

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a document at a URL:
    url = "https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_forms/add_ons/fonts_and_languages.png?raw=true"
    # Replace with your actual url:
    # If you use the URL of a public website, to find more URLs, please visit: https://aka.ms/V3.1-more-URLs 
    # If you analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-layout", document_url=url, features=[AnalysisFeature.LANGUAGES]    # Specify which add-on capabilities to enable.
    )

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_analysis_client.begin_analyze_document(
    #         "prebuilt-layout", document=f, features=[AnalysisFeature.LANGUAGES]    # Specify which add-on capabilities to enable.
    #     )
    result = poller.result()

    # [START analyze_languages]
    # To learn the detailed concept of "span" in the following codes, visit: https://aka.ms/v3.1-spans 
    print("----Languages detected in the document----")
    print(f"Detected {len(result.languages)} languages:")
    for lang_idx, lang in enumerate(result.languages):
        print(f"- Language #{lang_idx}: locale '{lang.locale}'")
        print(f"  Confidence: {lang.confidence}")
        print(f"  Text: '{','.join([result.content[span.offset : span.offset + span.length] for span in lang.spans])}'")

    print("----------------------------------------")
    # [END analyze_languages]


if __name__ == "__main__":
    from azure.core.exceptions import HttpResponseError

    try:
        analyze_languages()
    except HttpResponseError as error:
        print(
            "For more information about troubleshooting errors, see the following guide: "
            "https://aka.ms/azsdk/python/formrecognizer/troubleshooting"
        )
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

# Next steps:
# Learn more about Add-on capabilities (Language detection): https://aka.ms/V3.1-language-detection
# Find more sample code: https://github.com/Azure-Samples/document-intelligence-code-samples