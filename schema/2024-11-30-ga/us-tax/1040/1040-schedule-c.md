# Document Intelligence US IRS 1040 Schedule `C` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleC**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleC.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`BoxA`|`string`|Box A extracted from Form 1040-ScheduleC.|Car wash|
|`BoxB`|`string`|Box B extracted from Form 1040-ScheduleC.|123456|
|`BoxC`|`string`|Box C extracted from Form 1040-ScheduleC.|Contoso Carwash LTD|
|`BoxD`|`string`|Box D extracted from Form 1040-ScheduleC.|12-3456789|
|`BoxE`|`address`|Box E extracted from Form 1040-ScheduleC.|123 Main street, Seattle WA 98001|
|`BoxF`|`selectionGroup`|Value will be a list containing at least one of the following: 'cash', 'accrual', 'other'.|cash :unselected: accrual :unselected: other :unselected:|
|`BoxFExtraInfo`|`string`|Box F Extra Info extracted from Form 1040-ScheduleC.|Credit|
|`BoxG`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxH`|`boolean`|Box H extracted from Form 1040-ScheduleC.|:selected:|
|`BoxI`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxJ`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box1Checkbox`|`number`|Box1 Checkbox extracted from Form 1040-ScheduleC.|123456|
|`Box1`|`number`|Box 1 extracted from Form 1040-ScheduleC.|123456|
|`Box2`|`number`|Box 2 extracted from Form 1040-ScheduleC.|123456|
|`Box3`|`number`|Box 3 extracted from Form 1040-ScheduleC.|123456|
|`Box4`|`number`|Box 4 extracted from Form 1040-ScheduleC.|123456|
|`Box5`|`number`|Box 5 extracted from Form 1040-ScheduleC.|123456|
|`Box6`|`number`|Box 6 extracted from Form 1040-ScheduleC.|123456|
|`Box7`|`number`|Box 7 extracted from Form 1040-ScheduleC.|123456|
|`Box8`|`number`|Box 8 extracted from Form 1040-ScheduleC.|123456|
|`Box9`|`number`|Box 9 extracted from Form 1040-ScheduleC.|123456|
|`Box10`|`number`|Box 10 extracted from Form 1040-ScheduleC.|123456|
|`Box11`|`number`|Box 11 extracted from Form 1040-ScheduleC.|123456|
|`Box12`|`number`|Box 12 extracted from Form 1040-ScheduleC.|123456|
|`Box13`|`number`|Box 13 extracted from Form 1040-ScheduleC.|123456|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleC.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleC.|123456|
|`Box16a`|`number`|Box 16a extracted from Form 1040-ScheduleC.|123456|
|`Box16b`|`number`|Box 16b extracted from Form 1040-ScheduleC.|123456|
|`Box17`|`number`|Box 17 extracted from Form 1040-ScheduleC.|123456|
|`Box18`|`number`|Box 18 extracted from Form 1040-ScheduleC.|123456|
|`Box19`|`number`|Box 19 extracted from Form 1040-ScheduleC.|123456|
|`Box20a`|`number`|Box 20a extracted from Form 1040-ScheduleC.|123456|
|`Box20b`|`number`|Box 20b extracted from Form 1040-ScheduleC.|123456|
|`Box21`|`number`|Box 21 extracted from Form 1040-ScheduleC.|123456|
|`Box22`|`number`|Box 22 extracted from Form 1040-ScheduleC.|123456|
|`Box23`|`number`|Box 23 extracted from Form 1040-ScheduleC.|123456|
|`Box24a`|`number`|Box 24a extracted from Form 1040-ScheduleC.|123456|
|`Box24b`|`number`|Box 24b extracted from Form 1040-ScheduleC.|123456|
|`Box25`|`number`|Box 25 extracted from Form 1040-ScheduleC.|123456|
|`Box26`|`number`|Box 26 extracted from Form 1040-ScheduleC.|123456|
|`Box27a`|`number`|Box 27a extracted from Form 1040-ScheduleC.|123456|
|`Box27b`|`number`|Box 27b extracted from Form 1040-ScheduleC.|123456|
|`Box28`|`number`|Box 28 extracted from Form 1040-ScheduleC.|123456|
|`Box29`|`number`|Box 29 extracted from Form 1040-ScheduleC.|123456|
|`Box30a`|`number`|Box 30a extracted from Form 1040-ScheduleC.|123456|
|`Box30b`|`number`|Box 30b extracted from Form 1040-ScheduleC.|123456|
|`Box30`|`number`|Box 30 extracted from Form 1040-ScheduleC.|123456|
|`Box31`|`number`|Box 31 extracted from Form 1040-ScheduleC.|123456|
|`Box32a`|`boolean`|Box 32a extracted from Form 1040-ScheduleC.|:selected:|
|`Box32b`|`boolean`|Box 32b extracted from Form 1040-ScheduleC.|:selected:|
|`Box33`|`selectionGroup`|Value will be a list containing at least one of the following: 'cost', 'lowerCostOrMarket', 'other'.|cost :unselected: lowerCostOrMarket :unselected: other :unselected:|
|`Box34`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box35`|`number`|Box 35 extracted from Form 1040-ScheduleC.|123456|
|`Box36`|`number`|Box 36 extracted from Form 1040-ScheduleC.|123456|
|`Box37`|`number`|Box 37 extracted from Form 1040-ScheduleC.|123456|
|`Box38`|`number`|Box 38 extracted from Form 1040-ScheduleC.|123456|
|`Box39`|`number`|Box 39 extracted from Form 1040-ScheduleC.|123456|
|`Box40`|`number`|Box 40 extracted from Form 1040-ScheduleC.|123456|
|`Box41`|`number`|Box 41 extracted from Form 1040-ScheduleC.|123456|
|`Box42`|`number`|Box 42 extracted from Form 1040-ScheduleC.|123456|
|`Box43`|`date`|Box 43 extracted from Form 1040-ScheduleC.|2022-12-31|
|`Box44a`|`number`|Box 44a extracted from Form 1040-ScheduleC.|123456|
|`Box44b`|`number`|Box 44b extracted from Form 1040-ScheduleC.|123456|
|`Box44c`|`number`|Box 44c extracted from Form 1040-ScheduleC.|123456|
|`Box45`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box46`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box47a`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box47b`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box48`|`number`|Box 48 extracted from Form 1040-ScheduleC.|123456|
|`OtherExpenses`|`array`|List of other business expense and equivalent amounts extracted from Form 1040-ScheduleC||
|`OtherExpenses.*`|`object`|||
|`OtherExpenses.*.Description`|`string`|Description extracted from Form 1040-ScheduleC.|Social media advert|
|`OtherExpenses.*.Amount`|`number`|Amount extracted from Form 1040-ScheduleC.|123456|