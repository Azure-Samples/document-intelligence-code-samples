#define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
#if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

/*
  This code sample shows Prebuilt Read operations with the Azure Form Recognizer client library. 

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
string key = "<AZURE_DOCUMENT_INTELLIGENCE_KEY>";

var client = new DocumentIntelligenceClient(new Uri(endpoint), new AzureKeyCredential(key));

//sample document
Uri fileUri = new Uri("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/read.png");
var content = new AnalyzeDocumentContent() { UrlSource = fileUri };

Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-read", content);
AnalyzeResult result = operation.Value;

foreach (DocumentPage page in result.Pages)
{
    Console.WriteLine($"Document Page {page.PageNumber} has {page.Lines.Count} line(s), {page.Words.Count} word(s),");

    for (int i = 0; i < page.Lines.Count; i++)
    {
        DocumentLine line = page.Lines[i];
        Console.WriteLine($"  Line {i} has content: '{line.Content}'.");

        Console.WriteLine($"    Its bounding box is:");
        Console.WriteLine($"      Upper left => X: {line.Polygon[0]}, Y= {line.Polygon[1]}");
        Console.WriteLine($"      Upper right => X: {line.Polygon[2]}, Y= {line.Polygon[3]}");
        Console.WriteLine($"      Lower right => X: {line.Polygon[4]}, Y= {line.Polygon[5]}");
        Console.WriteLine($"      Lower left => X: {line.Polygon[6]}, Y= {line.Polygon[7]}");
    }
}

foreach (DocumentStyle style in result.Styles)
{
    // Check the style and style confidence to see if text is handwritten.
    // Note that value '0.8' is used as an example.

    bool isHandwritten = style.IsHandwritten.HasValue && style.IsHandwritten == true;

    if (isHandwritten && style.Confidence > 0.8)
    {
        Console.WriteLine($"Handwritten content found:");

        foreach (DocumentSpan span in style.Spans)
        {
            Console.WriteLine($"  Content: {result.Content.Substring(span.Offset, span.Length)}");
        }
    }
}

foreach (DocumentLanguage language in result.Languages)
{
    Console.WriteLine($"  Found language '{language.Locale}' with confidence {language.Confidence}.");
}

#endif
