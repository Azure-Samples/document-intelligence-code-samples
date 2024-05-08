// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------
namespace Quickstarts
{
    internal partial class Samples(string docIntelligenceEndPoint, string docIntelligenceApiKey)
    {
        private readonly string docIntelligenceEndPoint = docIntelligenceEndPoint;
        private readonly string docIntelligenceApiKey = docIntelligenceApiKey;

        private static void PromptRequestingDocumentIntelligenceService()
        {
            Utils.ConsoleHighlightWriteLine("Requesting the Azure Document Intelligence service and waiting for the response...");
        }

        private static void PromptGettingResponseFromDocumentIntelligenceService()
        {
            Utils.ConsoleHighlightWriteLine("Get the response from Azure DocumentIntelligence service");
        }
    }
}
