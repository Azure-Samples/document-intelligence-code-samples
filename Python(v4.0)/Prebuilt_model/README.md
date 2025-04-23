
# Samples for Azure Document Intelligence client library for Python（Prebuilt model）

These code samples show common scenario operations with the Azure Document Intelligence client library.

All of these samples need the endpoint to your Document Intelligence resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Document Intelligence API key ([instructions on how to get key][get-key-instructions]).

You can check all samples from [here][sample_path].

## Prerequisites
* Azure subscription - [Create one for free](https://azure.microsoft.com/free/ai-services/).
* [Python 3.8 or later](https://www.python.org/). Your Python installation should include [pip](https://pip.pypa.io/en/stable/). You can check if you have pip installed by running `pip --version` on the command line. Get pip by installing the latest version of Python.
* Install the latest version of [Visual Studio Code](https://code.visualstudio.com/) or your preferred IDE.  * For more information, see [Getting Started with Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial).
* An Azure AI services or Document Intelligence resource. * Once you have your Azure subscription,Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource.
    You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.
* [Get endpoint and keys](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/create-document-intelligence-resource?view=doc-intel-4.0.0#get-endpoint-url-and-keys) to your Document Intelligence resource.

## Set your environment variables
    
At a command prompt, run the following commands, replacing ```<yourKey>``` and ```<yourEndpoint>``` with the values from your resource in the Azure portal.
- For Windows:  
```setx DOCUMENTINTELLIGENCE_API_KEY <yourKey>```   
```setx DOCUMENTINTELLIGENCE_ENDPOINT <yourEndpoint>```   
   You need to restart any running programs that read the environment variable.
- For macOS:  
```export DOCUMENTINTELLIGENCE_API_KEY=<yourKey>```  
```export DOCUMENTINTELLIGENCE_ENDPOINT=<yourEndpoint>```  
       • This is a temporary environment variable setting method that only lasts until you close the terminal session.   
       • To set an environment variable permanently, visit: https://aka.ms/set-environment-variables-for-macOS
- For Linux:  
```export DOCUMENTINTELLIGENCE_API_KEY=<yourKey>```  
```export DOCUMENTINTELLIGENCE_ENDPOINT=<yourEndpoint>```  
       • This is a temporary environment variable setting method that only lasts until you close the terminal session.   
       • To set an environment variable permanently, visit: https://aka.ms/set-environment-variables-for-Linux

## Setup

1. Install the Azure Document Intelligence client library for Python with [pip][pip]:

```bash
pip install azure-ai-documentintelligence
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Create your Python application

1. Create a new Python file called "sample_analyze_receipts.py" in an editor or IDE.
2. Open the "sample_analyze_receipts.py" file and insert the provided code sample into your application.
3. At a command prompt, use the following code to run the Python code: 
       python sample_analyze_receipts.py

## Run the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Follow the usage described in the file, e.g. `python sample_analyze_receipts.py`

|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_bank_statement.py](sample_analyze_bank_statement.py) |Analyze document text and pre-trained fields and values pertaining to bank statements using a prebuilt model|
|[sample_analyze_check_us.py](sample_analyze_check_us.py) |Analyze check images and extract check fields using a prebuilt model|
|[sample_analyze_contracts.py](sample_analyze_contracts.py) |Analyze document text and key fields in legal contracts using a prebuilt model|
|[sample_analyze_credit_cards.py](sample_analyze_credit_cards.py) |Analyze document text and key information on credit cards using a prebuilt model|
|[sample_analyze_health_insurance_cards.py](sample_analyze_health_insurance_cards.py) |Analyze document text and pre-trained fields on US health insurance cards using a prebuilt model|
|[sample_analyze_identity_documents.py](sample_analyze_identity_documents.py) |Analyze document text and pre-trained fields and values pertaining to ID documents using a prebuilt model|
|[sample_analyze_invoices.py](sample_analyze_invoices.py) |Analyze document text, selection marks, tables, and pre-trained fields and values pertaining to English invoices using a prebuilt model|
|[sample_analyze_marriage_certificates.py](sample_analyze_marriage_certificates.py) |Analyze document text and fields in US marriage certificates using a prebuilt model|
|[sample_analyze_mortgage_1003.py](sample_analyze_mortgage_1003.py) |Analyze fields and values in the US Mortgage 1003 using a prebuilt model|
|[sample_analyze_mortgage_1004.py](sample_analyze_mortgage_1004.py) |Analyze fields and values in the US Mortgage 1004 using a prebuilt model|
|[sample_analyze_mortgage_1005.py](sample_analyze_mortgage_1005.py) |Analyze fields and values in the US Mortgage 1005 using a prebuilt model|
|[sample_analyze_mortgage_1008.py](sample_analyze_mortgage_1008.py) |Analyze fields and values in the US Mortgage 1008 using a prebuilt model|
|[sample_analyze_mortgage_closing_disclosure.py](sample_analyze_mortgage_closing_disclosure.py) |Analyze fields and values in the US Mortgage Closing Disclosure using a prebuilt model|
|[sample_analyze_pay_stub.py](sample_analyze_pay_stub.py) |Analyze document text and structured information on pay stubs using a prebuilt model|
|[sample_analyze_receipts.py](sample_analyze_receipts.py) |Analyze document text and pre-trained fields and values pertaining to receipts using a prebuilt model|
|[sample_analyze_tax_us_w2.py](sample_analyze_tax_us_w2.py)  |Analyze document text and pre-trained fields and values pertaining to US tax W-2 forms using a prebuilt model.<br>Below are US tax forms supported by the model:<br>**US personal tax**<br>**US tax W-2**<br>**US tax W-4**<br>**US tax 1040**<br>**US tax 1095**<br>**US tax 1098**<br>**US tax 1099**<br>|



## Next steps

Check out the [API reference documentation][python-di-ref-docs] to learn more about
what you can do with the Azure Document Intelligence client library.


[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity

[pip]: https://pypi.org/project/pip/
[azure_subscription]: https://azure.microsoft.com/free/
[azure_document_intelligence_account]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account?tabs=singleservice%2Cwindows
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[python-di-ref-docs]: https://aka.ms/azsdk/python/documentintelligence/docs
[get-endpoint-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-endpoint
[get-key-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-api-key
[changelog]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md


[sample_path]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples
