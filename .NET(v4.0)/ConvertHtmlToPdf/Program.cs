// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------
using System.Diagnostics;
using System.Text;
using iText.Html2pdf;

// function to convert Html string to Pdf document
Action<string, string> ConvertHtmlToPdf = (string htmlString, string outputFilePath) =>
{
    using var htmlStream = new MemoryStream(Encoding.UTF8.GetBytes(htmlString));
    using var pdfFileStream = new FileStream(outputFilePath, FileMode.OpenOrCreate, FileAccess.Write);
    HtmlConverter.ConvertToPdf(htmlStream, pdfFileStream);
};

var baseDir = Environment.CurrentDirectory;
var htmlContent = File.ReadAllText($"{baseDir}\\HtmlFile\\web-page.html");
var pdfOutputFolder = $"{baseDir}\\Output";
if (!Directory.Exists(pdfOutputFolder))
{
    Directory.CreateDirectory(pdfOutputFolder);
}

var pdfOutputPath = $"{pdfOutputFolder}\\converted.pdf";
ConvertHtmlToPdf(htmlContent, pdfOutputPath);

Console.WriteLine($"Pdf convert successfully in {pdfOutputPath}");
Process.Start(new ProcessStartInfo(pdfOutputPath) { UseShellExecute = true });

