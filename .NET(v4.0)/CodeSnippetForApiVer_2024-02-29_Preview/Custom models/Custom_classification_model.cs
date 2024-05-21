//#define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
#if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

/*
  This code sample shows Custom Classification Models operations with the Azure Form Recognizer client library. 

  To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
  https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-csharp
*/

using Azure;
using Azure.AI.DocumentIntelligence;

/*
  Remember to remove the key from your code when you're done, and never post it publicly. For production, use
  secure methods to store and access your credentials. For more information, see 
  https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
*/

string endpoint = "<AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT>";
string apiKey = "<AZURE_DOCUMENT_INTELLIGENCE_KEY>";

var client = new DocumentIntelligenceClient(new Uri(endpoint), new AzureKeyCredential(apiKey));

string modelId = "<CUSTOM_BUILT_MODEL_ID>";
Uri fileUri = new("<SAMPLE_DOCUMENT_URL>");
var content = new ClassifyDocumentContent() { UrlSource = fileUri };

Operation<AnalyzeResult> operation = await client.ClassifyDocumentAsync(WaitUntil.Completed, modelId, content);

AnalyzeResult result = operation.Value;

Console.WriteLine($"Document was analyzed with model with ID: {result.ModelId}");

foreach (AnalyzedDocument document in result.Documents)
{
    Console.WriteLine($"Document of type: {document.DocType}, with confidence {document.Confidence}");
}

#endif