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
- [Setup programming environment](#setup-programming-environment)
- [Run the samples](#run-the-samples)
- [Next steps](#next-steps)

## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/?view=doc-intel-4.0.0) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.  
This sample program is built based on .Net Console application. It shows common scenario operations with the Azure Document Intelligence client library.

## **Prerequisites**
The following prerequisites are necessary to run the sample program. For more details, please visit the [Get started with Document Intelligence SDKs](https://aka.ms/AApsqd6).  

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
2. Download this sample code and fill the [app.config](Quickstarts/app.config) with the endpoint and key which got from previous steps.


## **Run the samples**
1. Below are some sample code guidelines so that you can choose the sample according to your needs. 
2. Execute the "Build" command in [Visual Studio IDE](https://visualstudio.microsoft.com/vs/).
2. After building successfully, click the "▶"(debug button) or press the F5 keyboard's shortcut to start up.  

### Common scenarios samples
- [Extract the layout of a document](Quickstarts/Samples/Sample_ExtractLayout.cs)
- [Analyze a document with a prebuilt model](Quickstarts/Samples/Sample_AnalyzeWithPrebuiltModel.cs)

### Analyze a document with add-on capabilities
- [Detect Language](Quickstarts/Samples/Sample_AddOnCapabilities_DetectLanguage.cs)
- [Extract Barcode Property](Quickstarts/Samples/Sample_AddOnCapabilities_ExtractBarcodeProperty.cs)
- [Extract Font Property](Quickstarts/Samples/Sample_AddOnCapabilities_ExtractFontProperty.cs)
- [Extract Formula](Quickstarts/Samples/Sample_AddOnCapabilities_ExtractFormula.cs)
- [Extract High Resolution](Quickstarts/Samples/Sample_AddOnCapabilities_ExtractHighResolution.cs)
- [Extract Key-Value Pairs](Quickstarts/Samples/Sample_AddOnCapabilities_ExtractKeyValuePairs.cs)


## **Next steps**
-  For more samples, see [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence).  
-  Check out the [documentation](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview) to learn more about what you can do with the Azure Document Intelligence client library.



[cognitive_resource_cli]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account-cli
[nuget]: https://www.nuget.org/
