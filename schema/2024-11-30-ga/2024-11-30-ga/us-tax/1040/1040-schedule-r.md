# Document Intelligence US tax form 1040 Schedule `R` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleR**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleR.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`Part1`|`selectionGroup`|Value will be a list containing at least one of the following: '65OrOlder', 'under65AndRetiredOnDisability', 'bothSpouse65OrOlder', 'bothSpouseUnder65ButOneSpouseRetiredOnDisability', 'bothSpouseUnder65AndRetiredOnDisability', 'onlyOneSpouseAbove65AndOtherSpouseRetiredOnDisability', 'oneSpouseAbove65AndOtherSpouseRetiredOnDisability', 'oneSpouseAbove65AndOtherSpouseNotRetiredOnDisability'.|65OrOlder :unselected: under65AndRetiredOnDisability :unselected: bothSpouse65OrOlder :unselected: bothSpouseUnder65ButOneSpouseRetiredOnDisability :unselected: bothSpouseUnder65AndRetiredOnDisability :unselected: onlyOneSpouseAbove65AndOtherSpouseRetiredOnDisability :unselected: oneSpouseAbove65AndOtherSpouseRetiredOnDisability :unselected: oneSpouseAbove65AndOtherSpouseNotRetiredOnDisability :unselected:|
|`Part2Checkbox`|`boolean`|Part2 Checkbox extracted from Form 1040-ScheduleR.|:selected:|
|`Box10`|`number`|Box 10 extracted from Form 1040-ScheduleR.|123456|
|`Box11`|`number`|Box 11 extracted from Form 1040-ScheduleR.|123456|
|`Box12`|`number`|Box 12 extracted from Form 1040-ScheduleR.|123456|
|`Box13a`|`number`|Box 13a extracted from Form 1040-ScheduleR.|123456|
|`Box13b`|`number`|Box 13b extracted from Form 1040-ScheduleR.|123456|
|`Box13c`|`number`|Box 13c extracted from Form 1040-ScheduleR.|123456|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleR.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleR.|123456|
|`Box16`|`number`|Box 16 extracted from Form 1040-ScheduleR.|123456|
|`Box17`|`number`|Box 17 extracted from Form 1040-ScheduleR.|123456|
|`Box18`|`number`|Box 18 extracted from Form 1040-ScheduleR.|123456|
|`Box19`|`number`|Box 19 extracted from Form 1040-ScheduleR.|123456|
|`Box20`|`number`|Box 20 extracted from Form 1040-ScheduleR.|123456|
|`Box21`|`number`|Box 21 extracted from Form 1040-ScheduleR.|123456|
|`Box22`|`number`|Box 22 extracted from Form 1040-ScheduleR.|123456|