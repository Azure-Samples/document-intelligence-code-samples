# Document Intelligence US tax form 1040 Schedule `B` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleB**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleB.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`Box2`|`number`|Box 2 extracted from Form 1040-ScheduleB.|123456|
|`Box3`|`number`|Box 3 extracted from Form 1040-ScheduleB.|123456|
|`Box4`|`number`|Box 4 extracted from Form 1040-ScheduleB.|123456|
|`Box6`|`number`|Box 6 extracted from Form 1040-ScheduleB.|123456|
|`Box7a`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box7FileF114Required`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box7b`|`string`|Box 7b extracted from Form 1040-ScheduleB.|United Kingdom|
|`Box8`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box1`|`array`|List of interest payers and equivalent amounts extracted from Form 1040-ScheduleB||
|`Box1.*`|`object`|||
|`Box1.*.PayerDetails`|`string`|Payer Details extracted from Form 1040-ScheduleB.|Contoso Bank|
|`Box1.*.Amount`|`number`|Amount extracted from Form 1040-ScheduleB.|123456|
|`Box5`|`array`|List of dividend payers and equivalent amounts extracted from Form 1040-ScheduleB||
|`Box5.*`|`object`|||
|`Box5.*.PayerDetails`|`string`|Payer Details extracted from Form 1040-ScheduleB.|Contoso Bank|
|`Box5.*.Amount`|`number`|Amount extracted from Form 1040-ScheduleB.|123456|