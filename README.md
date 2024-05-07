
# **Azure AI Document Intelligence Code Samples**

> Note: on July 2023, the Azure Cognitive Services Form Recognizer service was renamed to Azure AI Document Intelligence. Any mentions of Form Recognizer or Document Intelligence in documentation refer to the same Azure service.

Welcome! Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from your documents. 

- Code samples for each language's SDK are in the links below. The first step is to select to choose one (default **Python**).

|Python| [.NET](.NET(v3.1))|[Java](Java(v3.1))| [JavaScript](JavaScript(v3.1))|
| --- | --- | --- | --- |


- The contents of this floder default the version: ** v3.1 (2023-07-31-GA) **.  
  You can select  **[v4.0 (2024-02-29-preview) )](../main)**  to view the latest version.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
- [Next steps](#next-steps)

## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/?view=doc-intel-3.1.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.

## **Prerequisites**
* Azure subscription - [Create one for free](https://azure.microsoft.com/free/ai-services/).
* [Python 3.7 or later](https://www.python.org/). Your Python installation should include [pip](https://pip.pypa.io/en/stable/). You can check if you have pip installed by running `pip --version` on the command line. Get pip by installing the latest version of Python.
* Install the latest version of [Visual Studio Code](https://code.visualstudio.com/) or your preferred IDE. For more information, see [Getting Started with Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial).
* An Azure AI services or Document Intelligence resource. Once you have your Azure subscription, Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource.
    You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.
* [Get endpoint and keys](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/create-document-intelligence-resource?view=doc-intel-3.1.0#get-endpoint-url-and-keys) to your Document Intelligence resource.

## **Setup**

1. Open a terminal window in your local environment and install the Azure AI Document Intelligence client library for Python with [pip][pip]:

```bash
pip install azure-ai-formrecognizer==3.3.0
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples
  
1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Below are some sample code guidelines so that you can choose the sample according to your needs.  
**Note**: For more samples, see **[Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples)** and **[Async Samples](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.2_and_later/async_samples)**.
- [Common samples](#common-samples)
- [Pre/post processing samples](#prepost-processing-samples)  
### **Common samples**
Select the link of the model name to reach the corresponding topic page for more details.  Select **[v4.0 (2024-02-29-preview)](../main)** to view the latest version.  

**[ Read model ](Python(v3.1)/Read_model)**: Extract printed and handwritten text.
> [sample_analyze_read.py](Python(v3.1)/Read_model/sample_analyze_read.py/) 

 **[ Layout mode ](Python(v3.1)/Layout_model)**: Extract and anlayze text, tables, and document structure.
> [sample_analyze_layout.py](Python(v3.1)/Layout_model/sample_analyze_layout.py)  

 **[ Prebuilt model ](Python(v3.1)/Prebuilt_model)**: Add intelligent document processing to your apps and flows without having to train and build your own models.
>  [sample_analyze_invoices.py](Python(v3.1)/Prebuilt_model/sample_analyze_invoices.py)  - Analyze document text, selection marks, tables, and pre-trained fields and values pertaining to English invoices using a prebuilt model.  
>  [sample_analyze_identity_documents.py](Python(v3.1)/Prebuilt_model/sample_analyze_identity_documents.py)  - Analyze document text and pre-trained fields and values pertaining to US driver licenses and international passports using a prebuilt model.  
> [sample_analyze_receipts.py](Python(v3.1)/Prebuilt_model/sample_analyze_receipts.py) - Analyze document text and pre-trained fields and values pertaining to English sales receipts using a prebuilt model.  
>  [sample_analyze_tax_us_w2.py](Python(v3.1)/Prebuilt_model/sample_analyze_tax_us_w2.py)  - Analyze document text and pre-trained fields and values pertaining to US tax W-2 forms using a prebuilt model. 

**[ Add-on capabilities ](Python(v3.1)/Add-on_capabilities)**: Extend the extracted results from documents with add-on capabilities. 
>  [sample_analyze_addon_barcodes.py](Python(v3.1)/Add-on_capabilities/sample_analyze_addon_barcodes.py) - Extract barcode from a document using this add-on capability.  
>  [sample_analyze_addon_fonts.py](Python(v3.1)/Add-on_capabilities/sample_analyze_addon_fonts.py) - Extract font property from a document using this add-on capability.  
> [sample_analyze_addon_formulas.py](Python(v3.1)/Add-on_capabilities/sample_analyze_addon_formulas.py) - Extract formula from a document using this add-on capability.  
>  [sample_analyze_addon_highres.py](Python(v3.1)/Add-on_capabilities/sample_analyze_addon_highres.py) - Extract high resolution from a document using this add-on capability.  
> [sample_analyze_addon_languages.py](Python(v3.1)/Add-on_capabilities/sample_analyze_addon_languages.py) - Detact language from a document using this add-on capability.  

### **Pre/post processing samples**
There are usually some pre/post processing steps that are needed to get the best results from the Document Intelligence models. These steps are not part of the Document Intelligence service, but are common steps that are needed to get the best results. The following samples show how to do these steps.  
**Note**：Applies to **all versions**.    

>**[sample_disambiguate_similar_characters.ipynb](Python(v3.1)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.ipynb)** and **[sample_disambiguate_similar_characters.py](Python(v3.1)/Pre_or_post_processing_samples/sample_disambiguate_similar_characters.py)**  
Sample postprocessing script to disambiguate similar characters based on business rules.

> **[sample_identify_cross_page_tables.ipynb](Python(v3.1)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.ipynb)** and **[sample_identify_cross_page_tables.py](Python(v3.1)/Pre_or_post_processing_samples/sample_identify_cross_page_tables.py)**  
Sample postprocessing script to identify cross-page tables based on business rules. 

## **Next steps**

Check out the [API reference documentation][python-di-ref-docs] to learn more about
what you can do with the Azure Document Intelligence client library.

  
[azure_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity

[pip]: https://pypi.org/project/pip/

[azure_identity_pip]: https://pypi.org/project/azure-identity/
[python-di-ref-docs]: https://aka.ms/azsdk/python/documentintelligence/docs
[get-endpoint-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-endpoint
[get-key-instructions]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/README.md#get-the-api-key 
[changelog]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/CHANGELOG.md

### Current document analysis models

Document analysis models enable text extraction from forms and documents and return structured business-ready content ready for your organization's action, use, or development.

* **Layout** — Extract text, tables, checkbox.
* **Read** — Extract printed and handwritten text.


### Current prebuilt models

Prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models.

* **Invoice** — Extract customer and vendor details.
* **Receipt** — Extract sales transaction details.
* **Identity** — Extract identification and verification details.
* **Health Insurance card** — Extract health insurance and coverage details.
* **Contract** — Extract agreement and party details.
* **US Tax W-2** — Extract taxable compensation details.
* **US Tax 1098** — Extract mortgage interest details.

### Current add-on capabilities

✔️ **ocr.highResolution** 
✔️ **ocr.formula**
✔️ **ocr.font**
✔️ **ocr.barcode**
✔️ **languages**