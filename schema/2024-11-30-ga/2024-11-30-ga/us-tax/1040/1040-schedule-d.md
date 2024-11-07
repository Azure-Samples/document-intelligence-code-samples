# Document Intelligence US tax form 1040 Schedule `D` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleD**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleD.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`QualifiedInvestmentDisposition`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box4`|`number`|Box 4 extracted from Form 1040-ScheduleD.|123456|
|`Box5`|`number`|Box 5 extracted from Form 1040-ScheduleD.|123456|
|`Box6`|`number`|Box 6 extracted from Form 1040-ScheduleD.|123456|
|`Box7`|`number`|Box 7 extracted from Form 1040-ScheduleD.|123456|
|`Box11`|`number`|Box 11 extracted from Form 1040-ScheduleD.|123456|
|`Box12`|`number`|Box 12 extracted from Form 1040-ScheduleD.|123456|
|`Box13`|`number`|Box 13 extracted from Form 1040-ScheduleD.|123456|
|`Box14`|`number`|Box 14 extracted from Form 1040-ScheduleD.|123456|
|`Box15`|`number`|Box 15 extracted from Form 1040-ScheduleD.|123456|
|`Box16`|`number`|Box 16 extracted from Form 1040-ScheduleD.|123456|
|`Box17`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box18`|`number`|Box 18 extracted from Form 1040-ScheduleD.|123456|
|`Box19`|`number`|Box 19 extracted from Form 1040-ScheduleD.|123456|
|`Box20`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box21`|`number`|Box 21 extracted from Form 1040-ScheduleD.|123456|
|`Box22`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box1a`|`object`|Totals for all short-term transactions reported on Form 1099-B for which basis was reported to the IRS and for which you have no adjustments||
|`Box1a.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box1a.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box1a.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box1b`|`object`|Totals for all transactions reported on Form(s) 8949 with Box A checked.||
|`Box1b.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box1b.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box1b.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box1b.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box2`|`object`|Totals for all transactions reported on Form(s) 8949 with Box B checked.||
|`Box2.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box2.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box2.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box2.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box3`|`object`|Totals for all transactions reported on Form(s) 8949 with Box C checked.||
|`Box3.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box3.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box3.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box3.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box8a`|`object`|Totals for all long-term transactions reported on Form 1099-B for which basis was reported to the IRS and for which you have no adjustments||
|`Box8a.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box8a.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box8a.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box8b`|`object`|Totals for all transactions reported on Form(s) 8949 with Box D checked.||
|`Box8b.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box8b.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box8b.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box8b.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box9`|`object`|Totals for all transactions reported on Form(s) 8949 with Box E checked.||
|`Box9.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box9.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box9.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box9.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|
|`Box10`|`object`|Totals for all transactions reported on Form(s) 8949 with Box F checked.||
|`Box10.Proceeds`|`number`|Proceeds extracted from Form 1040-ScheduleD.|123456|
|`Box10.Cost`|`number`|Cost extracted from Form 1040-ScheduleD.|123456|
|`Box10.Adjustments`|`number`|Adjustments extracted from Form 1040-ScheduleD.|123456|
|`Box10.GainOrLoss`|`number`|Gain Or Loss extracted from Form 1040-ScheduleD.|123456|