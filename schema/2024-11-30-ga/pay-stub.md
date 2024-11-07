# Document Intelligence pay stub model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**"prebuilt-payStub.us**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`EmployeeAddress`|`address`|Address of the employee|123 Maple Street, Springfield, IL, 62701|
|`EmployeeName`|`string`|Name of the employee|John A. Doe|
|`EmployeeSSN`|`string`|Social security number of the employee|123-45-6789|
|`EmployerAddress`|`address`|Address of the employer|456 Oak Avenue, Metropolis, NY, 10101|
|`EmployerName`|`string`|Listed name of the employer|Contoso Corporation|
|`PayDate`|`date`|Date of salary payment|Feb. 26, 2020|
|`PayPeriodStartDate`|`date`|Start date of the pay period|Feb. 19, 2020|
|`PayPeriodEndDate`|`date`|End date of the pay period|Feb. 25, 2020|
|`CurrentPeriodGrossPay`|`number`|Gross pay of the current period|$744.10|
|`YearToDateGrossPay`|`number`|Year-to-date gross pay|$2744.10|
|`CurrentPeriodTaxes`|`number`|Taxes of the current period|$410.10|
|`YearToDateTaxes`|`number`|Year-to-date taxes|$855.90|
|`CurrentPeriodDeductions`|`number`|Deductions of the current period|$410.10|
|`YearToDateDeductions`|`number`|Year-to-date deductions|$855.90|
|`CurrentPeriodNetPay`|`number`|Net pay of the current period|$744.10|
|`YearToDateNetPay`|`number`|Year-to-date net pay|$2744.10|
