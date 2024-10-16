# Document Intelligence Bank check model

## [2024-07-31-preview](#tab/2024-07-31-preview)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**check.us**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`PayerName`|`string`|Name of the payer (drawer)|Jane Doe|
|`PayerAddress`|`address`|Address of the payer (drawer)|123 Main St, Redmond, WA 98052|
|`PayTo`|`string`|Name of the payee|John Smith|
|`CheckDate`|`date`|Date the check was written|2023-04-01|
|`NumberAmount`|`number`|Amount of the check in numeric form|150.00|
|`WordAmount`|`number`|Amount of the check in written form|one hundred fifty and 00/100|
|`BankName`|`string`|Name of the bank|Contoso Bank|
|`Memo`|`string`|Short note describing the payment|April Rent Payment|
|`MICR`|`object`|Magnetic Ink Character Recognition (MICR) line|⑈0740⑈ ⑆123456789⑆ 1001001234⑈|
|`MICR.RoutingNumber`|`string`|Routing number of the bank|⑆123456789⑆|
|`MICR.AccountNumber`|`string`|Account number|1001001234⑈|
|`MICR.CheckNumber`|`string`|Check number|⑈0740⑈|
