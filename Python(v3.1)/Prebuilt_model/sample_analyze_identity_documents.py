# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_identity_documents.py

DESCRIPTION:
    This sample demonstrates how to analyze an identity document.

    See fields found on identity documents here:
    https://aka.ms/V3.1-iddocument-field-schema

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
    1) Create a new Python file called "sample_analyze_identity_documents.py" in an editor or IDE.
    2) Open the "sample_analyze_identity_documents.py" file and insert the provided code sample into your application.
    3) At a command prompt, use the following code to run the Python code: 
    python sample_analyze_identity_documents.py
"""

import os


def analyze_identity_documents():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.formrecognizer import DocumentAnalysisClient    

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DI_ENDPOINT"]
    key = os.environ["DI_KEY"]

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a document at a URL:
    url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/identity_documents.png"
    # Replace with your actual url:
    # If you use the URL of a public website, to find more URLs, please visit: https://aka.ms/V3.1-more-URLs 
    # If you analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-idDocument", document_url=url
    )

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_analysis_client.begin_analyze_document(
    #         "prebuilt-idDocument", document=f
    #     )
    id_documents = poller.result()

    # [START analyze_idDocuments]
    for idx, id_document in enumerate(id_documents.documents):
        print(f"--------Analyzing ID document #{idx + 1}--------")
        first_name = id_document.fields.get("FirstName")
        if first_name:
            print(
                f"First Name: {first_name.value} has confidence: {first_name.confidence}"
            )
        last_name = id_document.fields.get("LastName")
        if last_name:
            print(
                f"Last Name: {last_name.value} has confidence: {last_name.confidence}"
            )
        document_number = id_document.fields.get("DocumentNumber")
        if document_number:
            print(
                f"Document Number: {document_number.value} has confidence: {document_number.confidence}"
            )
        dob = id_document.fields.get("DateOfBirth")
        if dob:
            print(f"Date of Birth: {dob.value} has confidence: {dob.confidence}")
        doe = id_document.fields.get("DateOfExpiration")
        if doe:
            print(f"Date of Expiration: {doe.value} has confidence: {doe.confidence}")
        sex = id_document.fields.get("Sex")
        if sex:
            print(f"Sex: {sex.value} has confidence: {sex.confidence}")
        address = id_document.fields.get("Address")
        if address:
            print(f"Address: {address.value} has confidence: {address.confidence}")
        country_region = id_document.fields.get("CountryRegion")
        if country_region:
            print(
                f"Country/Region: {country_region.value} has confidence: {country_region.confidence}"
            )
        region = id_document.fields.get("Region")
        if region:
            print(f"Region: {region.value} has confidence: {region.confidence}")
    # [END analyze_idDocuments]

if __name__ == "__main__":
    import sys
    from azure.core.exceptions import HttpResponseError

    try:
        analyze_identity_documents()
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
# Learn more about ID document model: https://aka.ms/V3.1-concept-id-document
# Find more sample code: https://github.com/Azure-Samples/document-intelligence-code-samples
