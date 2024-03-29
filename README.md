# **Azure AI Document Intelligence Code Samples**

> [!NOTE]
> Form Recognizer is now **Azure AI Document Intelligence**!




- Code samples for each language's SDK are in the links below. The first step is to click to choose one(default **Python**).

|Python| [.NET](.NET(v4.0))|[Java](Java(v4.0))| [JavaScript](JavaScript(v4.0))|
| --- | --- | --- | --- |


- The contents of this floder default the latest version: **v4.0** .
  You can click  **[v3.1 (GA)](../v3.1(GA))**  to view earlier versions.

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
  - [Common samples](#common-samples)
  - [Retrieval Augmented Generation (RAG) samples](#retrieval-augmented-generation-rag-samples)
  - [Pre/post processing samples](#prepost-processing-samples)
- [Next steps](#next-steps)




## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/?view=doc-intel-4.0.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.

## **Prerequisites**
* Python 3.8 or later is required to use this package
* You must have an [Azure subscription][azure_subscription] and an [Azure Document Intelligence account][azure_document_intelligence_account] to run these samples.
* All of these samples need the endpoint to your Document Intelligence resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Document Intelligence API key ([instructions on how to get key][get-key-instructions]).

## **Setup**

1. Install the Azure Document Intelligence client library for Python with [pip][pip]:

```bash
pip install azure-ai-documentintelligence --pre
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## **Running the samples**

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. If necessary, click [Example Document](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/tree/master/curl/form-recognizer) to get your document URL.
4. Below are some sample code guidelines so that you can choose the sample according to your needs.

### **Common samples**

- ####  **[Read model](Python(v4.0)/Read_model/README.md)**

|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_read.py](Python(v4.0)/Read_model/sample_analyze_read.py/) and [sample_analyze_read async.py](Python(v4.0)/Read_model/sample_analyze_read_async.py/)|Read document elements, such as pages and detected languages|


- ####  **[Layout model](Python(v4.0)/Layout_model/README.md)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_layout.py](Python(v4.0)/Layout_model/sample_analyze_layout.py) and [sample_analyze_layout async.py](Python(v4.0)/Layout_model/sample_analyze_layout_async.py/) |Extract text, selection marks, and table structures in a document|
|[sample_analyze_general_documents.py](Python(v4.0)/Layout_model/sample_analyze_general_documents.py) and [sample_analyze_general_documents_async.py](Python(v4.0)/Layout_model/ssample_analyze_general_documents_async.py/) |Extract key-value pairs, selection marks, text, tables, and structure from documents|
|[sample_analyze_documents_output_in_markdown.py](Python(v4.0)/Layout_model/sample_analyze_documents_output_in_markdown.py) and [sample_analyze_documents_output_in_markdown_async.py](Python(v4.0)/Layout_model/sample_analyze_documents_output_in_markdown_async.py/) |Use markdown output to enhance the capabilities of Azure Document Intelligence Layout model and subsequently feed this refined data into Azure OpenAI service for comprehensive information extraction.|




- ####  **[Prebuilt model](Python(v4.0)/Prebuilt_model/README.md)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_invoices.py](Python(v4.0)/Prebuilt_model/sample_analyze_invoices.py) and [sample_analyze_invoices_async.py](Python(v4.0)/Prebuilt_model/sample_analyze_invoices_async.py) |Analyze document text, selection marks, tables, and pre-trained fields and values pertaining to English invoices using a prebuilt model|
|[sample_analyze_business_cards.py](Python(v4.0)/Prebuilt_model/sample_analyze_business_cards.py) and [sample_analyze_business_cards_async.py](Python(v4.0)/Prebuilt_model/sample_analyze_business_cards_async.py)  |Analyze document text and pre-trained fields and values pertaining to English business cards using a prebuilt model|
|[sample_analyze_identity_documents.py](Python(v4.0)/Prebuilt_model/sample_analyze_identity_documents.py) and [sample_analyze_identity_documents_async.py](Python(v4.0)/Prebuilt_model/sample_analyze_identity_documents_async.py)  |Analyze document text and pre-trained fields and values pertaining to US driver licenses and international passports using a prebuilt model|
|[sample_analyze_receipts.py](Python(v4.0)/Prebuilt_model/sample_analyze_receipts.py) and [sample_analyze_receipts_async.py](Python(v4.0)/Prebuilt_model/sample_analyze_receipts_async.py) |Analyze document text and pre-trained fields and values pertaining to English sales receipts using a prebuilt model|
|[sample_analyze_tax_us_w2.py](Python(v4.0)/Prebuilt_model/sample_analyze_tax_us_w2.py) and [sample_analyze_tax_us_w2_async.py](Python(v4.0)/Prebuilt_model/sample_analyze_tax_us_w2_async.py)  |Analyze document text and pre-trained fields and values pertaining to US tax W-2 forms using a prebuilt model|


- ####  **[Add-on capabilities](Python(v4.0)/Add-on_capabilities/README.md)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_addon_barcodes.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_barcodes.py)and [sample_analyze_addon_barcodes async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_barcodes_async.py)|Extract barcode|
|[sample_analyze_addon_fonts.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_fonts.py) and [sample_analyze_addon_fonts_async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_fonts_async.py)|Extract font property|
|[sample_analyze_addon_formulas.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_formulas.py) and [sample_analyze_addon_formulas_async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_formulas_async.py)|Extract formula|
|[sample_analyze_addon_highres.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_highres.py) and [sample_analyze_addon_highres_async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_highres_async.py)|Extract high resolution|
|[sample_analyze_addon_languages.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_languages.py) and [sample_analyze_addon_languages_async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_languages_async.py)|Detact language|
|[sample_analyze_addon_query_fields.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_query_fields.py) and [sample_analyze_addon_query_fields_async.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_query_fields_async.py)|Query fields|




- ####  **[Custom model](Python(v4.0)/Custom_model/README.md)**
|File Name|**Usage scenarios**|
|----------------|-------------|
|[sample_analyze_custom_documents.py](Python(v4.0)/Custom_model/sample_analyze_custom_documents.py) and [sample_analyze_custom_documents_async.py](Python(v4.0)/Custom_model/sample_analyze_custom_documents_async.py)| Analyze a document with a custom built model. The document must be of the same type as the documents the custom model was built on.|
|[sample_classify_document.py](Python(v4.0)/Custom_model/sample_classify_document.py) and [sample_classify_document_async.py](Python(v4.0)/Custom_model/sample_classify_document_async.py)| Classify a document using a trained document classifier.|
|[sample_compose_model.py](Python(v4.0)/Custom_model/sample_compose_model.py) and [sample_compose_model_async.py](Python(v4.0)/Custom_model/sample_compose_model.py)|This is useful when you have built different models and want to aggregate a group of them into a single model that you (or a user) could use to analyze a document.|
|[sample_copy_model_to.py](Python(v4.0)/Custom_model/sample_copy_model_to.py) and [sample_copy_model_to_async.py](Python(v4.0)/Custom_model/sample_copy_model_to_async.py)|Copy a custom model from a source Form Recognizer resource to a target Form Recognizer resource.|


>- Click the link of the model name to reach the corresponding topic page for more details.
>- Click  **[v3.1 (GA)](../v3.1(GA)/README.md/)** to view earlier versions.

### **Retrieval Augmented Generation (RAG) samples**
The Layout model provides various building blocks like tables, paragraphs, section headings, etc. that can enable different semantic chunking strategies of the document. With semantic chunking in Retrieval Augmented Generation (RAG), it will be more efficient in storage and retrieval, together with the benefits of improved relevance and enhanced interpretability. The following samples show how to use the Layout model to do semantic chunking and use the chunks to do RAG.
|File Name|**Usage scenarios**|
| --- | --- |
| [sample_rag_langchain.ipynb](Python(v4.0)/Retrieval_Augmented_Generation_(RAG)_samples/sample_rag_langchain.ipynb) | Sample RAG notebook using Azure AI Document Intelligence as document loader, MarkdownHeaderSplitter and Azure AI Search as retriever in Langchain |
> Only available for v4.0 (Preview) .
### **Pre/post processing samples**


There are usually some pre/post processing steps that are needed to get the best results from the Document Intelligence models. These steps are not part of the Document Intelligence service, but are common steps that are needed to get the best results. The following samples show how to do these steps.

|File Name|**Usage scenarios**|
| --- | --- |
| [sample_disambiguate_similar_characters.ipynb](Python(v4.0)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.ipynb) and [sample_disambiguate_similar_characters.py](Python(v4.0)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.py) | Sample postprocessing script to disambiguate similar characters based on business rules. |
| [sample_identify_cross_page_tables.ipynb](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.ipynb) and [sample_identify_cross_page_tables.py](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.py) | Sample postprocessing script to identify cross-page tables based on business rules. |
| [sample_identify_and_merge_cross_page_tales.ipynb](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_and_merge_cross_page_tales.ipynb) and [sample_identify_and_merge_cross_page_tales.py](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_and_merge_cross_page_tales.py) | Sample postprocessing script to identify and merge cross-page tables based on business rules. |
> Applies to all versions.




## **Next steps**

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



