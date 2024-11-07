# Document Intelligence US tax form 1040 Schedule `H` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleH**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleH.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`PaidPreparer`|`object`|||
|`PaidPreparer.PreparerName`|`date`|Preparer name.|John Smith|
|`PaidPreparer.PreparerPTIN`|`string`|Preparer PIN.|123456|
|`PaidPreparer.IsPreparerSelfEmployed`|`boolean`|Is preparer self-employed|:selected:|
|`PaidPreparer.PreparerFirmName`|`string`|Taxpayer firm name.|Contoso LLC|
|`PaidPreparer.PreparerFirmPhoneNumber`|`phoneNumber`|Preparer's firm phone number|1-123-456-7890|
|`PaidPreparer.PreparerFirmAddress`|`address`|Prepare Firm Address.|123 First street, Seattle WA 98001|
|`PaidPreparer.PreparerFirmEIN`|`string`|Prepare Firm EIN.|98-7654321|
|`EIN`|`string`|E I N extracted from Form 1040-ScheduleH.|12-3456789|
|`BoxA`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxB`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxC`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box1a`|`number`|Box 1a extracted from Form 1040-ScheduleH.|123456|
|`Box1b`|`number`|Box 1b extracted from Form 1040-ScheduleH.|123456|
|`Box2a`|`number`|Box 2a extracted from Form 1040-ScheduleH.|123456|
|`Box2b`|`number`|Box 2b extracted from Form 1040-ScheduleH.|123456|
|`Box2c`|`number`|Box 2c extracted from Form 1040-ScheduleH.|123456|
|`Box3`|`number`|Box 3 extracted from Form 1040-ScheduleH.|123456|
|`Box4`|`number`|Box 4 extracted from Form 1040-ScheduleH.|123456|
|`Box5`|`number`|Box 5 extracted from Form 1040-ScheduleH.|123456|
|`Box6`|`number`|Box 6 extracted from Form 1040-ScheduleH.|123456|
|`Box7`|`number`|Box 7 extracted from Form 1040-ScheduleH.|123456|
|`Box8a`|`number`|Box 8a extracted from Form 1040-ScheduleH.|123456|
|`Box8b`|`number`|Box 8b extracted from Form 1040-ScheduleH.|123456|
|`Box8c`|`number`|Box 8c extracted from Form 1040-ScheduleH.|123456|
|`Box8d`|`number`|Box 8d extracted from Form 1040-ScheduleH.|123456|
|`Box8e`|`number`|Box 8e extracted from Form 1040-ScheduleH.|123456|
|`Box8f`|`number`|Box 8f extracted from Form 1040-ScheduleH.|123456|
|`Box8g`|`number`|Box 8g extracted from Form 1040-ScheduleH.|123456|
|`Box8h`|`number`|Box 8h extracted from Form 1040-ScheduleH.|123456|
|`Box8i`|`number`|Box 8i extracted from Form 1040-ScheduleH.|123456|
|`Box8j`|`number`|Box 8j extracted from Form 1040-ScheduleH.|123456|
|`Box8k`|`number`|Box 8k extracted from Form 1040-ScheduleH.|123456|
|`Box8l`|`number`|Box 8l extracted from Form 1040-ScheduleH.|123456|
|`Box8m`|`number`|Box 8m extracted from Form 1040-ScheduleH.|123456|
|`Box8n`|`number`|Box 8n extracted from Form 1040-ScheduleH.|123456|
|`Box9`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box10`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box11`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box12`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box13`|`string`|Box 13 extracted from Form 1040-ScheduleH.|Washington|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleH.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleH.|123456|
|`Box16`|`number`|Box 16 extracted from Form 1040-ScheduleH.|123456|
|`Box18g`|`number`|Box 18g extracted from Form 1040-ScheduleH.|123456|
|`Box18h`|`number`|Box 18h extracted from Form 1040-ScheduleH.|123456|
|`Box19`|`number`|Box 19 extracted from Form 1040-ScheduleH.|123456|
|`Box20a`|`number`|Box 20a extracted from Form 1040-ScheduleH.|123456|
|`Box20b`|`number`|Box 20b extracted from Form 1040-ScheduleH.|123456|
|`Box21`|`number`|Box 21 extracted from Form 1040-ScheduleH.|123456|
|`Box22`|`number`|Box 22 extracted from Form 1040-ScheduleH.|123456|
|`Box23Checkboxes`|`boolean`|Box23 Checkboxes extracted from Form 1040-ScheduleH.|:selected:|
|`Box23`|`number`|Box 23 extracted from Form 1040-ScheduleH.|123456|
|`Box24`|`number`|Box 24 extracted from Form 1040-ScheduleH.|123456|
|`Box25`|`number`|Box 25 extracted from Form 1040-ScheduleH.|123456|
|`Box26`|`number`|Box 26 extracted from Form 1040-ScheduleH.|123456|
|`Box27`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`TaxpayerAddress`|`address`|Taxpayer Address extracted from Form 1040-ScheduleH.|123 Microsoft Way, Redmond WA 98052|
|`Box17`|`array`|State Specific FUTA details extracted from Form 1040-ScheduleH||
|`Box17.*`|`object`|||
|`Box17.*.NameOfState`|`string`|Name Of State extracted from Form 1040-ScheduleH.|WA|
|`Box17.*.TaxableWage`|`number`|Taxable Wage extracted from Form 1040-ScheduleH.|123456|
|`Box17.*.StateExperienceRatePeriodFromDate`|`date`|State Experience Rate Period From Date extracted from Form 1040-ScheduleH.|2022-12-31|
|`Box17.*.StateExperienceRatePeriodToDate`|`date`|State Experience Rate Period To Date extracted from Form 1040-ScheduleH.|2022-12-31|
|`Box17.*.StateExperienceRate`|`number`|State Experience Rate extracted from Form 1040-ScheduleH.|123456|
|`Box17.*.BoxE`|`number`|Box E extracted from Form 1040-ScheduleH.|123456|
|`Box17.*.BoxF`|`number`|Box F extracted from Form 1040-ScheduleH.|123456|
|`Box17.*.BoxG`|`number`|Box G extracted from Form 1040-ScheduleH.|123456|
|`Box17.*.ContributionPaid`|`number`|Contribution Paid extracted from Form 1040-ScheduleH.|123456|