# Azure AI Document Intelligence Code Samples（XXX topic）

> [!NOTE]
> Form Recognizer is now **Azure AI Document Intelligence**!




Code samples for each language's SDK are in the links below. Click to choose one（default **Python**）.
|Python| [.NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence)|[Java](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/documentintelligence/azure-ai-documentintelligence)| [JavaScript](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/documentintelligence/ai-document-intelligence-rest)|
| --- | --- | --- | --- |


>- The contents of this guide applies to the samples using the [latest SDK version](https://learn.microsoft.com/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true) (v4.0 Preview). Click to view earlier versions: [v3.2(GA)](), [v3.1 (GA)](), [v3.0 (GA)]().

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
  - [Samples](#samples)
- [Next steps](#next-steps)




## Features
xxx model …

## Prerequisites
* Python 3.8 or later is required to use this package
* You must have an [Azure subscription][azure_subscription]  and an [Azure Document Intelligence account][azure_document_intelligence_account] to run these samples.
* All of these samples need the endpoint to your Document Intelligence resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Document Intelligence API key ([instructions on how to get key][get-key-instructions]).

## Setup

1. Install the Azure Document Intelligence client library for Python with [pip][pip]:

```bash
pip install azure-ai-documentintelligence --pre
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. If necessary, click [Example Document](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer) to get your document URL.
4. Below are some sample code guidelines so that you can choose the sample according to your needs.

### Samples
|File-name  |       Desription      | 
| --- | --- |
|[file name](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_read.py)   |Extract…|  
|[file name](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_layout.py)   |Extract…|
| [file name](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_tax_us_w2.py)   |Extract…|
|[file name](~)   |Extract…|
|[file name](~)   |Extract…|

> Click to view earlier versions: [v3.2(GA)](), [v3.1 (GA)](), [v3.0 (GA)]().


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