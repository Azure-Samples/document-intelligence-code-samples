
# Azure AI Document Intelligence client library samples for JavaScript

- Code samples for each language's SDK are in the links below. The first step is to click to choose one (default **JavaScript**).

|[Python](../Python(v3.1))| [.NET](../.NET(v3.1))|[Java](../Java(v3.1))| JavaScript|
| --- | --- | --- | --- |
- The contents of this folder apply to the version: **v3.1 (2023-07-31-GA)** . 
- You can select  **[v4.0 (2024-02-29-preview)](../../main/JavaScript(v4.0))**  to view the latest version.  

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the samples](#running-the-samples)
- [Next steps](#next-steps)
## **Features**
Azure AI Document Intelligence is a cloud-based [Azure AI service](https://learn.microsoft.com/azure/ai-services/) that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation.  


## Prerequisites

The sample programs are compatible with [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule).

You need [an Azure subscription][freesub] and the following Azure resources to run these sample programs:

- [Azure Cognitive Services account][createinstance_azurecognitiveservicesaccount]

Samples retrieve credentials to access the service endpoint from environment variables. Alternatively, edit the source code to include the appropriate credentials. See each individual sample for details on which environment variables/credentials it requires to function.

Adapting the samples to run in the browser may require some additional consideration. For details, please see the [package README][package].

## Setup

To run the samples using the published version of the package:

1. Install the dependencies using `npm`:

```bash
npm install
```

2. Edit the file `sample.env`, adding the correct credentials to access the Azure service and run the samples. Then rename the file from `sample.env` to just `.env`. The sample programs will read this file automatically.

3. Run whichever samples you like (note that some samples may require additional setup, see the table above):

```bash
node composeModel.js
```

Alternatively, run a single sample with the correct environment variables set (setting up the `.env` file is not required if you do this), for example (cross-platform):

```bash
npx cross-env FORM_RECOGNIZER_ENDPOINT="<form recognizer endpoint>" FORM_RECOGNIZER_API_KEY="<form recognizer api key>" PURCHASE_ORDER_SUPPLIES_SAS_URL="<purchase order supplies sas url>" PURCHASE_ORDER_EQUIPMENT_SAS_URL="<purchase order equipment sas url>" PURCHASE_ORDER_FURNITURE_SAS_URL="<purchase order furniture sas url>" PURCHASE_ORDER_CLEANING_SUPPLIES_SAS_URL="<purchase order cleaning supplies sas url>" node composeModel.js
```
## Running the samples
These sample programs show how to use the JavaScript client libraries for Azure AI Document Intelligence in some common scenarios.


| **File Name**  | **Description**   |
| -------------- | ----------------- |
| [composeModel.js][composemodel]                         | create a composed model from several individual labeled models                             |
| [analyzeDocumentByModelId.js][analyzedocumentbymodelid] | analyze a document using a model by ID                                                     |
| [analyzeReceiptByModelId.js][analyzereceiptbymodelid]   | use the "prebuilt-receipt" model ID to extract data from a receipt document (weakly-typed) |
| [buildClassifier.js][buildclassifier]                   | build a classifier from a training data set                                                |
| [buildModel.js][buildmodel]                             | build a model with a single document type from a training data set                         |
| [classifyDocument.js][classifydocument]                 | use a custom classifier to classify a document                                             |
| [copyModel.js][copymodel]                               | copy a model from one resource to another                                                  |
| [getClassifier.js][getclassifier]                       | get information about a classifier by its ID                                               |
| [getInfo.js][getinfo]                                   | get information about the count and limit of custom models in the resource                 |
| [getModel.js][getmodel]                                 | get information about a model by its ID                                                    |
| [listClassifiers.js][listclassifiers]                   | iterate over the classifiers in a resource                                                 |
| [listModels.js][listmodels]                             | iterate over the models in a resource                                                      |
| [readDocument.js][readdocument]                         | use the prebuilt "read" model to extract information about the text content of a document  |



## Next Steps

For more samples, see [Azure SDK for JavaScript](https://github.com/witemple-msft/azure-sdk-for-js/tree/ai-form-recognizer/5.0.0-release/sdk/formrecognizer/ai-form-recognizer/samples/v5).

[composemodel]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/composeModel.js
[analyzedocumentbymodelid]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/analyzeDocumentByModelId.js
[analyzereceiptbymodelid]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/analyzeReceiptByModelId.js
[buildclassifier]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/buildClassifier.js
[buildmodel]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/buildModel.js
[classifydocument]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/classifyDocument.js
[copymodel]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/copyModel.js
[getclassifier]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/getClassifier.js
[getinfo]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/getInfo.js
[getmodel]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/getModel.js
[listclassifiers]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/listClassifiers.js
[listmodels]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/listModels.js
[readdocument]: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/formrecognizer/ai-form-recognizer/samples/v5/javascript/readDocument.js
[apiref]: https://docs.microsoft.com/javascript/api/@azure/ai-form-recognizer
[freesub]: https://azure.microsoft.com/free/
[createinstance_azurecognitiveservicesaccount]: https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account
[package]: https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/formrecognizer/ai-form-recognizer/README.md
