# Document Intelligence US tax form 1040 Schedule `EIC` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleEIC**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleEIC.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`SeparatedAndMeetingEicClaimReqsCheckbox`|`boolean`|Separated And Meeting Eic Claim Reqs Checkbox extracted from Form 1040-ScheduleEIC.|:selected:|
|`QualifyingChildInformation`|`array`|Qualifying Child information extracted from Form 1040-ScheduleEIC||
|`QualifyingChildInformation.*`|`object`|||
|`QualifyingChildInformation.*.Name`|`string`|Name extracted from Form 1040-ScheduleEIC.|Pascale Weyderth|
|`QualifyingChildInformation.*.SSN`|`string`|S S N extracted from Form 1040-ScheduleEIC.|123-45-6789|
|`QualifyingChildInformation.*.BirthYear`|`string`|Birth Year extracted from Form 1040-ScheduleEIC.|2010|
|`QualifyingChildInformation.*.Under24`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`QualifyingChildInformation.*.PermanentlyDisabled`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`QualifyingChildInformation.*.RelationshipToTaxpayer`|`string`|Relationship To Taxpayer extracted from Form 1040-ScheduleEIC.|Niece|
|`QualifyingChildInformation.*.NumberOfMonthsLivedWithTaxPayer`|`number`|Number Of Months Lived With Tax Payer extracted from Form 1040-ScheduleEIC.|123456|