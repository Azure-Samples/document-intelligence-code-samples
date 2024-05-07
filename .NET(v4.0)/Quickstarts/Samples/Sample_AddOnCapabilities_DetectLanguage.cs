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
        /// Detect languages from a given file with the add-on languages capability
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task DetectLanguage(string? path, string? url)
        {
            if (string.IsNullOrWhiteSpace(path) && string.IsNullOrWhiteSpace(url))
            {
                // local sample file
                path = $"{Environment.CurrentDirectory}\\Assets\\invoice_sample.jpg";
                /* If want to use the online sample file, just comment out the variable "path" and uncomment variable "url".
                 * If use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
                 * If analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
                 */

                // sample file online
                // url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/invoice_sample.jpg";
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

            // Specify DocumentAnalysisFeature.Languages as the analysis features
            var features = new List<DocumentAnalysisFeature> { DocumentAnalysisFeature.Languages };

            PromptRequestingDocumentIntelligenceService();
            var operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-layout", content, features: features);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            // Detect languages:
            Console.WriteLine("----Languages detected in the document----");
            Console.WriteLine($"Detected {result.Languages.Count} languages:");

            for (int i = 0; i < result.Languages.Count; i++)
            {
                var lang = result.Languages[i];
                Console.WriteLine($"- Language #{i}: locale '{lang.Locale}'");
                Console.WriteLine($"  Confidence: {lang.Confidence}");

                var contents = lang.Spans.Select(s => result.Content.Substring(s.Offset, s.Length));
                Console.WriteLine($"  Text: '{string.Join(",", contents)}'");
            }
        }
    }
}
