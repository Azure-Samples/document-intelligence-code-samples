// #define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
#if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

/*
  This code sample shows Prebuilt ID Document operations with the Azure AI Document Intelligence client library.

  To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
  https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-csharp
*/

using Azure;
using Azure.AI.DocumentIntelligence;

/*
  Remember to remove the key from your code when you're done, and never post it publicly. For production, use
  secure methods to store and access your credentials. For more information, see 
  https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
*/

string endpoint = Environment.GetEnvironmentVariable("DOCUMENTINTELLIGENCE_ENDPOINT") ?? string.Empty;
string key = Environment.GetEnvironmentVariable("DOCUMENTINTELLIGENCE_API_KEY") ?? string.Empty;
if (string.IsNullOrEmpty(endpoint) || string.IsNullOrEmpty(key))
{
    Console.WriteLine("Please set the environment variables for the endpoint and key.");
    return;
}

AzureKeyCredential credential = new AzureKeyCredential(key);
DocumentIntelligenceClient client = new DocumentIntelligenceClient(new Uri(endpoint), credential);

// sample document
Uri idDocumentUri = new Uri("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/DriverLicense.png");

Operation<AnalyzeResult> operation = await client.AnalyzeDocumentAsync(WaitUntil.Completed, "prebuilt-idDocument", idDocumentUri);

AnalyzeResult identityDocuments = operation.Value;

// To see the list of all the supported fields returned by service and its corresponding types, consult:
// https://aka.ms/formrecognizer/iddocumentfields

AnalyzedDocument identityDocument = identityDocuments.Documents.Single();

if (identityDocument.Fields.TryGetValue("Address", out DocumentField addressField))
{
    if (addressField.FieldType == DocumentFieldType.Address)
    {
        Console.WriteLine($"Address: '{addressField.Content}', with confidence {addressField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("CountryRegion", out DocumentField countryRegionField))
{
    if (countryRegionField.FieldType == DocumentFieldType.CountryRegion)
    {
        string countryRegion = countryRegionField.ValueCountryRegion;
        Console.WriteLine($"CountryRegion: '{countryRegion}', with confidence {countryRegionField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("DateOfBirth", out DocumentField dateOfBirthField))
{
    if (dateOfBirthField.FieldType == DocumentFieldType.Date)
    {
        DateTimeOffset? dateOfBirth = dateOfBirthField.ValueDate;
        Console.WriteLine($"Date Of Birth: '{dateOfBirth}', with confidence {dateOfBirthField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("DateOfExpiration", out DocumentField dateOfExpirationField))
{
    if (dateOfExpirationField.FieldType == DocumentFieldType.Date)
    {
        DateTimeOffset? dateOfExpiration = dateOfExpirationField.ValueDate;
        Console.WriteLine($"Date Of Expiration: '{dateOfExpiration}', with confidence {dateOfExpirationField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("DocumentNumber", out DocumentField documentNumberField))
{
    if (documentNumberField.FieldType == DocumentFieldType.String)
    {
        string documentNumber = documentNumberField.ValueString;
        Console.WriteLine($"Document Number: '{documentNumber}', with confidence {documentNumberField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("FirstName", out DocumentField firstNameField))
{
    if (firstNameField.FieldType == DocumentFieldType.String)
    {
        string firstName = firstNameField.ValueString;
        Console.WriteLine($"First Name: '{firstName}', with confidence {firstNameField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("LastName", out DocumentField lastNameField))
{
    if (lastNameField.FieldType == DocumentFieldType.String)
    {
        string lastName = lastNameField.ValueString;
        Console.WriteLine($"Last Name: '{lastName}', with confidence {lastNameField.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("Region", out DocumentField regionfield))
{
    if (regionfield.FieldType == DocumentFieldType.String)
    {
        string region = regionfield.ValueString;
        Console.WriteLine($"Region: '{region}', with confidence {regionfield.Confidence}");
    }
}

if (identityDocument.Fields.TryGetValue("Sex", out DocumentField sexfield))
{
    if (sexfield.FieldType == DocumentFieldType.String)
    {
        string sex = sexfield.ValueString;
        Console.WriteLine($"Sex: '{sex}', with confidence {sexfield.Confidence}");
    }
}

#endif
