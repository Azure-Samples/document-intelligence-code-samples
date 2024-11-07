# Document Intelligence US tax form 1099 Combo model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

#### Model ID

**prebuilt-tax.us.1099COMBO**


### Supported document fields
| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`TaxYear`|`string`|Tax Year extracted from Form 1099-COMBO.|2022|
|`Payer`|`object`|||
|`Payer.TIN`|`string`|Payer tax identification number.|123-45-6789|
|`Payer.Name`|`string`|Payer full name as written on the form.|John Smith|
|`Payer.Address`|`address`|Payer address.|123 Microsoft Way, Redmond WA 98052|
|`Payer.AccountNumber`|`phoneNumber`|Payer Phone Number.|+19876543210|
|`Recipient`|`object`|||
|`Recipient.TIN`|`string`|Recipient tax identification number.|123-45-6789|
|`Recipient.Name`|`string`|Recipient full name as written on the form.|John Smith|
|`Recipient.Address`|`address`|Recipient address.|123 Microsoft Way, Redmond WA 98052|
|`Recipient.AccountNumber`|`string`|Recipient account number.|55123456789|
|`1099-B`|`object`|||
|`1099-B.Summary`|`array`|List of transactions summary reported in the Form 1099-B||
|`1099-B.Summary.*`|`object`|||
|`1099-B.Summary.*.Category`|`string`|Can be one for the following: 'shortTermBasisReportedToIRS', 'shortTermBasisNotReportedToIRS', 'shortTerm1099BNotReceived', 'longTermBasisReportedToIRS', 'longTermBasisNotReportedToIRS', 'longTerm1099BNotReceived', 'underterminedTermBasisReportedToIRS', 'undertinedTermBasisNotReportedToIRS', 'undertined1099BNotReceived'.|shortTermBasisReportedToIRS|
|`1099-B.Summary.*.TotalProceeds`|`number`|Total proceeds summary extracted from Form 1099-B.|123456|
|`1099-B.Summary.*.TotalCostBasis`|`string`|Total cost basis summary extracted from Form 1099-B.|123456|
|`1099-B.Summary.*.TotalMarketDiscount`|`string`|Total market discount summary extracted from Form 1099-B.|123456|
|`1099-B.Summary.*.TotalWashSales`|`string`|Total wash sales summary extracted from Form 1099-B.|123456|
|`1099-B.Summary.*.TotalRealizedGainOrLoss`|`string`|Total realized gain or loss summary extracted from Form 1099-B.|123456|
|`1099-B.Summary.*.TotalFederalIncomeTaxWithheld`|`string`|Total federal income tax withheld summary extracted from Form 1099-B.|123456|
|`1099-B.Transactions`|`array`|List of transactions reported in the Form 1099-B||
|`1099-B.Transactions.*`|`object`|||
|`1099-B.Transactions.*.CusipNumber`|`string`|Cusip Number extracted from Form 1099-B.|981276345|
|`1099-B.Transactions.*.IsFactaFilingRequired`|`boolean`|Is Facta Filing Required extracted from Form 1099-B.|:selected:|
|`1099-B.Transactions.*.ApplicableForm8949Checkbox`|`string`|Applicable Form8949 Checkbox extracted from Form 1099-B.|A|
|`1099-B.Transactions.*.BasisStatus`|`selectionGroup`|Value will be a list containing at least one of the following: 'basisReportedToIRS', 'basisNotReportedToIRS', '1099BNotReceived'.|basisReportedToIRS :unselected: basisNotReportedToIRS :unselected: undertermined :unselected:|
|`1099-B.Transactions.*.Box1a`|`string`|Box 1a extracted from Form 1099-B.|100 sh. XYZ Co.|
|`1099-B.Transactions.*.Box1b`|`date`|Box 1b extracted from Form 1099-B.|2022-12-31|
|`1099-B.Transactions.*.Box1c`|`date`|Box 1c extracted from Form 1099-B.|2022-12-31|
|`1099-B.Transactions.*.Box1d`|`number`|Box 1d extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box1e`|`number`|Box 1e extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box1f`|`number`|Box 1f extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box1g`|`number`|Box 1g extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box2`|`selectionGroup`|Value will be a list containing at least one of the following: 'shortTermGainOrLoss', 'longTermGainOrLoss', 'ordinary', 'undertermined'.|shortTermGainOrLoss :unselected: longTermGainOrLoss :unselected: ordinary :unselected:|
|`1099-B.Transactions.*.Box3`|`selectionGroup`|Value will be a list containing at least one of the following: 'collectible', 'qof'.|collectible :unselected: qof :unselected:|
|`1099-B.Transactions.*.Box4`|`number`|Box 4 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box5`|`boolean`|Box 5 extracted from Form 1099-B.|:selected:|
|`1099-B.Transactions.*.Box6`|`selectionGroup`|Value will be a list containing at least one of the following: 'grossProceeds', 'netProceeds'.|grossProceeds :unselected: netProceeds :unselected:|
|`1099-B.Transactions.*.Box7`|`boolean`|Box 7 extracted from Form 1099-B.|:selected:|
|`1099-B.Transactions.*.Box8`|`number`|Box 8 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box9`|`number`|Box 9 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box10`|`number`|Box 10 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box11`|`number`|Box 11 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.Box12`|`boolean`|Box 12 extracted from Form 1099-B.|:selected:|
|`1099-B.Transactions.*.Box13`|`number`|Box 13 extracted from Form 1099-B.|123456|
|`1099-B.Transactions.*.StateTaxesWithheld`|`array`|State Taxes Withheld extracted from Form 1099-B||
|`1099-B.Transactions.*.StateTaxesWithheld.*`|`object`|||
|`1099-B.Transactions.*.StateTaxesWithheld.*.Box14`|`string`|Box 14 extracted from Form 1099-B.|WA|
|`1099-B.Transactions.*.StateTaxesWithheld.*.Box15`|`string`|Box 15 extracted from Form 1099-B.|12-3456789|
|`1099-B.Transactions.*.StateTaxesWithheld.*.Box16`|`number`|Box 16 extracted from Form 1099-B.|123456|
|`1099-DIV`|`object`|||
|`1099-DIV.Box1a`|`number`|Box 1a extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box1b`|`number`|Box 1b extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2a`|`number`|Box 2a extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2b`|`number`|Box 2b extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2c`|`number`|Box 2c extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2d`|`number`|Box 2d extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2e`|`number`|Box 2e extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box2f`|`number`|Box 2f extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box3`|`number`|Box 3 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box4`|`number`|Box 4 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box5`|`number`|Box 5 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box6`|`number`|Box 6 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box7`|`number`|Box 7 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box8`|`string`|Box 8 extracted from Form 1099-DIV.|Foreign|
|`1099-DIV.Box9`|`number`|Box 9 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box10`|`number`|Box 10 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box11`|`boolean`|Box 11 extracted from Form 1099-DIV.|:selected:|
|`1099-DIV.Box12`|`number`|Box 12 extracted from Form 1099-DIV.|123456|
|`1099-DIV.Box13`|`number`|Box 13 extracted from Form 1099-DIV.|123456|
|`1099-DIV.StateTaxesWithheld`|`array`|State Taxes Withheld extracted from Form 1099-DIV||
|`1099-DIV.StateTaxesWithheld.*`|`object`|||
|`1099-DIV.StateTaxesWithheld.*.Box14`|`string`|Box 14 extracted from Form 1099-DIV.|WA|
|`1099-DIV.StateTaxesWithheld.*.Box15`|`string`|Box 15 extracted from Form 1099-DIV.|12-3456789|
|`1099-DIV.StateTaxesWithheld.*.Box16`|`number`|Box 16 extracted from Form 1099-DIV.|123456|
|`1099-INT`|`object`|||
|`1099-INT.IsFactaFilingRequired`|`boolean`|Is Facta Filing Required extracted from Form 1099-INT.|:selected:|
|`1099-INT.Box1`|`number`|Box 1 extracted from Form 1099-INT.|123456|
|`1099-INT.Box2`|`number`|Box 2 extracted from Form 1099-INT.|123456|
|`1099-INT.Box3`|`number`|Box 3 extracted from Form 1099-INT.|123456|
|`1099-INT.Box4`|`number`|Box 4 extracted from Form 1099-INT.|123456|
|`1099-INT.Box5`|`number`|Box 5 extracted from Form 1099-INT.|123456|
|`1099-INT.Box6`|`number`|Box 6 extracted from Form 1099-INT.|123456|
|`1099-INT.Box7`|`string`|Box 7 extracted from Form 1099-INT.|Foreign|
|`1099-INT.Box8`|`number`|Box 8 extracted from Form 1099-INT.|123456|
|`1099-INT.Box9`|`number`|Box 9 extracted from Form 1099-INT.|123456|
|`1099-INT.Box10`|`number`|Box 10 extracted from Form 1099-INT.|123456|
|`1099-INT.Box11`|`number`|Box 11 extracted from Form 1099-INT.|123456|
|`1099-INT.Box12`|`number`|Box 12 extracted from Form 1099-INT.|123456|
|`1099-INT.Box13`|`number`|Box 13 extracted from Form 1099-INT.|123456|
|`1099-INT.Box14`|`string`|Box 14 extracted from Form 1099-INT.|123456789|
|`1099-INT.StateTaxesWithheld`|`array`|State Taxes Withheld extracted from Form 1099-INT||
|`1099-INT.StateTaxesWithheld.*`|`object`|||
|`1099-INT.StateTaxesWithheld.*.Box15`|`string`|Box 15 extracted from Form 1099-INT.|WA|
|`1099-INT.StateTaxesWithheld.*.Box16`|`string`|Box 16 extracted from Form 1099-INT.|12-3456789|
|`1099-INT.StateTaxesWithheld.*.Box17`|`number`|Box 17 extracted from Form 1099-INT.|123456|