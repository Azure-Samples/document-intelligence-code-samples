# Document Intelligence contract model

## 2024-07-31-preview

#### Model ID

**prebuilt-contract**

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`Title`|`string`|Contract title|SERVICE AGREEMENT|
|`ContractId`|`string`|Contract identification code|AB12956|
|`Parties`|`array`|List of legal parties||
|`Parties.*`|`object`|Legal party||
|`Parties.*.Name`|`string`|Name of legal party|Contoso Corporation|
|`Parties.*.Address`|`address`|Address of legal party|1 Microsoft Way, Redmond, Washington, 98052|
|`Parties.*.ReferenceName`|`string`|Name used throughout the contract as reference to the legal party|Contoso|
|`Parties.*.Clause`|`string`|Full description of the party|Contoso Corporation ( Contoso ), a Washington corporation, having its principal place of business at 1 Microsoft Way, Redmond, Washington, 98052|
|`ExecutionDate`|`date`|Date when the agreement was fully signed and agreed upon by all parties|Twenty Third of February in the year Twenty Twenty Two|
|`EffectiveDate`|`date`|Date when the contract starts to be in effect|immediately|
|`ExpirationDate`|`date`|Date when the contract ends to be in effect|1 year|
|`ContractDuration`|`string`|Contract terms|5 years|
|`RenewalDate`|`date`|Date when the contract needs to be renewed by|Twenty Third of February in the year Twenty Twenty Two|
|`Jurisdictions`|`array`|List of jurisdictions||
|`Jurisdictions.*`|`object`|A location of the court agreed by both parties where any arising dispute out of or in connection with the agreement should be filed||
|`Jurisdictions.*.Clause`|`string`|Full description of the jurisdiction|This Agreement shall be governed by and construed in accordance with the internal laws of the State of Washington applicable to agreements made and to be performed entirely within such state.|
|`Jurisdictions.*.Region`|`string`|Court location|Washington|
