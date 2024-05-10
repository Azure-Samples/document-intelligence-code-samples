//#define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
#if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

/*
  This code sample shows Custom Extraction Models operations with the Azure Form Recognizer client library. 

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
AzureKeyCredential credential = new AzureKeyCredential(apiKey);

var client = new DocumentIntelligenceClient(new Uri(endpoint), new AzureKeyCredential(apiKey));

string modelId = "<CUSTOM_BUILT_MODEL_ID>";
Uri fileUri = new Uri("<SAMPLE_DOCUMENT_URL>");
var content = new AnalyzeDocumentContent() { UrlSource = fileUri };

Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, modelId, content);

AnalyzeResult result = operation.Value;

Console.WriteLine($"Document was analyzed with model with ID: {result.ModelId}");

foreach (AnalyzedDocument document in result.Documents)
{
    Console.WriteLine($"Document of type: {document.DocType}");

    foreach (KeyValuePair<string, DocumentField> fieldKvp in document.Fields)
    {
        string fieldName = fieldKvp.Key;
        DocumentField field = fieldKvp.Value;

        Console.WriteLine($"Field '{fieldName}': ");

        Console.WriteLine($"  Content: '{field.Content}'");
        Console.WriteLine($"  Confidence: '{field.Confidence}'");
    }
}

// Iterate over lines and selection marks on each page
foreach (DocumentPage page in result.Pages)
{
    Console.WriteLine($"Lines found on page {page.PageNumber}");
    foreach (var line in page.Lines)
    {
        Console.WriteLine($"  {line.Content}");
    }

    Console.WriteLine($"Selection marks found on page {page.PageNumber}");
    foreach (var selectionMark in page.SelectionMarks)
    {
        Console.WriteLine($"  Selection mark is '{selectionMark.State}' with confidence {selectionMark.Confidence}");
    }
}

// Iterate over the document tables
for (int i = 0; i < result.Tables.Count; i++)
{
    Console.WriteLine($"Table {i + 1}");
    foreach (var cell in result.Tables[i].Cells)
    {
        Console.WriteLine($"  Cell[{cell.RowIndex}][{cell.ColumnIndex}] has content '{cell.Content}' with kind '{cell.Kind}'");
    }
}

#endif