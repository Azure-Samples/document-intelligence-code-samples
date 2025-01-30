# Document Intelligence invoice model

## 2024-11-30 (GA)

### Model ID

**prebuilt-invoice**

### Supported languages

| Supported Languages | Details |
|:--------------------|:-------:|
|English|United States (`en-US`), Australia (`en-AU`), Canada (`en-CA`), United Kingdom (`en-GB`), India (`en-IN`)|
|Dutch|Netherlands (`nl-NL`)|
|French|France (`fr-FR`)|
|German|Germany (`de-DE`)|
|Italian|Italy (`it-IT`)|
|Portuguese|Portugal (`pt-PT`), Brazil (`pt-BR`)|
|Spanish|Argentina (`es-AR`), Bolivia (`es-BO`), Chile (`es-CL`), Colombia (`es-CO`), Costa Rica (`es-CR`), Dominican Republic (`es-DO`), Ecuador (`es-EC`), Spain (`es-ES`), Guatemala (`es-GT`), Honduras (`es-HN`), Mexico (`es-MX`), Nicaragua (`es-NI`), Panama (`es-PA`), Peru (`es-PE`), Puerto Rico (`es-PR`), Paraguay (`es-PY`), El Salvador (`es-SV`), United States (`es-US`), Uruguay (`es-UY`), Venezuela (`es-VE`)|


### Supported document fields

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`CustomerName`|`string`|Customer being invoiced|Microsoft Corp|
|`CustomerId`|`string`|Reference ID for the customer|CID-12345|
|`PurchaseOrder`|`string`|A purchase order reference number|PO-3333|
|`InvoiceId`|`string`|ID for this specific invoice (often 'Invoice Number')|INV-100|
|`InvoiceDate`|`date`|Date the invoice was issued|11/15/2019|
|`DueDate`|`date`|Date payment for this invoice is due|12/15/2019|
|`VendorName`|`string`|Vendor who has created this invoice|CONTOSO LTD.|
|`VendorAddress`|`address`|Mailing address for the Vendor|123 456th St, New York, NY 10001|
|`VendorAddressRecipient`|`string`|Name associated with the VendorAddress|Contoso Headquarters|
|`CustomerAddress`|`address`|Mailing address for the Customer|123 Other St, Redmond WA, 98052|
|`CustomerAddressRecipient`|`string`|Name associated with the CustomerAddress|Microsoft Corp|
|`BillingAddress`|`address`|Explicit billing address for the customer|123 Bill St, Redmond WA, 98052|
|`BillingAddressRecipient`|`string`|Name associated with the BillingAddress|Microsoft Services|
|`ShippingAddress`|`address`|Explicit shipping address for the customer|123 Ship St, Redmond WA, 98052|
|`ShippingAddressRecipient`|`string`|Name associated with the ShippingAddress|Microsoft Delivery|
|`SubTotal`|`currency`|Subtotal field identified on this invoice|$100.00|
|`TotalDiscount`|`currency`|Total discount field identified on this invoice|$5.00|
|`TotalTax`|`currency`|Total tax field identified on this invoice|$10.00|
|`InvoiceTotal`|`currency`|Total new charges associated with this invoice|$110.00|
|`AmountDue`|`currency`|Total Amount Due to the vendor|$610.00|
|`PreviousUnpaidBalance`|`currency`|Explicit previously unpaid balance|$500.00|
|`RemittanceAddress`|`address`|Explicit remittance or payment address for the customer|123 Remit St New York, NY, 10001|
|`RemittanceAddressRecipient`|`string`|Name associated with the RemittanceAddress|Contoso Billing|
|`ServiceAddress`|`address`|Explicit service address or property address for the customer|123 Service St, Redmond WA, 98052|
|`ServiceAddressRecipient`|`string`|Name associated with the ServiceAddress|Microsoft Services|
|`ServiceStartDate`|`date`|First date for the service period (for example, a utility bill service period)|10/14/2019|
|`ServiceEndDate`|`date`|End date for the service period (for example, a utility bill service period)|11/14/2019|
|`VendorTaxId`|`string`|The government ID number associated with the vendor|123456-7|
|`CustomerTaxId`|`string`|The government ID number associated with the customer|765432-1|
|`PaymentTerm`|`string`|The terms under which the payment is meant to be paid|Net90|
|`KVKNumber`|`string`|A unique identifier for businesses registered in the Netherlands|12345678|
|`PaymentDetails`|`array`|List of payment details||
|`PaymentDetails.*`|`object`|A single payment detail||
|`PaymentDetails.*.IBAN`|`string`|International bank account number|DE 94 700 700 100 029 49 00 00|
|`PaymentDetails.*.SWIFT`|`string`|ISO9362, an international standard for Business Identifier Codes (BIC)|DEUTDEMMXXX|
|`PaymentDetails.*.BankAccountNumber`|`string`|Bank account number, a unique identifier for a bank account|123456|
|`PaymentDetails.*.BPayBillerCode`|`string`|Biller code for BPay, an alphanumeric identifier unique to a biller or their product/service|123456|
|`PaymentDetails.*.BPayReference`|`string`|Reference number for BPay, a unique identifier for a specific customer's bill transaction|1234567|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail||
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|29,520.00|
|`TaxDetails.*.Rate`|`string`|The rate of the tax detail|18 %|
|`PaidInFourInstallements`|`array`|List of tax details||
|`PaidInFourInstallements.*`|`object`|A single tax detail||
|`PaidInFourInstallements.*.Amount`|`currency`|The installement amount due|29,520.00|
|`PaidInFourInstallements.*.DueDate`|`date`|The installement due date|2024/01/01|
|`Items`|`array`|List of line items||
|`Items.*`|`object`|A single line item|3/4/2021<br>A123<br>Consulting Services<br>2 hours<br>$30.00<br>10%<br>$60.00|
|`Items.*.Amount`|`currency`|The amount of the line item|$60.00|
|`Items.*.Date`|`date`|Date corresponding to each line item. Often it is a date the line item was shipped|3/4/2021|
|`Items.*.Description`|`string`|The text description for the invoice line item|Consulting service|
|`Items.*.Quantity`|`number`|The quantity for this invoice line item|2|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.Tax`|`currency`|Tax associated with each line item. Possible values include tax amount, tax %, and tax Y/N|$6.00|
|`Items.*.TaxRate`|`string`|Tax rate associated with each line item|18 %|
|`Items.*.Unit`|`string`|The unit of the line item, e.g, kg, lb etc.|hours|
|`Items.*.UnitPrice`|`currency`|The net or gross price (depending on the gross invoice setting of the invoice) of one unit of this item|$30.00|
