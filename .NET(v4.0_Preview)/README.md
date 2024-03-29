---
page_type: sample
languages:
- csharp
products:
- azure
- azure-cognitive-services
- azure-form-recognizer
name: Azure Document Intelligence samples for .NET
description: Samples for the Azure.AI.DocumentIntelligence client library
---

# Azure Document Intelligence client SDK Samples

>- Note: on July 2023, the Azure Cognitive Services Form Recognizer service was renamed to Azure AI Document Intelligence. Any mentions of Form Recognizer or Document Intelligence in documentation refer to the same Azure service.
>- The contents of this folder apply to the latest version: **v4.0 (Preview)** . 
You can click  **[v3.1 (GA)](../v3.1(GA)/.NET(v3.1_GA)/README.md/)**  to view earlier versions.

Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from your documents. It includes the following main features:

- Layout - Extract text, selection marks, table structures, styles, and paragraphs, along with their bounding region coordinates from documents.
- Read - Read information about textual elements, such as page words and lines in addition to text language information.
- Prebuilt - Analyze data from certain types of common documents using prebuilt models. Supported documents include receipts, invoices, business cards, identity documents, vaccination cards, US W2 tax forms, and US health insurance cards.
- Custom analysis - Build custom document models to analyze text, field values, selection marks, table structures, styles, and paragraphs from documents. Custom models are built with your own data, so they're tailored to your documents.
- Custom classification - Build custom classifier models that combine layout and language features to accurately detect and identify documents you process within your application.

## Common scenarios samples
- [Extract the layout of a document](Sample_ExtractLayout.md)
- [Analyze a document with a prebuilt model](Sample_AnalyzeWithPrebuiltModel.md)
- [Build a custom model](Sample_BuildCustomModel.md)
- [Manage models](Sample_ManageModels.md)
- [Classify a document](Sample_ClassifyDocument.md)
- [Build a document classifier](Sample_BuildDocumentClassifier.md)

## Advanced samples
- [Compose a model](Sample_ModelCompose.md)
- [Get and List document model operations](Sample_GetAndListOperations.md)
- [Copy a custom model between Document Intelligence resources](Sample_CopyCustomModel.md)
- [Analyze a document with add-on capabilities](Sample_AddOnCapabilities.md)
- [Extract the layout of a document as Markdown](Sample_ExtractLayoutAsMarkdown.md)
