# Document Intelligence business card model

## 2023-07-31 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`), Australia (`en-AU`), Canada (`en-CA`), United Kingdom (`en-GB`), India (`en-IN`), Japan (`en-JP`)|
|Japanese|Japan (`ja-JP`)|

### Model ID

**prebuilt-businessCard**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`ContactNames`|`array`|||
|`ContactNames.*`|`object`|Contact name|Chris Smith|
|`ContactNames.*.FirstName`|`string`|First (given) name of contact|Chris|
|`ContactNames.*.LastName`|`string`|Last (family) name of contact|Smith|
|`CompanyNames`|`array`|||
|`CompanyNames.*`|`string`|Company name|CONTOSO|
|`JobTitles`|`array`|||
|`JobTitles.*`|`string`|Job title|Senior Researcher|
|`Departments`|`array`|||
|`Departments.*`|`string`|Department or organization|Cloud & AI Department|
|`Addresses`|`array`|||
|`Addresses.*`|`address`|Address|4001 1st Ave NE Redmond, WA 98052|
|`WorkPhones`|`array`|||
|`WorkPhones.*`|`phoneNumber`|Work phone number|+1 (987) 213-5674|
|`MobilePhones`|`array`|||
|`MobilePhones.*`|`phoneNumber`|Mobile phone number|+1 (987) 123-4567|
|`Faxes`|`array`|||
|`Faxes.*`|`phoneNumber`|Fax number|+1 (987) 312-6745|
|`OtherPhones`|`array`|||
|`OtherPhones.*`|`phoneNumber`|Other phone number|+1 (987) 213-5673|
|`Emails`|`array`|||
|`Emails.*`|`string`|Contact email|chris.smith@contoso.com|
|`Websites`|`array`|||
|`Websites.*`|`string`|Website|https://www.contoso.com|
