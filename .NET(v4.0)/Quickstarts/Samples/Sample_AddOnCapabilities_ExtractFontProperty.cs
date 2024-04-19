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
        /// Extract font information from a given file with the add-on font styling capability
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task ExtractFontProperty(string? path, string? url)
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

            // Specify DocumentAnalysisFeature.FontStyling as the analysis features.
            var features = new List<DocumentAnalysisFeature> { DocumentAnalysisFeature.StyleFont };

            PromptRequestingDocumentIntelligenceService();
            var operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-layout", content, features: features);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            // Handwritten styles
            var handwrittenSpans = result.Styles
                .Where(s => s.IsHandwritten != null && s.IsHandwritten.Value)
                .SelectMany(s => s.Spans).OrderBy(s => s.Offset);
            if (handwrittenSpans.Any())
            {
                Console.WriteLine("----Handwritten content----");
                var handwrittenContents = handwrittenSpans.Select(s => result.Content.Substring(s.Offset, s.Length));
                Console.WriteLine(string.Join(",", handwrittenContents));
            }
            else
            {
                Console.WriteLine("No handwritten content was detected.");
            }

            // DocumentStyle has the following font related attributes:
            var similarFontFamilies = new Dictionary<string, List<DocumentStyle>>(); // e.g., 'Arial, sans-serif
            var fontStyles = new Dictionary<DocumentFontStyle, List<DocumentStyle>>(); // e.g, 'italic'
            var fontWeights = new Dictionary<DocumentFontWeight, List<DocumentStyle>>(); // e.g., 'bold'
            var fontColors = new Dictionary<string, List<DocumentStyle>>(); // in '#rrggbb' hexadecimal format
            var fontBackgroundColors = new Dictionary<string, List<DocumentStyle>>(); // in '#rrggbb' hexadecimal format

            Console.WriteLine("\n----Fonts styles detected in the document----");

            // Iterate over the styles and group them by their font attributes.
            foreach (var style in result.Styles)
            {
                if (!string.IsNullOrEmpty(style.SimilarFontFamily))
                {
                    if (similarFontFamilies.ContainsKey(style.SimilarFontFamily))
                    {
                        similarFontFamilies[style.SimilarFontFamily].Add(style);
                    }
                    else
                    {
                        similarFontFamilies.Add(style.SimilarFontFamily, [style]);
                    }
                }
                if (style.FontStyle != null)
                {
                    if (fontStyles.ContainsKey(style.FontStyle.Value))
                    {
                        fontStyles[style.FontStyle.Value].Add(style);
                    }
                    else
                    {
                        fontStyles.Add(style.FontStyle.Value, [style]);
                    }
                }
                if (style.FontWeight != null)
                {
                    if (fontWeights.ContainsKey(style.FontWeight.Value))
                    {
                        fontWeights[style.FontWeight.Value].Add(style);
                    }
                    else
                    {
                        fontWeights.Add(style.FontWeight.Value, [style]);
                    }
                }
                if (!string.IsNullOrEmpty(style.Color))
                {
                    if (fontColors.ContainsKey(style.Color))
                    {
                        fontColors[style.Color].Add(style);
                    }
                    else
                    {
                        fontColors.Add(style.Color, [style]);
                    }
                }
                if (!string.IsNullOrEmpty(style.BackgroundColor))
                {
                    if (fontBackgroundColors.ContainsKey(style.BackgroundColor))
                    {
                        fontBackgroundColors[style.BackgroundColor].Add(style);
                    }
                    else
                    {
                        fontBackgroundColors.Add(style.BackgroundColor, [style]);
                    }
                }
            }

            Console.WriteLine($"Detected {similarFontFamilies.Count} font families:");
            foreach (var family in similarFontFamilies)
            {
                var spans = family.Value.SelectMany(s => s.Spans).OrderBy(s => s.Offset);
                var styleContents = spans.Select(s => result.Content.Substring(s.Offset, s.Length));

                Console.WriteLine($"- Font family: '{family.Key}'");
                Console.WriteLine($"  Text: '{string.Join(",", styleContents)}'");
            }

            Console.WriteLine($"\nDetected {fontStyles.Count} font styles:");
            foreach (var style in fontStyles)
            {
                var spans = style.Value.SelectMany(s => s.Spans).OrderBy(s => s.Offset);
                var styleContents = spans.Select(s => result.Content.Substring(s.Offset, s.Length));

                Console.WriteLine($"- Font style: '{style.Key}'");
                Console.WriteLine($"  Text: '{string.Join(",", styleContents)}'");
            }

            Console.WriteLine($"\nDetected {fontWeights.Count} font weights:");
            foreach (var weight in fontWeights)
            {
                var spans = weight.Value.SelectMany(s => s.Spans).OrderBy(s => s.Offset);
                var styleContents = spans.Select(s => result.Content.Substring(s.Offset, s.Length));

                Console.WriteLine($"- Font weight: '{weight.Key}'");
                Console.WriteLine($"  Text: '{string.Join(",", styleContents)}'");
            }

            Console.WriteLine($"\nDetected {fontColors.Count} font colors:");
            foreach (var color in fontColors)
            {
                var spans = color.Value.SelectMany(s => s.Spans).OrderBy(s => s.Offset);
                var styleContents = spans.Select(s => result.Content.Substring(s.Offset, s.Length));

                Console.WriteLine($"- Font color: '{color.Key}'");
                Console.WriteLine($"  Text: '{string.Join(",", styleContents)}'");
            }

            Console.WriteLine($"\nDetected {fontBackgroundColors.Count} font background colors:");
            foreach (var backGroundColor in fontBackgroundColors)
            {
                var spans = backGroundColor.Value.SelectMany(s => s.Spans).OrderBy(s => s.Offset);
                var styleContents = spans.Select(s => result.Content.Substring(s.Offset, s.Length));

                Console.WriteLine($"- Font background color: '{backGroundColor.Key}'");
                Console.WriteLine($"  Text: '{string.Join(",", styleContents)}'");
            }
        }
    }
}
