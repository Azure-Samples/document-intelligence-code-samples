# Azure Form Recognizer client SDK Samples for .NET

> Note: on July 2023, the Azure Cognitive Services Form Recognizer service was renamed to Azure AI Document Intelligence. Any mentions to Form Recognizer or Document Intelligence in documentation refer to the same Azure service.

- Code samples for each language's SDK are in the links below. The first step is to click to choose one (default **.NET**).

|[Python](../Python(v3.1))| .NET|[Java](../Java(v3.1))| [JavaScript](../JavaScript(v3.1))|
| --- | --- | --- | --- |
-  The contents of this folder apply to the version: **v3.1 (2023-07-31-GA)** . 
- You can select  **[v4.0 (2024-02-29-preview)](../../main/.NET(v4.0))**  to view the latest version.
## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup programming environment](#setup-programming-environment)
- [Run the samples](#run-the-samples)
- [Next steps](#next-steps)
 
## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/azure/ai-services/) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.  
This sample program is built based on .Net Console application. It shows common scenario operations with the Azure Document Intelligence client library.
## **Prerequisites**
The following prerequisites are necessary to run the sample program. For more details, please visit the [Get started with Document Intelligence SDKs](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-3.1.0&pivots=programming-language-csharp).  

* **Azure subscription**  - [Create one for free](https://azure.microsoft.com/free/ai-services/).  
* **Azure AI services or Document Intelligence resource**  
Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource.
You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.  
* **Get the key and endpoint**    
1 - After your resource is deployed, select "Go to resource".   
2 - In the left navigation menu, select "Keys and Endpoint".   
3 - Copy one of the keys and the Endpoint for use in this sample. 

## **Setup programming environment**

1. Install the current version of [Visual Studio IDE](https://visualstudio.microsoft.com/vs/).
2. You can set `endpoint` and `apiKey` based on an environment variable, a configuration setting, or any way that works for your application.

```C# Snippet:CreateFormRecognizerClient
string endpoint = "<endpoint>";
string apiKey = "<apiKey>";
var credential = new AzureKeyCredential(apiKey);
var client = new FormRecognizerClient(new Uri(endpoint), credential);
```
## **Run the samples**
1. Below are some sample code guidelines so that you can choose the sample according to your needs. 
2. Execute the "Build" command in [Visual Studio IDE](https://visualstudio.microsoft.com/vs/).
2. After building successfully, click the "▶"(debug button) or press the F5 keyboard's shortcut to start up. 

### Common scenarios samples
- [Recognize form content](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample1_RecognizeFormContent.md)
- [Recognize custom forms](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample2_RecognizeCustomForms.md)
- [Recognize receipts](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample3_RecognizeReceipts.md)
- [Recognize business cards](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample9_RecognizeBusinessCards.md)
- [Recognize invoices](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample10_RecognizeInvoices.md)
- [Recognize identity documents](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample11_RecognizeIdentityDocuments.md)
- [Train a model](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample5_TrainModel.md)
- [Manage custom models](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample6_ManageCustomModels.md)

### Advanced samples
- [Strongly-typing a recognized form](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample4_StronglyTypingARecognizedForm.md)
- [Create a composed model](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample8_ModelCompose.md)
- [Differentiate output models trained with and without labels](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/tests/samples/V3.1/Sample10_DifferentiateOutputModelsTrainedWithAndWithoutLabels.cs)
- [Differentiate output labeled tables](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/tests/samples/V3.1/Sample15_DifferentiateOutputLabeledTables.cs)
- [Copy a custom model between Form Recognizer resources](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample7_CopyCustomModel.md)
- [Field Bounding Box](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/tests/samples/V3.1/Sample9_FieldBoundingBox.cs)
- [Mock a client for testing using the Moq library](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1/Sample_MockClient.md)

[changelog]: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/CHANGELOG.md
[v31samples]: V3.1/README.md
[migration_guide]: https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/MigrationGuide.md

## **Next steps**
For more samples, see [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/V3.1).  

