// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------

using Azure;
using Azure.AI.DocumentIntelligence;

namespace Quickstarts
{
    internal partial class Samples
    {
        /// <summary>
        ///  Extract content from a given file with improved quality through the add-on high resolution capability
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task ExtractHighResolution(string? path, string? url)
        {
            if (string.IsNullOrWhiteSpace(path) && string.IsNullOrWhiteSpace(url))
            {
                // local sample file
                path = $"{Environment.CurrentDirectory}\\Assets\\read-highres.png";
                /* If want to use the online sample file, just comment out the variable "path" and uncomment variable "url".
                 * If use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
                 * If analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
                 */

                // sample file online
                // url = "https://documentintelligence.ai.azure.com/documents/samples/read/read-highres.png";
            }

            var client = new DocumentIntelligenceClient(new Uri(this.docIntelligenceEndPoint), new AzureKeyCredential(this.docIntelligenceApiKey));
            var content = new AnalyzeDocumentContent();
            if (!string.IsNullOrWhiteSpace(path))
            {
                #region Option 1: Analyze a sample document file from local file system.
                var docFileBytes = File.ReadAllBytes(path);
                content.Base64Source = BinaryData.FromBytes(docFileBytes);
                #endregion
            }
            else if (!string.IsNullOrWhiteSpace(url))
            {
                #region Option 2: Analyze a sample document file from url.
                var uriSource = new Uri(url);
                content.UrlSource = uriSource;
                #endregion
            }

            //  Specify DocumentAnalysisFeature.OcrHighResolution as the analysis features
            var features = new List<DocumentAnalysisFeature> { DocumentAnalysisFeature.OcrHighResolution };

            PromptRequestingDocumentIntelligenceService();
            var operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-read", content, features: features);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            // Extract page lines:
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

            // Detect handwritten:
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

            // Detect language:
            foreach (DocumentLanguage language in result.Languages)
            {
                Console.WriteLine($"  Found language '{language.Locale}' with confidence {language.Confidence}.");
            }
        }
    }
}
