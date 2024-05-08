// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------

using Azure;
using Azure.AI.DocumentIntelligence;
using ConsoleTables;

namespace Quickstarts
{
    internal partial class Samples
    {
        /// <summary>
        /// Extract page lines, paragraphs, styles, table structures from a given document
        /// </summary>
        /// <param name="path"> the file path to analyze in local </param>
        /// <param name="url"> the file url expect to analyze online </param>
        public async Task ExtractLayoutAsync(string? path, string? url)
        {
            if (string.IsNullOrWhiteSpace(path) && string.IsNullOrWhiteSpace(url))
            {
                // local sample file
                path = $"{Environment.CurrentDirectory}\\Assets\\layout-pageobject.pdf";
                /* If want to use the online sample file, just comment out the variable "path" and uncomment variable "url".
                 * If use the URL of a public website, to find more URLs, please visit: https://aka.ms/more-URLs 
                 * If analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
                 */

                // sample file online
                // url = "https://documentintelligence.ai.azure.com/documents/samples/layout/layout-pageobject.pdf";
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
            Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-layout", content);
            AnalyzeResult result = operation.Value;
            PromptGettingResponseFromDocumentIntelligenceService();

            // Extract page lines:
            foreach (DocumentPage page in result.Pages)
            {
                Console.WriteLine($"Document Page {page.PageNumber} has {page.Lines.Count} line(s), {page.Words.Count} word(s)," +
                    $" and {page.SelectionMarks.Count} selection mark(s).");

                for (int i = 0; i < page.Lines.Count; i++)
                {
                    DocumentLine line = page.Lines[i];

                    Console.WriteLine($"  Line {i}:");
                    Console.WriteLine($"    Content: '{line.Content}'");

                    Console.Write("    Bounding polygon, with points ordered clockwise:");
                    for (int j = 0; j < line.Polygon.Count; j += 2)
                    {
                        Console.Write($" ({line.Polygon[j]}, {line.Polygon[j + 1]})");
                    }

                    Console.WriteLine();
                }

                for (int i = 0; i < page.SelectionMarks.Count; i++)
                {
                    DocumentSelectionMark selectionMark = page.SelectionMarks[i];

                    Console.WriteLine($"  Selection Mark {i} is {selectionMark.State}.");
                    Console.WriteLine($"    State: {selectionMark.State}");

                    Console.Write("    Bounding polygon, with points ordered clockwise:");
                    for (int j = 0; j < selectionMark.Polygon.Count - 1; j++)
                    {
                        Console.Write($" ({selectionMark.Polygon[j]}, {selectionMark.Polygon[j + 1]})");
                    }

                    Console.WriteLine();
                }
            }

            // Extract paragraph:
            for (int i = 0; i < result.Paragraphs.Count; i++)
            {
                DocumentParagraph paragraph = result.Paragraphs[i];

                Console.WriteLine($"Paragraph {i}:");
                Console.WriteLine($"  Content: {paragraph.Content}");

                if (paragraph.Role != null)
                {
                    Console.WriteLine($"  Role: {paragraph.Role}");
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
                        var handwrittenContent = result.Content.Substring(span.Offset, span.Length);
                        Console.WriteLine($"  {handwrittenContent}");
                    }
                }
            }

            // Extract table cells:
            for (int i = 0; i < result.Tables.Count; i++)
            {
                DocumentTable table = result.Tables[i];
                Console.WriteLine($"Table {i} has {table.RowCount} rows and {table.ColumnCount} columns.");

                PrintPrettyTable(table.Cells);
            }

            // Extract figures:
            if (result.Figures.Count > 0)
            {
                var figureContent = "";
                Console.WriteLine($"Document has {result.Figures.Count} figures: ");
                foreach (var figure in result.Figures)
                {
                    for (var i = 0; i < figure.Spans.Count; i++)
                    {
                        var spanOffset = figure.Spans[i].Offset;
                        var spanLength = figure.Spans[i].Length;
                        Console.WriteLine($"Span #{i} Offset: {spanOffset}, Length: {spanLength}");

                        figureContent += result.Content.Substring(spanOffset, spanLength);
                    }

                    Console.WriteLine($"Original figure content: {figureContent}");

                    if (figure.Caption != null)
                    {
                        Console.WriteLine($"\tCaption: {figure.Caption.Content}");
                        foreach (var captionRegion in figure.Caption.BoundingRegions)
                        {
                            (float x_left, float y_top, float x_right, float y_bottom) = captionRegion.CoordinateBoundary();
                            Console.WriteLine($"\tCaption bounding box in ({x_left}, {y_top}, {x_right}, {y_bottom})");
                        }
                    }

                    foreach (var figureRegion in figure.BoundingRegions)
                    {
                        (float x_left, float y_top, float x_right, float y_bottom) = figureRegion.CoordinateBoundary();
                        Console.WriteLine($"\tFigure body bounding box in ({x_left}, {y_top}, {x_right}, {y_bottom})");
                    }
                }
            }

            // Next steps:
            // Learn more about Layout model: https://aka.ms/di-layout
            // Find more sample code: https://aka.ms/doc-intelligence-samples
        }

        private static void PrintPrettyTable(IEnumerable<DocumentTableCell> cells)
        {
            var columnNameList = new List<string>();
            var cellsInRow = new List<string>();
            var allCellsByRow = new List<List<string>>();
            int lastRowIndex = -1;

            foreach (DocumentTableCell cell in cells)
            {
                if (cell.RowIndex == 0 && cell.Kind == "columnHeader")
                {
                    columnNameList.Add(cell.Content);
                }
                else
                {
                    if (cell.RowIndex == lastRowIndex)
                    {
                        cellsInRow.Add(cell.Content);
                    }
                    else
                    {
                        if (lastRowIndex != -1)
                        {
                            allCellsByRow.Add(new List<string>(cellsInRow));
                        }
                        cellsInRow = [cell.Content];
                        lastRowIndex = cell.RowIndex;
                    }
                }
            }
            allCellsByRow.Add(new List<string>(cellsInRow));

            var consoleTable = new ConsoleTable([.. columnNameList]);
            allCellsByRow.ForEach(row =>
            {
                consoleTable.AddRow([.. row]);
            });
            consoleTable.Write();
        }
    }
}
