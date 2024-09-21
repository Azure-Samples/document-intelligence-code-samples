// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------
using Azure;
using Azure.AI.DocumentIntelligence;
using Azure.Identity;
using Utility;

namespace AuthenticateWithServicePrincipal
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            #region To obtain these parameters, please reference the document in (..\..\Doc\Prerequisites For Authentication With Service Principal.md)
            // the endpoint to your Document Intelligence resource.
            var docIntelligenceEndpoint = "<Azure Document Intelligence Endpoint>";
            // your Azure tenant id.
            var tenantId = "<Azure Tenant Id>";
            // the Client Secrets of Microsoft Entra App.
            var clientId = "<Id of Azure Entra App>";
            // the Client Secrets of Microsoft Entra App.
            var clientSecret = "<Secret of Azure Entra App>";
            #endregion

            var clientSecretCredential = new ClientSecretCredential(tenantId, clientId, clientSecret);
            var client = new DocumentIntelligenceClient(new Uri(docIntelligenceEndpoint), clientSecretCredential);

            // sample file online
            var url = "https://documentintelligence.ai.azure.com/documents/samples/prebuilt/w2-single.png";
            var content = new AnalyzeDocumentContent
            {
                UrlSource = new Uri(url)
            };

            // To see the list of all the supported fields returned by service and its corresponding types for each supported model,
            // access https://aka.ms/di-prebuilt please.
            Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-tax.us.w2", content);
            AnalyzeResult result = operation.Value;

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
