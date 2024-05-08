
# Azure Form Recognizer client library samples for Java

> [!NOTE]
> Form Recognizer is now **Azure AI Document Intelligence**!

- Code samples for each language's SDK are in the links below. The first step is to click to choose one (default **Java**).

|[Python](../Python(v3.1))| [.NET](../.NET(v3.1))|Java| [JavaScript](../JavaScript(v3.1))|
| --- | --- | --- | --- |
- The contents of this folder apply to the version: **v3.1 (2023-07-31-GA)** . 
- You can select  **[v4.0 (2024-02-29-preview)](../../main/Java(v4.0))**  to view the latest version.

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run the samples](#run-the-samples)
- [Next steps](#next-steps)

## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/azure/ai-services/) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.  
Azure Form Recognizer samples are a set of self-contained Java programs that demonstrate interacting with Azure Form Recognizer service/ Document Intelligence
using the client library. Each sample focuses on a specific scenario and can be executed independently.
## **Prerequisites**
- A [Java Development Kit (JDK)][jdk_link], version 8 or later.
- [Azure Subscription][azure_subscription]
- [Cognitive Services or Form Recognizer account][form_recognizer_account] to use this package.
- [Include the Package](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/formrecognizer/azure-ai-formrecognizer#include-the-package)


## **Setup**
[Authenticate the client](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/formrecognizer/azure-ai-formrecognizer#authenticate-the-client).

## **Run the samples**
The following sections provide code samples covering common scenario operations with the Azure Form Recognizer client library.

All of these samples need the endpoint to your Form Recognizer resource ([instructions on how to get endpoint][get-endpoint-instructions]), and your Form Recognizer API key ([instructions on how to get key][get-key-instructions]).

| **File Name**      | **Description**        |
|--------------------|------------------------|
| [Authentication][authentication_sample]  | Authenticate the client    |
| [AnalyzeBusinessCards][analyze_business_cards] and [AnalyzeBusinessCardsAsync][analyze_business_cards_async]  | Analyze business cards from an input stream   |
| [AnalyzeBusinessCardsFromUrl][analyze_business_cards_from_url] and [AnalyzeBusinessCardsFromUrlAsync][analyze_business_cards_from_url_async] | Analyze business cards from a URL   |
| [AnalyzeLayout][analyze_layout] and [AnalyzeLayoutAsync][analyze_layout_async]   | Analyze document layout, such as tables, lines, words, and selection marks like radio buttons and check boxes from a file stream |
| [AnalyzeLayoutFromUrl][analyze_layout_from_url] and [AnalyzeLayoutFromUrlAsync][analyze_layout_from_url_async]     | Extract document layout such as tables, lines, words, and selection marks like radio buttons and check boxes from a URL          |
| [AnalyzeIdentityDocuments][analyze_id_documents] and [AnalyzeIdentityDocumentsAsync][analyze_id_documents_async]    | Analyze data from an identity document like a passport or a US drivers license using a prebuilt model |
| [AnalyzeIdentityDocumentsFromUrl][analyze_id_documents_from_url] and [AnalyzeIdentityDocumentsFromUrlAsync][analyze_id_documents_from_url_async] | Analyze data from a URL of a passport or a US drivers license using a prebuilt model   |
| [AnalyzeInvoices][analyze_invoices] and [AnalyzeInvoiceAsync][analyze_invoices_async]     | Analyze invoices from an input stream    |
| [AnalyzeInvoicesFromUrl][analyze_invoices_from_url] and [AnalyzeInvoicesFromUrlAsync][analyze_invoices_from_url_async]                           | Analyze invoices from a URL   |
| [AnalyzeReceipts][analyze_receipts] and [AnalyzeReceiptsAsync][analyze_receipts_async]  | Analyze data from a file of a US sales receipt using a prebuilt model |
| [AnalyzeReceiptsFromUrl][analyze_receipts_from_url] and [AnalyzeReceiptsFromUrlAsync][analyze_receipts_from_url_async]  | Analyze data from a URL of a US sales receipt using a prebuilt model  |
| [AnalyzeTaxW2][analyze_w2] and [AnalyzeTaxW2Async][analyze_w2_async]                                                                             | Analyze data from a file of a US W2 Tax document using a prebuilt model   |
| [AnalyzeCustomDocumentFromUrl][analyze_custom_documents] and [AnalyzeCustomDocumentAsync][analyze_custom_documents_async]    | Analyze forms with your custom model                                                                                             |
| [BuildDocumentModel][build_model] and [BuildDocumentModelAsync][build_model_async]   | Build a custom document analysis model        |
| [ManageCustomModels][manage_custom_models] and [ManageCustomModelsAsync][manage_custom_models_async]  | Manage the custom models in your account                 |
| [CopyDocumentModel][copy_model] and [CopyDocumentModelAsync][copy_model_async]   | Copy custom model from one Form Recognizer resource to another    |
| [ComposeDocumentModel][compose_model] and [ComposeDocumentModelAsync][compose_model_async]  | Creates a composed model from a collection of existing built models with labels |
| [GetOperation][get_operation] and [GetOperationAsync][get_operation_async]         | Get/list all document model associated with the Form Recognizer resource  |
| [BuildDocumentClassifier][build_classifier] and [BuildDocumentClassifierAsync][build_classifier_async]  | Build custom classifier models that combine layout and language features  |

#
## Next steps
For more samples, see [Azure SDK for Java](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples). 


<!-- LINKS -->
[SDK_README_CONTRIBUTING]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/README.md#contributing
[SDK_README_GETTING_STARTED]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/README.md#getting-started
[SDK_README_TROUBLESHOOTING]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/README.md#troubleshooting
[SDK_README_KEY_CONCEPTS]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/README.md#key-concepts
[SDK_README_DEPENDENCY]: ../../README.md#include-the-package
[SDK_README_NEXT_STEPS]: ../../README.md#next-steps
[java_fr_ref_docs]: https://aka.ms/azsdk-java-formrecognizer-ref-doc
[get-endpoint-instructions]: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/formrecognizer/azure-ai-formrecognizer#create-a-form-recognizer-resource
[get-key-instructions]: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/formrecognizer/azure-ai-formrecognizer#create-a-form-recognizer-client-using-azurekeycredential

[authentication_sample]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/Authentication.java
[build_model]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/BuildDocumentModel.java
[build_model_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/BuildDocumentModelAsync.java
[compose_model]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ComposeDocumentModel.java
[compose_model_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ComposeDocumentModelAsync.java
[copy_model]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/CopyDocumentModel.java
[copy_model_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/CopyDocumentModelAsync.java
[manage_custom_models]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ManageCustomModels.java
[manage_custom_models_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ManageCustomModelsAsync.java
[analyze_business_cards]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeBusinessCard.java
[analyze_business_cards_async]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeBusinessCardAsync.java
[analyze_business_cards_from_url]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeBusinessCardFromUrl.java
[analyze_business_cards_from_url_async]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeBusinessCardFromUrlAsync.java
[analyze_layout]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeLayout.java
[analyze_layout_async]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeLayoutAsync.java
[analyze_layout_from_url]:https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeLayoutFromUrl.java
[analyze_layout_from_url_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeLayoutFromUrlAsync.java
[analyze_custom_documents]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeCustomDocumentFromUrl.java
[analyze_custom_documents_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeCustomDocumentAsync.java
[analyze_id_documents]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeIdentityDocuments.java
[analyze_id_documents_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeIdentityDocumentsAsync.java
[analyze_id_documents_from_url]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeIdentityDocumentsFromUrl.java
[analyze_id_documents_from_url_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeIdentityDocumentsFromUrlAsync.java
[analyze_invoices]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeInvoices.java
[analyze_invoices_async]:  https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeInvoicesAsync.java
[analyze_invoices_from_url]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeInvoicesFromUrl.java
[analyze_invoices_from_url_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeInvoicesFromUrlAsync.java
[analyze_receipts]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeReceipts.java
[analyze_receipts_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeReceiptsAsync.java
[analyze_receipts_from_url]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeReceiptsFromUrl.java
[analyze_receipts_from_url_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeReceiptsFromUrlAsync.java
[analyze_w2]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeTaxW2.java
[analyze_w2_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeTaxW2Async.java
[get_operation]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/GetOperationSummary.java
[get_operation_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/GetOperationSummaryAsync.java
[build_classifier]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/BuildDocumentClassifier.java
[build_classifier_async]: https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/BuildDocumentClassifierAsync.java


[jdk_link]: https://docs.microsoft.com/java/azure/jdk/?view=azure-java-stable
[azure_subscription]: https://azure.microsoft.com/free
[form_recognizer_account]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows

![Impressions](https://azure-sdk-impressions.azurewebsites.net/api/impressions/azure-sdk-for-java%2Fsdk%2Fformrecognizer%2Fazure-ai-formrecognizer%2FREADME.png)
