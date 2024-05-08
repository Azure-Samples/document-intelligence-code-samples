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
        /// Extract barcodes from a given file with the add-on barcodes capability
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task ExtractBarcodeProperty(string? path, string? url)
        {
            if (string.IsNullOrWhiteSpace(path) && string.IsNullOrWhiteSpace(url))
            {
                // local sample file
                path = $"{Environment.CurrentDirectory}\\Assets\\read-barcode.pdf";
                /* If want to use the online sample file, just comment out the variable "path" and uncomment variable "url".
                 * If use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
                 * If analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
                 */

                // sample file online
                // url = "https://documentintelligence.ai.azure.com/documents/samples/read/read-barcode.pdf";
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

            // Specify DocumentAnalysisFeature.Barcodes as the analysis features
            var features = new List<DocumentAnalysisFeature> { DocumentAnalysisFeature.Barcodes };

            PromptRequestingDocumentIntelligenceService();
            var operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-layout", content, features: features);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            foreach (DocumentPage page in result.Pages)
            {
                Console.WriteLine($"----Barcodes detected from page #{page.PageNumber}----");
                Console.WriteLine($"Detected {page.Barcodes.Count} barcodes:");

                // Extract the barcodes:
                for (int i = 0; i < page.Barcodes.Count; i++)
                {
                    DocumentBarcode barcode = page.Barcodes[i];

                    Console.WriteLine($"- Barcode #{i}: {barcode.Value}");
                    Console.WriteLine($"  Kind: {barcode.Kind}");
                    Console.WriteLine($"  Confidence: {barcode.Confidence}");
                    Console.WriteLine($"  bounding polygon (points ordered clockwise):");

                    for (int j = 0; j < barcode.Polygon.Count; j += 2)
                    {
                        Console.WriteLine($"      Point {j / 2} => X: {barcode.Polygon[j]}, Y: {barcode.Polygon[j + 1]}");
                    }
                }
            }
        }
    }
}
