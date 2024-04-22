// coding: utf - 8 
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------

using ConsoleTables;
using System.Configuration;
using System.Diagnostics;

namespace Quickstarts
{
    internal class Program
    {
        const string GNU_PARAM_SYMBOL = " --";
        static readonly ConsoleTable helpTable = new(["FunctionName", "Description"]);
        static readonly List<(string, string)> sampleFunctionList = [
            ("ExtractLayoutAsync", "Sample - Extract the layout of a document"),
            ("AnalyzeWithPrebuiltModel", "Sample - Analyze a document with a prebuilt model"),
            ("ExtractHighResolution", "Sample - Add-on : High resolution extraction"),
            ("ExtractFormula", "Sample - Add-on : Formula extraction"),
            ("ExtractFontProperty", "Sample - Add-on : Font property extraction"),
            ("ExtractBarcodeProperty", "Sample - Add-on : Barcode property extraction"),
            ("ExtractKeyValuePairs", "Sample - Add-on : Key-value pairs extraction"),
            ("DetectLanguage", "Sample - Add-on : Language detection")];

        /// <summary>
        /// Here is the entrance for the Azure Document Intelligence client SDK Samples.
        /// </summary>
        /// <returns></returns>
        static async Task Main()
        {
            Console.WriteLine("Hello, welcome to the Azure Document Intelligence client SDK Sample Codes for .Net!");

            // Read the Azure Document Intelligence endpoint and apikey from app.config.
            // For how to obtain the endpoint and apikey, please see Prerequisites in README.md .
            var docIntelligenceEndPoint = ConfigurationManager.AppSettings["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"];
            var docIntelligenceApiKey = ConfigurationManager.AppSettings["AZURE_DOCUMENT_INTELLIGENCE_KEY"];
            if (string.IsNullOrWhiteSpace(docIntelligenceEndPoint) || string.IsNullOrWhiteSpace(docIntelligenceApiKey))
            {
                var exceptionStr = "Missing the Azure Document Intelligence EndPoint and ApiKey.";
                Console.WriteLine(exceptionStr);
                Console.WriteLine("Press the 'Enter' for getting help.");
                Console.ReadLine();
                Process.Start(new ProcessStartInfo("https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-csharp#prerequisites") { UseShellExecute = true });
                throw new ArgumentException(exceptionStr);
            }

            Type sampleType = typeof(Samples);
            var sampleInstance = new Samples(docIntelligenceEndPoint!, docIntelligenceApiKey!);

            sampleFunctionList.ForEach(f =>
            {
                (string funcName, string description) = f;
                helpTable.AddRow(funcName, description);
            });
            PrintHelpInfo();

            bool running = true;
            while (running)
            {
                Console.WriteLine("Please input the command which you want to execute:");
                string? commandStr = Console.ReadLine();
                if (!string.IsNullOrWhiteSpace(commandStr))
                {
                    switch (commandStr.ToLower())
                    {
                        case "help": PrintHelpInfo(); break;
                        case "cls": Console.Clear(); break;
                        case "quit":
                        case "exit": running = false; break;
                        default:
                            var commandArr = commandStr.Split(GNU_PARAM_SYMBOL);
                            if (commandArr.Length >= 1)
                            {
                                var funcName = commandArr[0];
                                var methodInfo = sampleType.GetMethod(funcName);
                                if (methodInfo != null)
                                {
                                    Console.WriteLine();
                                    Utils.ConsoleImportantWriteLine($"Running function: {commandStr}");

                                    object? taskResult = null;
                                    if (commandArr.Length > 1)
                                    {
                                        var paramKVP = commandArr[1].Split(" ");
                                        var paramName = paramKVP[0].ToLower();
                                        var paramValue = paramKVP[1].Trim('"').Trim('\'');
                                        if (paramName == "path")
                                        {
                                            taskResult = methodInfo.Invoke(sampleInstance, [paramValue, ""]);
                                        }
                                        else if (paramName == "url")
                                        {
                                            taskResult = methodInfo.Invoke(sampleInstance, ["", paramValue]);
                                        }
                                        else
                                        {
                                            Console.WriteLine("No corresponding parameter, please check it!");
                                            PrintHelpInfo();
                                        }
                                    }
                                    else
                                    {
                                        taskResult = methodInfo.Invoke(sampleInstance, ["", ""]);
                                    }

                                    if (taskResult != null)
                                    {
                                        await (Task)taskResult;
                                    }
                                }
                                else
                                {
                                    Console.WriteLine("The syntax format is incorrect, please check it!");
                                    PrintHelpInfo();
                                }
                            }
                            else
                            {
                                Console.WriteLine("No such function");
                                PrintHelpInfo();
                            }
                            break;
                    }
                }
            }

            Console.WriteLine("Program Exited.");
        }

        /// <summary>
        /// Print the sample command list and help information.
        /// </summary>
        static void PrintHelpInfo()
        {
            Console.WriteLine("Here're the demo functions:");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("--------------------------------------------------------------------------------");
            helpTable.Write(Format.Minimal);
            Console.WriteLine("--------------------------------------------------------------------------------");
            Console.ResetColor();
            Console.WriteLine("If you want to run the demo function with the sample test data, just input the function name directly.");
            Console.WriteLine("e.g.");
            Utils.ConsoleImportantWriteLine("ExtractLayoutAsync");
            Console.WriteLine();
            Console.WriteLine("If you want to execute the function with your customized data, input the function name with the parameter by GNU style, as below:");
            Utils.ConsoleImportantWriteLine("--path    the file path to analyze in you local file system.");
            Utils.ConsoleImportantWriteLine("--url     the file url which you expect to analyze online.");
            Console.WriteLine("e.g.");
            Utils.ConsoleImportantWriteLine("ExtractLayoutAsync --path <The file path to analyze in you local file system>");
            Console.WriteLine("or");
            Utils.ConsoleImportantWriteLine("ExtractLayoutAsync --url <The file url which you expect to analyze online>");
            Console.WriteLine("--------------------------------------------------------------------------------");
            Console.WriteLine();
            Console.WriteLine("Here're the console commands:");
            Console.WriteLine("================================================================================");
            Utils.ConsoleImportantWriteLine("help          ------------ Print the command list");
            Utils.ConsoleImportantWriteLine("cls           ------------ Clear the console output");
            Utils.ConsoleImportantWriteLine("exit | quit   ------------ Exit program");
            Console.WriteLine("================================================================================");
        }
    }
}
