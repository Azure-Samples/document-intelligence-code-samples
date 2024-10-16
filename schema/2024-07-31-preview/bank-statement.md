# Document Intelligence bank statement model

## **2024-07-31-preview**

## Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

### Model Id: 

**prebuilt-bankStatement.us**

## Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`BankAddress`|`address`|Listed address of the bank|123 Main St, Redmond, WA 98052|
|`BankName`|`string`|Listed name of the bank|Contoso Bank|
|`AccountHolderAddress`|`address`|Address of the account holder|456 Main St, Redmond, WA 98052|
|`AccountHolderName`|`string`|Name of the account holder|JOHN DEO|
|`StatementStartDate`|`date`|Start date of the bank statement|July 01, 2017|
|`StatementEndDate`|`date`|End date of the bank statement|July 31, 2017|
|`Accounts`|`array`|||
|`Accounts.*`|`object`|||
|`Accounts.*.AccountNumber`|`string`|Account number on the bank statement|987-654-3210|
|`Accounts.*.AccountType`|`string`|Type of account on the bank statement|Checking|
|`Accounts.*.BeginningBalance`|`number`|Beginning balance on the bank statement|$1488.03|
|`Accounts.*.EndingBalance`|`number`|Ending balance on the bank statement|$1488.03|
|`Accounts.*.TotalServiceFees`|`number`|Total service fees|$0.00|
|`Accounts.*.Transactions`|`array`|Extracted transaction line item|07/17<br>OnlineTransfer From Chk...6609 Transaction#: 6373187418<br>$1,500.00|
|`Accounts.*.Transactions.*`|`object`|||
|`Accounts.*.Transactions.*.Date`|`date`|Transaction date|07/17|
|`Accounts.*.Transactions.*.Description`|`string`|Transaction description|OnlineTransfer From Chk...6609 Transaction#: 6373187418|
|`Accounts.*.Transactions.*.CheckNumber`|`string`|Check number of the transaction|6609|
|`Accounts.*.Transactions.*.DepositAmount`|`number`|Amount of deposit in the transaction|$1500.00|
|`Accounts.*.Transactions.*.WithdrawalAmount`|`number`|Amount of withdrawal in the transaction|$1500.00|
