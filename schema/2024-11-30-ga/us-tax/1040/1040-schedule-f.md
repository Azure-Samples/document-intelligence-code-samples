# Document Intelligence US tax form 1040 Schedule `F` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleF**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleF.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`BoxA`|`string`|Box A extracted from Form 1040-ScheduleF.|Wheat|
|`BoxB`|`string`|Box B extracted from Form 1040-ScheduleF.|123456|
|`BoxC`|`selectionGroup`|Value will be a list containing at least one of the following: 'cash', 'accrual'.|cash :unselected: accrual :unselected:|
|`BoxD`|`string`|Box D extracted from Form 1040-ScheduleF.|12-3456789|
|`BoxE`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxF`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxG`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box1a`|`number`|Box 1a extracted from Form 1040-ScheduleF.|123456|
|`Box1b`|`number`|Box 1b extracted from Form 1040-ScheduleF.|123456|
|`Box1c`|`number`|Box 1c extracted from Form 1040-ScheduleF.|123456|
|`Box2`|`number`|Box 2 extracted from Form 1040-ScheduleF.|123456|
|`Box3a`|`number`|Box 3a extracted from Form 1040-ScheduleF.|123456|
|`Box3b`|`number`|Box 3b extracted from Form 1040-ScheduleF.|123456|
|`Box4a`|`number`|Box 4a extracted from Form 1040-ScheduleF.|123456|
|`Box4b`|`number`|Box 4b extracted from Form 1040-ScheduleF.|123456|
|`Box5a`|`number`|Box 5a extracted from Form 1040-ScheduleF.|123456|
|`Box5b`|`number`|Box 5b extracted from Form 1040-ScheduleF.|123456|
|`Box5c`|`number`|Box 5c extracted from Form 1040-ScheduleF.|123456|
|`Box6a`|`number`|Box 6a extracted from Form 1040-ScheduleF.|123456|
|`Box6b`|`number`|Box 6b extracted from Form 1040-ScheduleF.|123456|
|`Box6c`|`boolean`|Box 6c extracted from Form 1040-ScheduleF.|:selected:|
|`Box6d`|`number`|Box 6d extracted from Form 1040-ScheduleF.|123456|
|`Box7`|`number`|Box 7 extracted from Form 1040-ScheduleF.|123456|
|`Box8`|`number`|Box 8 extracted from Form 1040-ScheduleF.|123456|
|`Box9`|`number`|Box 9 extracted from Form 1040-ScheduleF.|123456|
|`Box10`|`number`|Box 10 extracted from Form 1040-ScheduleF.|123456|
|`Box11`|`number`|Box 11 extracted from Form 1040-ScheduleF.|123456|
|`Box12`|`number`|Box 12 extracted from Form 1040-ScheduleF.|123456|
|`Box13`|`number`|Box 13 extracted from Form 1040-ScheduleF.|123456|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleF.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleF.|123456|
|`Box16`|`number`|Box 16 extracted from Form 1040-ScheduleF.|123456|
|`Box17`|`number`|Box 17 extracted from Form 1040-ScheduleF.|123456|
|`Box18`|`number`|Box 18 extracted from Form 1040-ScheduleF.|123456|
|`Box19`|`number`|Box 19 extracted from Form 1040-ScheduleF.|123456|
|`Box20`|`number`|Box 20 extracted from Form 1040-ScheduleF.|123456|
|`Box21a`|`number`|Box 21a extracted from Form 1040-ScheduleF.|123456|
|`Box21b`|`number`|Box 21b extracted from Form 1040-ScheduleF.|123456|
|`Box22`|`number`|Box 22 extracted from Form 1040-ScheduleF.|123456|
|`Box23`|`number`|Box 23 extracted from Form 1040-ScheduleF.|123456|
|`Box24a`|`number`|Box 24a extracted from Form 1040-ScheduleF.|123456|
|`Box24b`|`number`|Box 24b extracted from Form 1040-ScheduleF.|123456|
|`Box25`|`number`|Box 25 extracted from Form 1040-ScheduleF.|123456|
|`Box26`|`number`|Box 26 extracted from Form 1040-ScheduleF.|123456|
|`Box27`|`number`|Box 27 extracted from Form 1040-ScheduleF.|123456|
|`Box28`|`number`|Box 28 extracted from Form 1040-ScheduleF.|123456|
|`Box29`|`number`|Box 29 extracted from Form 1040-ScheduleF.|123456|
|`Box30`|`number`|Box 30 extracted from Form 1040-ScheduleF.|123456|
|`Box31`|`number`|Box 31 extracted from Form 1040-ScheduleF.|123456|
|`Box32aExtraInfo`|`string`|Box32a Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32a`|`number`|Box 32a extracted from Form 1040-ScheduleF.|123456|
|`Box32bExtraInfo`|`string`|Box32b Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32b`|`number`|Box 32b extracted from Form 1040-ScheduleF.|123456|
|`Box32cExtraInfo`|`string`|Box32c Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32c`|`number`|Box 32c extracted from Form 1040-ScheduleF.|123456|
|`Box32dExtraInfo`|`string`|Box32d Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32d`|`number`|Box 32d extracted from Form 1040-ScheduleF.|123456|
|`Box32eExtraInfo`|`string`|Box32e Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32e`|`number`|Box 32e extracted from Form 1040-ScheduleF.|123456|
|`Box32fExtraInfo`|`string`|Box32f Extra Info extracted from Form 1040-ScheduleF.|Landscaping|
|`Box32f`|`number`|Box 32f extracted from Form 1040-ScheduleF.|123456|
|`Box33`|`number`|Box 33 extracted from Form 1040-ScheduleF.|123456|
|`Box34`|`number`|Box 34 extracted from Form 1040-ScheduleF.|123456|
|`Box36`|`selectionGroup`|Value will be a list containing at least one of the following: 'allInvestmentAtRisk', 'someInvestmentNotAtRisk'.|allInvestmentAtRisk :unselected: someInvestmentNotAtRisk :unselected:|
|`Box37`|`number`|Box 37 extracted from Form 1040-ScheduleF.|123456|
|`Box38a`|`number`|Box 38a extracted from Form 1040-ScheduleF.|123456|
|`Box38b`|`number`|Box 38b extracted from Form 1040-ScheduleF.|123456|
|`Box39a`|`number`|Box 39a extracted from Form 1040-ScheduleF.|123456|
|`Box39b`|`number`|Box 39b extracted from Form 1040-ScheduleF.|123456|
|`Box40a`|`number`|Box 40a extracted from Form 1040-ScheduleF.|123456|
|`Box40b`|`number`|Box 40b extracted from Form 1040-ScheduleF.|123456|
|`Box40c`|`number`|Box 40c extracted from Form 1040-ScheduleF.|123456|
|`Box41`|`number`|Box 41 extracted from Form 1040-ScheduleF.|123456|
|`Box42`|`number`|Box 42 extracted from Form 1040-ScheduleF.|123456|
|`Box43`|`number`|Box 43 extracted from Form 1040-ScheduleF.|123456|
|`Box44`|`number`|Box 44 extracted from Form 1040-ScheduleF.|123456|
|`Box45`|`number`|Box 45 extracted from Form 1040-ScheduleF.|123456|
|`Box46`|`number`|Box 46 extracted from Form 1040-ScheduleF.|123456|
|`Box47`|`number`|Box 47 extracted from Form 1040-ScheduleF.|123456|
|`Box48`|`number`|Box 48 extracted from Form 1040-ScheduleF.|123456|
|`Box49`|`number`|Box 49 extracted from Form 1040-ScheduleF.|123456|
|`Box50`|`number`|Box 50 extracted from Form 1040-ScheduleF.|123456|