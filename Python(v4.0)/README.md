---
page_type: sample
languages:
  - python
products:
  - azure
  - azure-cognitive-services
  - azure-document-intelligence
urlFragment: documentintelligence-samples
---

# Samples for Azure Document Intelligence client library for Python

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
3. Follow the usage described in the file, e.g. `python sample_analyze_receipts.py`
### **Common samples**

- ####  **[Read model](Read_model)**

|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_read.py](Read_model/sample_analyze_read.py/) and [sample_analyze_read async.py](Read_model/sample_analyze_read_async.py/)|Read document elements, such as pages and detected languages|


- ####  **[Layout model](Layout_model)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_layout.py](Layout_model/sample_analyze_layout.py) and [sample_analyze_layout async.py](Layout_model/sample_analyze_layout_async.py/) |Extract text, selection marks, and table structures in a document|
|[sample_analyze_general_documents.py](Layout_model/sample_analyze_general_documents.py) and [sample_analyze_general_documents_async.py](Layout_model/ssample_analyze_general_documents_async.py/) |Extract key-value pairs, selection marks, text, tables, and structure from documents|
|[sample_analyze_documents_output_in_markdown.py](Layout_model/sample_analyze_documents_output_in_markdown.py) and [sample_analyze_documents_output_in_markdown_async.py](Layout_model/sample_analyze_documents_output_in_markdown_async.py/) |Use markdown output to enhance the capabilities of Azure Document Intelligence Layout model and subsequently feed this refined data into Azure OpenAI service for comprehensive information extraction.|




- ####  **[Prebuilt model](Prebuilt_model)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_invoices.py](Prebuilt_model/sample_analyze_invoices.py) and [sample_analyze_invoices_async.py](Prebuilt_model/sample_analyze_invoices_async.py) |Analyze document text, selection marks, tables, and pre-trained fields and values pertaining to English invoices using a prebuilt model|
|[sample_analyze_business_cards.py](Prebuilt_model/sample_analyze_business_cards.py) and [sample_analyze_business_cards_async.py](Prebuilt_model/sample_analyze_business_cards_async.py)  |Analyze document text and pre-trained fields and values pertaining to English business cards using a prebuilt model|
|[sample_analyze_identity_documents.py](Prebuilt_model/sample_analyze_identity_documents.py) and [sample_analyze_identity_documents_async.py](Prebuilt_model/sample_analyze_identity_documents_async.py)  |Analyze document text and pre-trained fields and values pertaining to US driver licenses and international passports using a prebuilt model|
|[sample_analyze_receipts.py](Prebuilt_model/sample_analyze_receipts.py) and [sample_analyze_receipts_async.py](Prebuilt_model/sample_analyze_receipts_async.py) |Analyze document text and pre-trained fields and values pertaining to English sales receipts using a prebuilt model|
|[sample_analyze_tax_us_w2.py](Prebuilt_model/sample_analyze_tax_us_w2.py) and [sample_analyze_tax_us_w2_async.py](Prebuilt_model/sample_analyze_tax_us_w2_async.py)  |Analyze document text and pre-trained fields and values pertaining to US tax W-2 forms using a prebuilt model|


- ####  **[Add-on capabilities](Add-on_capabilities)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_addon_barcodes.py](Add-on_capabilities/sample_analyze_addon_barcodes.py)and [sample_analyze_addon_barcodes async.py](Add-on_capabilities/sample_analyze_addon_barcodes_async.py)|Extract barcode from a document using this add-on capability.|
|[sample_analyze_addon_fonts.py](Add-on_capabilities/sample_analyze_addon_fonts.py) and [sample_analyze_addon_fonts_async.py](Add-on_capabilities/sample_analyze_addon_fonts_async.py)|Extract font property from a document using this add-on capability.|
|[sample_analyze_addon_formulas.py](Add-on_capabilities/sample_analyze_addon_formulas.py) and [sample_analyze_addon_formulas_async.py](Add-on_capabilities/sample_analyze_addon_formulas_async.py)|Extract formula from a document using this add-on capability.|
|[sample_analyze_addon_highres.py](Add-on_capabilities/sample_analyze_addon_highres.py) and [sample_analyze_addon_highres_async.py](Add-on_capabilities/sample_analyze_addon_highres_async.py)|Extract high resolution from a document using this add-on capability.|
|[sample_analyze_addon_languages.py](Add-on_capabilities/sample_analyze_addon_languages.py) and [sample_analyze_addon_languages_async.py](Add-on_capabilities/sample_analyze_addon_languages_async.py)|Detact language from a document using this add-on capability.|
|[sample_analyze_addon_query_fields.py](Add-on_capabilities/sample_analyze_addon_query_fields.py) and [sample_analyze_addon_query_fields_async.py](Add-on_capabilities/sample_analyze_addon_query_fields_async.py)|Query fields from a document using this add-on capability.|




- ####  **[Custom model](Custom_model)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_custom_documents.py](Custom_model/sample_analyze_custom_documents.py) and [sample_analyze_custom_documents_async.py](Custom_model/sample_analyze_custom_documents_async.py)| Analyze a document with a custom built model. The document must be of the same type as the documents the custom model was built on.|
|[sample_classify_document.py](Custom_model/sample_classify_document.py) and [sample_classify_document_async.py](Custom_model/sample_classify_document_async.py)| Classify a document using a trained document classifier.|
|[sample_compose_model.py](Custom_model/sample_compose_model.py) and [sample_compose_model_async.py](Custom_model/sample_compose_model.py)|This is useful when you have built different models and want to aggregate a group of them into a single model that you (or a user) could use to analyze a document.|
|[sample_copy_model_to.py](Custom_model/sample_copy_model_to.py) and [sample_copy_model_to_async.py](Custom_model/sample_copy_model_to_async.py)|Copy a custom model from a source Form Recognizer resource to a target Form Recognizer resource.|


- ####  **[Others](Python(v4.0))**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_convert_to_dict.py](Others/sample_convert_to_dict.py) and [sample_convert_to_dict_async.py](Others/sample_convert_to_dict_async.py)| Convert a model returned from an analyze operation to a JSON serializable dictionary.|
|[sample_copy_model_to.py](Others/sample_copy_model_to.py) and [sample_copy_model_to_async.py](Others/sample_copy_model_to_async.py)| copy a custom model from a source Document Intelligence resource to a target Document Intelligence resource.|
|[sample_manage_classifiers.py](Others/sample_manage_classifiers.py) and [sample_manage_classifiers_async.py](Others/sample_manage_classifiers_async.py)|  Manage the classifiers on your account.|
|[sample_manage_models.py](Others/sample_manage_models.py) and [sample_manage_models_async.py](Others/sample_manage_models_async.py)| Manage the models on your account.|


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
