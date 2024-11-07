# Document Intelligence health insurance card model

## 2024-11-30 (GA)

### Model ID

**prebuilt-healthInsuranceCard.us**

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`Insurer`|`string`|Health insurance provider name|PREMERA<br>BLUE CROSS|
|`Member`|`object`|||
|`Member.Name`|`string`|Member name|ANGEL BROWN|
|`Member.BirthDate`|`date`|Member date of birth|01/06/1958|
|`Member.Employer`|`string`|Member name employer|Microsoft|
|`Member.Gender`|`string`|Member gender|M|
|`Member.IdNumberSuffix`|`string`|Identification Number Suffix as it appears on some health insurance cards|01|
|`Dependents`|`array`|Array holding list of dependents, ordered where possible by membership suffix value||
|`Dependents.*`|`object`|||
|`Dependents.*.Name`|`string`|Dependent name|01|
|`IdNumber`|`object`|||
|`IdNumber.Prefix`|`string`|Identification Number Prefix as it appears on some health insurance cards|ABC|
|`IdNumber.Number`|`string`|Identification Number|123456789|
|`GroupNumber`|`string`|Insurance Group Number|1000000|
|`PrescriptionInfo`|`object`|||
|`PrescriptionInfo.Issuer`|`string`|ANSI issuer identification number (IIN)|(80840) 300-11908-77|
|`PrescriptionInfo.RxBIN`|`string`|Prescription issued BIN number|987654|
|`PrescriptionInfo.RxPCN`|`string`|Prescription processor control number|63200305|
|`PrescriptionInfo.RxGrp`|`string`|Prescription group number|BCAAXYZ|
|`PrescriptionInfo.RxId`|`string`|Prescription identification number. If not present, will default to membership id number|P97020065|
|`PrescriptionInfo.RxPlan`|`string`|Prescription Plan number|A1|
|`Pbm`|`string`|Pharmacy Benefit Manager for the plan|CVS CAREMARK|
|`EffectiveDate`|`date`|Date from which the plan is effective|08/12/2012|
|`Copays`|`array`|Array holding list of CoPay Benefits||
|`Copays.*`|`object`|||
|`Copays.*.Benefit`|`string`|Co-Pay Benefit name|Deductible|
|`Copays.*.Amount`|`currency`|Co-Pay required amount|$1,500|
|`Payer`|`object`|||
|`Payer.Id`|`string`|Payer Id Number|89063|
|`Payer.Address`|`address`|Payer address|123 Service St, Redmond WA, 98052|
|`Payer.PhoneNumber`|`phoneNumber`|Payer phone number|+1 (987) 213-5674|
|`Plan`|`object`|||
|`Plan.Number`|`string`|Plan number|456|
|`Plan.Name`|`string`|Plan name - If see Medicaid -> then medicaid|HEALTH SAVINGS PLAN|
|`Plan.Type`|`string`|Plan type|PPO|
|`MedicareMedicaidInfo`|`object`|||
|`MedicareMedicaidInfo.Id`|`string`|Medicare or Medicaid number|1AB2-CD3-EF45|
|`MedicareMedicaidInfo.PartAEffectiveDate`|`date`|Effective date of Medicare Part A|01-01-2023|
|`MedicareMedicaidInfo.PartBEffectiveDate`|`date`|Effective date of Medicare Part B|01-01-2023|