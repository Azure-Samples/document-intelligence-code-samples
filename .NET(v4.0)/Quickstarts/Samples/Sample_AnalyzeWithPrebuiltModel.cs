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
        /// Analyze data from certain types of common documents with prebuilt models, using a tax as an example.
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task AnalyzeWithPrebuiltModel(string? path, string? url)
        {
            if (string.IsNullOrWhiteSpace(path) && string.IsNullOrWhiteSpace(url))
            {
                // local sample file
                path = $"{Environment.CurrentDirectory}\\Assets\\w2-single.png";
                /* If want to use the online sample file, just comment out the variable "path" and uncomment variable "url".
                 * If use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
                 * If analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
                 */

                // sample file online
                // url = "https://documentintelligence.ai.azure.com/documents/samples/prebuilt/w2-single.png";
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

            PromptRequestingDocumentIntelligenceService();

            // To see the list of all the supported fields returned by service and its corresponding types for each supported model,
            // access https://aka.ms/di-prebuilt please.
            Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-tax.us.w2", content);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            // Extract DocumentField: 
            for (int i = 0; i < result.Documents.Count; i++)
            {
                Console.WriteLine($"Document {i}:");

                AnalyzedDocument document = result.Documents[i];

                foreach (var item in document.Fields)
                {
                    Utils.ExtractValueFromDocumentField(item.Key, item.Value);
                }
            }
        }
    }
}
