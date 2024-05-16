---
page_type: sample
languages:
  - python
  - csharp
  - java
  - javascript
products:
  - azure
  - ai-services
  - document-intelligence
name: Azure Document Intelligence code samples
description: Code samples for the Azure.AI.DocumentIntelligence client library.
urlFragment: document-intelligence-code-samples
---

# Azure Document Intelligence code samples repo

> Note: on July 2023, the Azure Cognitive Services Form Recognizer service was renamed to Azure AI Document Intelligence. Any mentions of Form Recognizer or Document Intelligence in documentation refer to the same Azure service.

Welcome! Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from your documents. 
- Code samples for each language's SDK are in the links below. The first step is to select to choose one (default **Python**).

|Python| [.NET](.NET(v4.0))|[Java](Java(v4.0))| [JavaScript](JavaScript(v4.0))|
| --- | --- | --- | --- |


- The contents of this folder default to the latest preview version: **v4.0 (2024-02-29-preview)** .
- Select [**v3.1 (2023-07-31-GA)**](../v3.1(2023-07-31-GA))  to view earlier versions.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run the samples](#run-the-samples)
- [Next steps](#next-steps)


## Features

Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/azure/ai-services/?view=doc-intel-4.0.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.

## Prerequisites

* Azure subscription - [Create one for free](https://azure.microsoft.com/free/ai-services/).
* [Python 3.8 or later](https://www.python.org/). Your Python installation should include [pip](https://pip.pypa.io/en/stable/). You can check if you have pip installed by running `pip --version` on the command line. Get pip by installing the latest version of Python.
* Install the latest version of [Visual Studio Code](https://code.visualstudio.com/) or your preferred IDE.   For more information, see [Getting Started with Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial).
* An Azure AI services or Document Intelligence resource.  Once you have your Azure subscription,Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource.
    You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.
* [Get endpoint and keys](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/create-document-intelligence-resource?view=doc-intel-4.0.0#get-endpoint-url-and-keys) to your Document Intelligence resource.

## Setup

1. Open a terminal window in your local environment and install the Azure AI Document Intelligence client library for Python with [pip][pip]:

```bash
pip install azure-ai-documentintelligence --pre
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Run the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. If necessary, select [Data](Data) to get your document.
4. Below are some sample code guidelines so that you can choose the sample according to your needs.   
**Note**: For more samples, see **[Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples)** and **[Async Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/aio)**.

  - [Common samples](#common-samples)
  - [Retrieval Augmented Generation (RAG) samples](#retrieval-augmented-generation-rag-samples)
  - [Pre/post processing samples](#prepost-processing-samples)

### Common samples

 Select the link of the model name to reach the corresponding topic page for more details.  Select **[v3.1 (2023-07-31-GA)](../v3.1(2023-07-31-GA))** to view earlier versions.

  [**Read model**](Python(v4.0)/Read_model): Extract printed and handwritten text. 
  
> [sample_analyze_read.py](Python(v4.0)/Read_model/sample_analyze_read.py/) 

  [**Layout model**](Python(v4.0)/Layout_model): Extract and anlayze text, tables, and document structure.
  
> [sample_analyze_layout.py](Python(v4.0)/Layout_model/sample_analyze_layout.py)

  [**Prebuilt models**](Python(v4.0)/Prebuilt_model): Add intelligent document processing to your apps and flows without having to train and build your own models.
  
> [sample_analyze_invoices.py](Python(v4.0)/Prebuilt_model/sample_analyze_invoices.py) — Extract and analyze customer and vendor details from invoice documents.  
> [sample_analyze_identity_documents.py](Python(v4.0)/Prebuilt_model/sample_analyze_identity_documents.py) — Extract and analyze identification and verification details identification documents.   
> [sample_analyze_receipts.py](Python(v4.0)/Prebuilt_model/sample_analyze_receipts.py) — Extract and analyze sales transaction details from receipt documents.  
> [sample_analyze_tax_us_w2.py](Python(v4.0)/Prebuilt_model/sample_analyze_tax_us_w2.py) — Extract and analyze taxable compensation details from US tax W-2 forms.

  [**Add-on capabilities**](Python(v4.0)/Add-on_capabilities): Extend the extracted results from documents with add-on capabilities.
  
> [sample_analyze_addon_barcodes.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_barcodes.py) - Extract barcode properties documents using this add-on capability.  
> [sample_analyze_addon_fonts.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_fonts.py) - Extract font properties from documents using this add-on capability.  
> [sample_analyze_addon_formulas.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_formulas.py) - Extract formulas from documents using this add-on capability.  
> [sample_analyze_addon_highres.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_highres.py) - Extract high resolution properties from documents using this add-on capability.  
> [sample_analyze_addon_languages.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_languages.py) - Detact language from documents using this add-on capability.  
> [sample_analyze_addon_query_fields.py](Python(v4.0)/Add-on_capabilities/sample_analyze_addon_query_fields.py) - Specify and extract query fields from documents using this add-on capability.

[**Custom model**](Python(v4.0)/Custom_model): Train your own models to extract data from structured and unstructured documents.

> [sample_analyze_custom_documents.py](Python(v4.0)/Custom_model/sample_analyze_custom_documents.py) - Analyze a document with a custom built model. The document must be of the same type as the documents the custom model was trained on.  
> [sample_classify_document.py](Python(v4.0)/Custom_model/sample_classify_document.py) - Classify a document using a trained document classifier.  
> [sample_compose_model.py](Python(v4.0)/Custom_model/sample_compose_model.py) - This is useful when you have built different models and want to aggregate a group of them into a single model that you (or a user) could use to analyze a document.  
> [sample_copy_model_to.py](Python(v4.0)/Custom_model/sample_copy_model_to.py) - Copy a custom model from a source Form Recognizer resource to a target Form Recognizer resource.  
> [sample_copy_model_to.py](Python(v4.0)/Custom_model/sample_copy_model_to.py) - Copy a custom model from a source Document Intelligence resource to a target Document Intelligence resource.  
> [sample_manage_classifiers.py](Python(v4.0)/Custom_model/sample_manage_classifiers.py) - Manage the classifiers on your account.  
> [sample_manage_models.py](Python(v4.0)/Custom_model/sample_manage_models.py) - Manage the models on your account.

 [**Additional samples**](Python(v4.0)/Others)
 
> [sample_convert_to_dict.py](Python(v4.0)/Others/sample_convert_to_dict.py) -  Convert a model returned from an analyze operation to a JSON serializable dictionary.



### Retrieval Augmented Generation (RAG) samples

The Layout model provides various building blocks like tables, paragraphs, section headings, etc. that can enable different semantic chunking strategies of the document. With semantic chunking in Retrieval Augmented Generation (RAG), it will be more efficient in storage and retrieval, together with the benefits of improved relevance and enhanced interpretability. The following samples show how to use the Layout model to do semantic chunking and use the chunks to do RAG.  
**Note**：Only available for **v4.0 (2024-02-29-preview)** .

> [**sample_rag_langchain.ipynb**](Python(v4.0)/Retrieval_Augmented_Generation_(RAG)_samples/sample_rag_langchain.ipynb)  
Sample RAG notebook using Azure AI Document Intelligence as document loader, MarkdownHeaderSplitter and Azure AI Search as retriever in Langchain.

> [**sample_figure_understanding.ipynb**](Python(v4.0)/Retrieval_Augmented_Generation_(RAG)_samples/sample_figure_understanding.ipynb)  
Sample notebook showcasing how to crop the figures and send figure content (with its caption) to Azure OpenAI GPT-4V model to understand the semantics. The figure description will be used to update the markdown output, which can be further used for [semantic chunking](https://aka.ms/doc-gen-ai).

> [**sample_identify_and_merge_cross_page_tables.ipynb**](Python(v4.0)/Retrieval_Augmented_Generation_(RAG)_samples/sample_identify_and_merge_cross_page_tables.ipynb) and **[sample_identify_and_merge_cross_page_tables.py](Python(v4.0)/Retrieval_Augmented_Generation_(RAG)_samples/sample_identify_and_merge_cross_page_tables.py)**  
Sample postprocessing script to identify and merge cross-page tables based on business rules. 

 
### Pre/post processing samples

There are usually some pre/post processing steps that are needed to get the best results from the Document Intelligence models. These steps are not part of the Document Intelligence service, but are common steps that are needed to get the best results. The following samples show how to do these steps.  
**Note**：Applies to **all versions**.

> [**sample_disambiguate_similar_characters.ipynb**](Python(v4.0)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.ipynb) and [**sample_disambiguate_similar_characters.py**](Python(v4.0)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.py): Sample postprocessing script to disambiguate similar characters based on business rules.

> [**sample_identify_cross_page_tables.ipynb**](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.ipynb) and [**sample_identify_cross_page_tables.py**](Python(v4.0)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.py):Sample postprocessing script to identify cross-page tables based on business rules. 


## Next steps

To learn more about Azure Document Intelligence features and capabilities, *see* the [**client library API reference documentation**][python-di-ref-docs].


[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity

[pip]: https://pypi.org/project/pip/

[azure_identity_pip]: https://pypi.org/project/azure-identity/
[python-di-ref-docs]: https://aka.ms/azsdk/python/documentintelligence/docs
[get-endpoint-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-endpoint
[get-key-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-api-key
[changelog]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md

### Current document analysis models

Document analysis models enable text extraction from forms and documents and return structured business-ready content ready for your organization's action, use, or development.

* **Layout** — Extract text, tables, and document structure.
* **Read** — Extract printed and handwritten text.


### Current prebuilt models

Prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models.

* **Invoice** — Extract customer and vendor details.
* **Receipt** — Extract sales transaction details.
* **Identity** — Extract identification and verification details.
* **US Mortgage 1003** — Extract mortgage loan application details.
* **US Mortgage 1008** — Extract mortgage loan transmittal details.
* **US Mortgage closing disclosure** — Extract final mortgage loan terms.
* **Health Insurance card** — Extract health insurance and coverage details.
* **Contract** — Extract agreement and party details.
* **Credit/Debit card** — Extract payment card information.
* **Marriage certificate** — Extract information from certified marriage documents.
* **US Tax W-2** — Extract taxable compensation details.
* **US Tax 1098** — Extract mortgage interest details.
* **US Tax 1098-E** — Extract student loan interest details.
* **US Tax 1098-T** — Extract qualified tuition details.
* **US Tax 1099** — Extract information from 1099 form variations.
* **US Tax 1040** — Extract information from 1040 form variations.

### Current custom models

* **Custom template** — Extract data from static layouts.
* **Custom neural** — Extract data from mixed-type documents.
* **Custom composed** — Extract data using a collection of models.
* **Custom classifier** — Identify designated document types (classes) before invoking an extraction model.

### Current add-on capabilities

✔️ **ocr.highResolution** 
✔️ **ocr.formula**
✔️ **ocr.font**
✔️ **ocr.barcode**
✔️ **queryFields**





