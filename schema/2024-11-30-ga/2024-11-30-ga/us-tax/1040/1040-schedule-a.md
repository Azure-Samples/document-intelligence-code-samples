# Document Intelligence US tax form 1040 Schedule `A` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleA**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleA.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`Box1`|`number`|Box 1 extracted from Form 1040-ScheduleA.|123456|
|`Box2`|`number`|Box 2 extracted from Form 1040-ScheduleA.|123456|
|`Box3`|`number`|Box 3 extracted from Form 1040-ScheduleA.|123456|
|`Box4`|`number`|Box 4 extracted from Form 1040-ScheduleA.|123456|
|`Box5aCheckbox`|`boolean`|Box5a Checkbox extracted from Form 1040-ScheduleA.|:selected:|
|`Box5a`|`number`|Box 5a extracted from Form 1040-ScheduleA.|123456|
|`Box5b`|`number`|Box 5b extracted from Form 1040-ScheduleA.|123456|
|`Box5c`|`number`|Box 5c extracted from Form 1040-ScheduleA.|123456|
|`Box5d`|`number`|Box 5d extracted from Form 1040-ScheduleA.|123456|
|`Box5e`|`number`|Box 5e extracted from Form 1040-ScheduleA.|123456|
|`Box6ExtraInfo`|`string`|Box6 Extra Info extracted from Form 1040-ScheduleA.|Sales Tax|
|`Box6`|`number`|Box 6 extracted from Form 1040-ScheduleA.|123456|
|`Box7`|`number`|Box 7 extracted from Form 1040-ScheduleA.|123456|
|`Box8Checkbox`|`boolean`|Box8 Checkbox extracted from Form 1040-ScheduleA.|:selected:|
|`Box8a`|`number`|Box 8a extracted from Form 1040-ScheduleA.|123456|
|`Box8b`|`number`|Box 8b extracted from Form 1040-ScheduleA.|123456|
|`Box8bExtraInfo`|`string`|Box8b Extra Info extracted from Form 1040-ScheduleA.|Bob Weydert|
|`Box8c`|`number`|Box 8c extracted from Form 1040-ScheduleA.|123456|
|`Box8d`|`number`|Box 8d extracted from Form 1040-ScheduleA.|123456|
|`Box8e`|`number`|Box 8e extracted from Form 1040-ScheduleA.|123456|
|`Box9`|`number`|Box 9 extracted from Form 1040-ScheduleA.|123456|
|`Box10`|`number`|Box 10 extracted from Form 1040-ScheduleA.|123456|
|`Box11`|`number`|Box 11 extracted from Form 1040-ScheduleA.|123456|
|`Box12`|`number`|Box 12 extracted from Form 1040-ScheduleA.|123456|
|`Box13`|`number`|Box 13 extracted from Form 1040-ScheduleA.|123456|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleA.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleA.|123456|
|`Box16`|`number`|Box 16 extracted from Form 1040-ScheduleA.|123456|
|`Box16ExtraInfo`|`number`|Box16 Extra Info extracted from Form 1040-ScheduleA.|123456|
|`Box17`|`number`|Box 17 extracted from Form 1040-ScheduleA.|123456|
|`Box18Checkbox`|`number`|Box18 Checkbox extracted from Form 1040-ScheduleA.|123456|