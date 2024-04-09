# Azure Document Intelligence client SDK Samples for .NET
> [!NOTE]
> Form Recognizer is now **Azure AI Document Intelligence**!
- Code samples for each language's SDK are in the links below. The first step is to click to choose one (default **.NET**).

|[Python](../Python(v4.0))| .NET|[Java](../Java(v4.0))| [JavaScript](../JavaScript(v4.0))|
| --- | --- | --- | --- |

-  The contents of this folder apply to the latest version: **v4.0 (2024-02-29-preview)** . 
- You can click  **[v3.1 (2023-07-31-GA)](../../v3.1(2023-07-31-GA)/.NET(v3.1))**  to view earlier versions.
## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
- [Next steps](#next-steps)

## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/?view=doc-intel-4.0.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.

## **Prerequisites**
* Azure subscription - [Create one for free](https://azure.microsoft.com/free/ai-services/).
* The current version of [Visual Studio IDE](https://visualstudio.microsoft.com/vs/).

* An Azure AI services or Document Intelligence resource. Once you have your Azure subscription,Create a [single-service](https://aka.ms/single-service) or [multi-service](https://aka.ms/multi-service) resource. You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.
For more information about creating the resource or how to get the location and sku information see [here][cognitive_resource_cli].
* [Authenticate the client](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/README.md#authenticate-the-client).
  * Get endpoint and keys to your Document Intelligence resource.
  * Create DocumentIntelligenceClient with AzureKeyCredential
  * Create DocumentIntelligenceClient with Azure Active Directory Credential



## **Setup**

Install the Azure Document Intelligence client library for .NET with [NuGet][nuget]:

```dotnetcli
dotnet add package Azure.AI.DocumentIntelligence --prerelease
```
> Note: This version of the client library defaults to the `2024-02-29-preview` version of the service.


## **Running the samples**
Below are some sample code guidelines so that you can choose the sample according to your needs.


### Common scenarios samples
- [Extract the layout of a document](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_ExtractLayout.md)
- [Analyze a document with a prebuilt model](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_AnalyzeWithPrebuiltModel.md)
- [Build a custom model](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_BuildCustomModel.md)
- [Manage models](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_ManageModels.md)
- [Classify a document](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_ClassifyDocument.md)
- [Build a document classifier](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_BuildDocumentClassifier.md)

### Advanced samples
- [Compose a model](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_ModelCompose.md)
- [Get and List document model operations](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_GetAndListOperations.md)
- [Copy a custom model between Document Intelligence resources](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_CopyCustomModel.md)
- [Analyze a document with add-on capabilities](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_AddOnCapabilities.md)
- [Extract the layout of a document as Markdown](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/samples/Sample_ExtractLayoutAsMarkdown.md)


## **Next steps**
 For more samples, see [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence).



[cognitive_resource_cli]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account-cli
[nuget]: https://www.nuget.org/