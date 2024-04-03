

# Samples for Azure Document Intelligence client library for Python（Add-on capabilities）

These code samples show common scenario operations with the Azure Document Intelligence client library.

All of these samples need the endpoint to your Document Intelligence resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Document Intelligence API key ([instructions on how to get key][get-key-instructions]).

You can check all samples from [here][sample_path].

## Prerequisites
* Python 3.8 or later is required to use this package
* You must have an [Azure subscription][azure_subscription] and an
[Azure Document Intelligence account][azure_document_intelligence_account] to run these samples.

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
3. Follow the usage described in the file, e.g. `python sample_analyze_addon_barcodes.py`

|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_addon_barcodes.py](sample_analyze_addon_barcodes.py)and [sample_analyze_addon_barcodes async.py](sample_analyze_addon_barcodes_async.py)|Extract barcode|
|[sample_analyze_addon_fonts.py](sample_analyze_addon_fonts.py) and [sample_analyze_addon_fonts_async.py](sample_analyze_addon_fonts_async.py)|Extract font property|
|[sample_analyze_addon_formulas.py](sample_analyze_addon_formulas.py) and [sample_analyze_addon_formulas_async.py](sample_analyze_addon_formulas_async.py)|Extract formula|
|[sample_analyze_addon_highres.py](sample_analyze_addon_highres.py) and [sample_analyze_addon_highres_async.py](sample_analyze_addon_highres_async.py)|Extract high resolution|
|[sample_analyze_addon_languages.py](sample_analyze_addon_languages.py) and [sample_analyze_addon_languages_async.py](sample_analyze_addon_languages_async.py)|Detact language|
|[sample_analyze_addon_query_fields.py](sample_analyze_addon_query_fields.py) and [sample_analyze_addon_query_fields_async.py](sample_analyze_addon_query_fields_async.py)|Query fields|


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
