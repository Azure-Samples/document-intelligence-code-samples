# Document Intelligence ID document model

## 2024-11-30 (GA)

### Supported document types

| Region | Document Types |

|--------|----------------|
|Worldwide|Passport Book, Passport Card|
|United States|Driver License, Identification Card, Residency Permit (Green card), Social Security Card, Military ID|
|North America|Driver License, Identification Card, Residency Permit|
|South America|Driver License, Identification Card, Residency Permit|
|Europe|Driver License, Identification Card, Residency Permit|
|Southeast Asia|Driver License, Identification Card, Residency Permit|
|India|Driver License, PAN Card, Aadhaar Card|
|Australia|Driver License, Photo Card, Key-pass ID (including digital version)|
|New Zealand|Driver License, Identification Card, Residency Permit|


### Model ID

**prebuilt-idDocument**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`CountryRegion`|`countryRegion`|Country or region code|USA|
|`Region`|`string`|State or province|Washington|
|`DocumentNumber`|`string`|Driver license number|WDLABCD456DG|
|`DocumentDiscriminator`|`string`|Driver license document discriminator|12645646464554646456464544|
|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
|`LastName`|`string`|Surname|TALBOT|
|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
|`DateOfBirth`|`date`|Date of birth|01/06/1958|
|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
|`DateOfIssue`|`date`|Date of issue|08/12/2012|
|`EyeColor`|`string`|Eye color|BLU|
|`HairColor`|`string`|Hair color|BRO|
|`Height`|`string`|Height|5'11"|
|`Weight`|`string`|Weight|185LB|
|`Sex`|`string`|Sex|M|
|`Endorsements`|`string`|Endorsements|L|
|`Restrictions`|`string`|Restrictions|B|
|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|
|`VehicleClassifications`|`string`|Vehicle classification|D|

#### idDocument.passport

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`DocumentNumber`|`string`|Passport number|340020013|
|`FirstName`|`string`|Given name and middle initial if applicable|JENNIFER|
|`MiddleName`|`string`|Name between given name and surname|REYES|
|`LastName`|`string`|Surname|BROOKS|
|`Aliases`|`array`|||
|`Aliases.*`|`string`|Also known as|MAY LIN|
|`DateOfBirth`|`date`|Date of birth|1980-01-01|
|`DateOfExpiration`|`date`|Date of expiration|2019-05-05|
|`DateOfIssue`|`date`|Date of issue|2014-05-06|
|`Sex`|`string`|Sex|F|
|`CountryRegion`|`countryRegion`|Issuing country or organization|USA|
|`DocumentType`|`string`|Document type|P|
|`Nationality`|`countryRegion`|Nationality|USA|
|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|
|`PlaceOfIssue`|`string`|Place of issue|LA PAZ|
|`IssuingAuthority`|`string`|Issuing authority|United States Department of State|
|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
|`MachineReadableZone`|`object`|Machine readable zone (MRZ)|P<USABROOKS<<JENNIFER<<<<<<<<<<<<<<<<<<<<<<< 3400200135USA8001014F1905054710000307<715816|
|`MachineReadableZone.FirstName`|`string`|Given name and middle initial if applicable|JENNIFER|
|`MachineReadableZone.LastName`|`string`|Surname|BROOKS|
|`MachineReadableZone.DocumentNumber`|`string`|Passport number|340020013|
|`MachineReadableZone.CountryRegion`|`countryRegion`|Issuing country or organization|USA|
|`MachineReadableZone.Nationality`|`countryRegion`|Nationality|USA|
|`MachineReadableZone.DateOfBirth`|`date`|Date of birth|1980-01-01|
|`MachineReadableZone.DateOfExpiration`|`date`|Date of expiration|2019-05-05|
|`MachineReadableZone.Sex`|`string`|Sex|F|

#### idDocument.nationalIdentityCard

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`CountryRegion`|`countryRegion`|Country or region code|USA|
|`Region`|`string`|State or province|Washington|
|`DocumentNumber`|`string`|National identity card number|WDLABCD456DG|
|`DocumentDiscriminator`|`string`|National identity card document discriminator|12645646464554646456464544|
|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
|`LastName`|`string`|Surname|TALBOT|
|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
|`DateOfBirth`|`date`|Date of birth|01/06/1958|
|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
|`DateOfIssue`|`date`|Date of issue|08/12/2012|
|`EyeColor`|`string`|Eye color|BLU|
|`HairColor`|`string`|Hair color|BRO|
|`Height`|`string`|Height|5'11"|
|`Weight`|`string`|Weight|185LB|
|`Sex`|`string`|Sex|M|
|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|


#### idDocument.residencePermit

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`CountryRegion`|`countryRegion`|Country or region code|USA|
|`DocumentNumber`|`string`|Residence permit number|WDLABCD456DG|
|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
|`LastName`|`string`|Surname|TALBOT|
|`DateOfBirth`|`date`|Date of birth|01/06/1958|
|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
|`DateOfIssue`|`date`|Date of issue|08/12/2012|
|`Sex`|`string`|Sex|M|
|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
|`PlaceOfBirth`|`string`|Place of birth|Germany|
|`Category`|`string`|Permit category|DV2|
|`Address`|`string`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|

#### idDocument.usSocialSecurityCard

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`DocumentNumber`|`string`|Social security card number|WDLABCD456DG|
|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
|`LastName`|`string`|Surname|TALBOT|
|`DateOfIssue`|`date`|Date of issue|08/12/2012|

#### idDocument

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
|`DocumentNumber`|`string`|Identity document number|WDLABCD456DG|
|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
|`LastName`|`string`|Surname|TALBOT|
|`DateOfBirth`|`date`|Date of birth|01/06/1958|
|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
