# Document Intelligence mortgage closing disclosure model

## 2024-11-30 (GA)

### Supported languages and locales

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`)|

### Model ID

**prebuilt-mortgage.us.closingDisclosure**

### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`Closing`|`object`|||
|`Closing.IssueDate`|`date`|Issue date|4/15/2013|
|`Closing.ClosingDate`|`date`|Closing date|4/15/2013|
|`Closing.DisbursementDate`|`date`|Disbursement date|4/15/2013|
|`Closing.SettlementAgent`|`string`|Settlement agent|Epsilon Title Co.|
|`Closing.FileNumber`|`string`|File number|12-3456|
|`Closing.PropertyAddress`|`address`|Property address|123 Main St., Redmond WA 98052|
|`Closing.SalePrice`|`number`|Sale price|$180,000|
|`Transaction`|`object`|||
|`Transaction.BorrowerName`|`string`|Borrower's name|Michael Jones and Mary Stone|
|`Transaction.BorrowerAddress`|`address`|Borrower's address|123 Microsoft Way, Redmond WA 98052|
|`Transaction.SellerName`|`string`|Seller's name|Renner, Hamill and Harber|
|`Transaction.SellerAddress`|`address`|Seller's address|9180 Landen Curve Apt. 137<br>Gulfport, MO 39503, United States|
|`Transaction.LenderName`|`string`|Lender's name|Ficus Bank|
|`Transaction.BorrowerClosingCosts`|`number`|Borrower's closing costs|$9,712.10|
|`Transaction.BorrowerCashToCloseType`|`selectionGroup`|Borrower's cash to close type|:selected: From :unselected: To|
|`Transaction.BorrowerCashToCloseAmount`|`number`|Borrower's cash to close amount|$9,712.10|
|`Transaction.SellerCashToCloseType`|`selectionGroup`|Seller's cash to close type|:unselected: From :selected: To|
|`Transaction.SellerCashToCloseAmount`|`number`|Seller's cash to close amount|$64,414.96|
|`Transaction.CoBorrowerNames`|`string`|Full names of all co-borrowers as written on the form|Glory Grant|
|`Loan`|`object`|||
|`Loan.Term`|`string`|Loan term|30 years|
|`Loan.Purpose`|`string`|Loan purpose|Purchase|
|`Loan.Product`|`string`|Loan product|Fixed Rate|
|`Loan.Type`|`selectionGroup`|Loan type|:selected: Conventional :unselected: FHA :unselected: VA :unselected:|
|`Loan.OtherType`|`string`|Other loan type|RHS|
|`Loan.IdentificationNumber`|`string`|Loan identification number|123456789|
|`Loan.MortgageInsuranceCaseNumber`|`string`|Mortgage insurance case number|000654321|
|`Loan.Amount`|`number`|Loan amount|$162,000|
|`Loan.InterestRate`|`number`|Interest rate|3.875|
|`Loan.MonthlyPrincipalAndInterest`|`number`|Monthly principal and interest|$761.78|
|`Loan.EstimatedTaxInsuranceAndAssessmentsPerMonth`|`number`|Estimated taxes, insurance and assessments per month|$356.13|
|`ApplicantConfirmReceiptSignature`|`signature`|Applicant's confirmation signature.|Michael Jones and Mary Stone|
|`CoApplicantConfirmReceiptSignature`|`signature`|Co-Applicant's confirmation signature.|Mary Stone|
