# Document Intelligence US tax form 1040 Schedule `E` model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1040ScheduleE**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1040-ScheduleE.|2022|
|`Taxpayer`|`object`|||
|`Taxpayer.SSN`|`string`|Taxpayer tax social security number.|123-45-6789|
|`Taxpayer.Name`|`string`|Taxpayer name as written on the form.|Smith|
|`BoxA`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`BoxB`|`selectionGroup`|Value will be a list containing at least one of the following: 'yes', 'no'.|yes :unselected: no :unselected:|
|`Box19ExtraInfo`|`string`|Box19 Extra Info extracted from Form 1040-ScheduleE.|Pest control|
|`Box23a`|`number`|Box 23a extracted from Form 1040-ScheduleE.|123456|
|`Box23b`|`number`|Box 23b extracted from Form 1040-ScheduleE.|123456|
|`Box23c`|`number`|Box 23c extracted from Form 1040-ScheduleE.|123456|
|`Box23d`|`number`|Box 23d extracted from Form 1040-ScheduleE.|123456|
|`Box23e`|`number`|Box 23e extracted from Form 1040-ScheduleE.|123456|
|`Box24`|`number`|Box 24 extracted from Form 1040-ScheduleE.|123456|
|`Box25`|`number`|Box 25 extracted from Form 1040-ScheduleE.|123456|
|`Box26`|`number`|Box 26 extracted from Form 1040-ScheduleE.|123456|
|`OtherPropertyDescription`|`string`|Other Property Description extracted from Form 1040-SE.|Land|
|`IncomeOrLossFromRentalRealEstatePropertyDetails`|`array`|Income or loss from rental real estate property and royalties detailed information extracted from Form 1040-ScheduleE||
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*`|`object`|||
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.PhysicalAddress`|`address`|Physical Address extracted from Form 1040-ScheduleE.|123 Microsoft Way, Redmond WA 98052|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.FairRentalDays`|`number`|Fair Rental Days extracted from Form 1040-ScheduleE.|1|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.PersonalUseDays`|`number`|Personal Use Days extracted from Form 1040-ScheduleE.|364|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.QJV`|`boolean`|Q J V extracted from Form 1040-ScheduleE.|:selected:|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box3`|`number`|Box 3 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box4`|`number`|Box 4 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box5`|`number`|Box 5 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box6`|`number`|Box 6 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box7`|`number`|Box 7 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box8`|`number`|Box 8 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box9`|`number`|Box 9 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box10`|`number`|Box 10 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box11`|`number`|Box 11 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box12`|`number`|Box 12 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box13`|`number`|Box 13 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box14`|`number`|Box 14 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box15`|`number`|Box 15 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box16`|`number`|Box 16 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box17`|`number`|Box 17 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box18`|`number`|Box 18 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box19`|`number`|Box 19 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box20`|`number`|Box 20 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box21`|`number`|Box 21 extracted from Form 1040-ScheduleE.|123456|
|`IncomeOrLossFromRentalRealEstatePropertyDetails.*.Box22`|`number`|Box 22 extracted from Form 1040-ScheduleE.|123456|
