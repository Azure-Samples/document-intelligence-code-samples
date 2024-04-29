# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_receipts.py

DESCRIPTION:
    This sample demonstrates how to analyze and extract common fields from receipts,
    using a pre-trained receipt model.

    See fields found on a receipt here:
    https://aka.ms/V3.1-receipt-field-schema

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
    1) Create a new Python file called "sample_analyze_receipts.py" in an editor or IDE.
    2) Open the "sample_analyze_read.py" file and insert the provided code sample into your application.
    3) At a command prompt, use the following code to run the Python code: 
    python sample_analyze_receipts.py
"""

import os


def analyze_receipts():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.formrecognizer import DocumentAnalysisClient

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DI_ENDPOINT"]
    key = os.environ["DI_KEY"]

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a document at a URL:
    url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"
    # Replace with your actual url:
    # If you use the URL of a public website, to find more URLs, please visit: https://aka.ms/V3.1-more-URLs 
    # If you analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-receipt", document_url=url, locale="en-US"
    )

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_analysis_client.begin_analyze_document(
    #         "prebuilt-receipt", document=f, locale="en-US"
    #     )
    receipts = poller.result()

    # [START analyze_receipts]
    for idx, receipt in enumerate(receipts.documents):
        print(f"--------Analysis of receipt #{idx + 1}--------")
        print(f"Receipt type: {receipt.doc_type if receipt.doc_type else 'N/A'}")
        merchant_name = receipt.fields.get("MerchantName")
        if merchant_name:
            print(
                f"Merchant Name: {merchant_name.value} has confidence: "
                f"{merchant_name.confidence}"
            )
        transaction_date = receipt.fields.get("TransactionDate")
        if transaction_date:
            print(
                f"Transaction Date: {transaction_date.value} has confidence: "
                f"{transaction_date.confidence}"
            )
        if receipt.fields.get("Items"):
            print("Receipt items:")
            for idx, item in enumerate(receipt.fields.get("Items").value):
                print(f"...Item #{idx + 1}")
                item_description = item.value.get("Description")
                if item_description:
                    print(
                        f"......Item Description: {item_description.value} has confidence: "
                        f"{item_description.confidence}"
                    )
                item_quantity = item.value.get("Quantity")
                if item_quantity:
                    print(
                        f"......Item Quantity: {item_quantity.value} has confidence: "
                        f"{item_quantity.confidence}"
                    )
                item_price = item.value.get("Price")
                if item_price:
                    print(
                        f"......Individual Item Price: {item_price.value} has confidence: "
                        f"{item_price.confidence}"
                    )
                item_total_price = item.value.get("TotalPrice")
                if item_total_price:
                    print(
                        f"......Total Item Price: {item_total_price.value} has confidence: "
                        f"{item_total_price.confidence}"
                    )
        subtotal = receipt.fields.get("Subtotal")
        if subtotal:
            print(f"Subtotal: {subtotal.value} has confidence: {subtotal.confidence}")
        tax = receipt.fields.get("TotalTax")
        if tax:
            print(f"Total tax: {tax.value} has confidence: {tax.confidence}")
        tip = receipt.fields.get("Tip")
        if tip:
            print(f"Tip: {tip.value} has confidence: {tip.confidence}")
        total = receipt.fields.get("Total")
        if total:
            print(f"Total: {total.value} has confidence: {total.confidence}")
        print("--------------------------------------")
    # [END analyze_receipts]


if __name__ == "__main__":
    import sys
    from azure.core.exceptions import HttpResponseError

    try:
        analyze_receipts()
    except HttpResponseError as error:
        print(
            "For more information about troubleshooting errors, see the following guide: "
            "https://aka.ms/azsdk/python/formrecognizer/troubleshooting"
        )
        # Examples of how to check an HttpResponseErrorA
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
# Learn more about Receipt model: https://aka.ms/V3.1-concept-receipt
# Find more sample code: https://github.com/Azure-Samples/document-intelligence-code-samples
