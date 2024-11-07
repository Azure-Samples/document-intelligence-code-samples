# Document Intelligence receipt model

## 2024-11-30 (GA)

### Supported languages

#### Thermal receipts (retail, meal, parking, etc.)

| Language name | Language code | Language name | Language code |
|:--------------|:-------------:|:--------------|:-------------:|
|English|``en``|Lithuanian|`lt`|
|Afrikaans|``af``|Luxembourgish|`lb`|
|Akan|``ak``|Macedonian|`mk`|
|Albanian|``sq``|Malagasy|`mg`|
|Arabic|``ar``|Malay|`ms`|
|Azerbaijani|``az``|Maltese|`mt`|
|Bamanankan|``bm``|Māori|`mi`|
|Basque|``eu``|Marathi|`mr`|
|Belarusian|``be``|Maya, Yucatán|`yua`|
|Bhojpuri|``bho``|Mongolian|`mn`|
|Bosnian|``bs``|Nepali|`ne`|
|Bulgarian|``bg``|Norwegian|`no`|
|Catalan|``ca``|Nyanja|`ny`|
|Cebuano|``ceb``|Oromo|`om`|
|Corsican|``co``|Pashto|`ps`|
|Croatian|``hr``|Persian|`fa`|
|Czech|``cs``|Persian (Dari)|`prs`|
|Danish|``da``|Polish|`pl`|
|Dutch|``nl``|Portuguese|`pt`|
|Estonian|``et``|Punjabi|`pa`|
|Faroese|``fo``|Quechua|`qu`|
|Fijian|``fj``|Romanian|`ro`|
|Filipino|``fil``|Russian|`ru`|
|Finnish|``fi``|Samoan|`sm`|
|French|``fr``|Sanskrit|`sa`|
|Galician|``gl``|Scottish Gaelic|`gd`|
|Ganda|``lg``|Serbian (Cyrillic)|`sr-cyrl`|
|German|``de``|Serbian (Latin)|`sr-latn`|
|Greek|``el``|Sesotho|`st`|
|Guarani|``gn``|Sesotho sa Leboa|`nso`|
|Haitian Creole|``ht``|Shona|`sn`|
|Hawaiian|``haw``|Slovak|`sk`|
|Hebrew|``he``|Slovenian|`sl`|
|Hindi|``hi``|Somali (Latin)|`so-latn`|
|Hmong Daw|``mww``|Spanish|`es`|
|Hungarian|``hu``|Sundanese|`su`|
|Icelandic|``is``|Swedish|`sv`|
|Igbo|``ig``|Tahitian|`ty`|
|Iloko|``ilo``|Tajik|`tg`|
|Indonesian|``id``|Tamil|`ta`|
|Irish|``ga``|Tatar|`tt`|
|isiXhosa|``xh``|Tatar (Latin)|`tt-latn`|
|isiZulu|``zu``|Thai|`th`|
|Italian|``it``|Tongan|`to`|
|Japanese|``ja``|Turkish|`tr`|
|Javanese|``jv``|Turkmen|`tk`|
|Kazakh|``kk``|Ukrainian|`uk`|
|Kazakh (Latin)|``kk-latn``|Upper Sorbian|`hsb`|
|Kinyarwanda|``rw``|Uyghur|`ug`|
|Kiswahili|``sw``|Uyghur (Arabic)|`ug-arab`|
|Korean|``ko``|Uzbek|`uz`|
|Kurdish|``ku``|Uzbek (Latin)|`uz-latn`|
|Kurdish (Latin)|``ku-latn``|Vietnamese|`vi`|
|Kyrgyz|``ky``|Welsh|`cy`|
|Latin|``la``|Western Frisian|`fy`|
|Latvian|``lv``|Xitsonga|`ts`|
|Lingala|``ln``|||

#### Hotel receipts

| Language name | Language code | Language name | Language code |
|:--------------|:-------------:|:--------------|:-------------:|
|English|``en``|Japanese|`ja`|
|French|``fr``|Portuguese|`pt`|
|German|``de``|Spanish|`es`|
|Italian|``it``|||

### Supported document fields

#### receipt

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
|`Subtotal`|`currency`|Subtotal of receipt, often before taxes are applied|$12.34|
|`TotalTax`|`currency`|Tax on receipt, often sales tax or equivalent|$2.00|
|`Tip`|`currency`|Tip included by buyer|$1.00|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Surface Pro 6|
|`Items.*.Quantity`|`number`|Quantity of each item|1|
|`Items.*.Price`|`currency`|Individual price of each item unit|$999.00|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Supplies|
|`Payments`|`array`|||
|`Payments.*`|`object`|Extracted payment|Cash $14.34|
|`Payments.*.Method`|`string`|Method of payment|Cash|
|`Payments.*.Amount`|`currency`|Amount of payment|$14.34|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|

#### receipt.retailMeal

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
|`Subtotal`|`currency`|Subtotal of receipt, often before taxes are applied|$12.34|
|`TotalTax`|`currency`|Tax on receipt, often sales tax or equivalent|$2.00|
|`Tip`|`currency`|Tip included by buyer|$1.00|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Surface Pro 6|
|`Items.*.Quantity`|`number`|Quantity of each item|1|
|`Items.*.Price`|`currency`|Individual price of each item unit|$999.00|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Meal|
|`Payments`|`array`|||
|`Payments.*`|`object`|Extracted payment|Cash $14.34|
|`Payments.*.Method`|`string`|Method of payment|Cash|
|`Payments.*.Amount`|`currency`|Amount of payment|$14.34|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|

#### receipt.creditCard

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
|`Subtotal`|`currency`|Subtotal of receipt, often before taxes are applied|$12.34|
|`TotalTax`|`currency`|Tax on receipt, often sales tax or equivalent|$2.00|
|`Tip`|`currency`|Tip included by buyer|$1.00|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Surface Pro 6|
|`Items.*.Quantity`|`number`|Quantity of each item|1|
|`Items.*.Price`|`currency`|Individual price of each item unit|$999.00|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Other|
|`Payments`|`array`|||
|`Payments.*`|`object`|Extracted payment|Cash $14.34|
|`Payments.*.Method`|`string`|Method of payment|Cash|
|`Payments.*.Amount`|`currency`|Amount of payment|$14.34|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|

#### receipt.gas

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
|`Subtotal`|`currency`|Subtotal of receipt, often before taxes are applied|$12.34|
|`TotalTax`|`currency`|Tax on receipt, often sales tax or equivalent|$2.00|
|`Tip`|`currency`|Tip included by buyer|$1.00|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Surface Pro 6|
|`Items.*.Quantity`|`number`|Quantity of each item|1|
|`Items.*.Price`|`currency`|Individual price of each item unit|$999.00|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Fuel&Energy.Gas|
|`Payments`|`array`|||
|`Payments.*`|`object`|Extracted payment|Cash $14.34|
|`Payments.*.Method`|`string`|Method of payment|Cash|
|`Payments.*.Amount`|`currency`|Amount of payment|$14.34|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|

#### receipt.parking

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
|`Subtotal`|`currency`|Subtotal of receipt, often before taxes are applied|$12.34|
|`TotalTax`|`currency`|Tax on receipt, often sales tax or equivalent|$2.00|
|`Tip`|`currency`|Tip included by buyer|$1.00|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Surface Pro 6|
|`Items.*.Quantity`|`number`|Quantity of each item|1|
|`Items.*.Price`|`currency`|Individual price of each item unit|$999.00|
|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Transportation.Parking|
|`Payments`|`array`|||
|`Payments.*`|`object`|Extracted payment|Cash $14.34|
|`Payments.*.Method`|`string`|Method of payment|Cash|
|`Payments.*.Amount`|`currency`|Amount of payment|$14.34|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|

#### receipt.hotel

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
|`Balance`|`currency`|Balance due on receipt|$0.00|
|`ArrivalDate`|`date`|Date of arrival|27Mar21|
|`DepartureDate`|`date`|Date of departure|28Mar21|
|`MerchantAliases`|`array`|||
|`MerchantAliases.*`|`string`|Alternative name of merchant|Contoso (R)|
|`Items`|`array`|||
|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
|`Items.*.TotalPrice`|`currency`|Total price of line item|$999.00|
|`Items.*.Description`|`string`|Item description|Room Charge|
|`Items.*.Date`|`date`|Item date|27Mar21|
|`Items.*.Category`|`string`|Item category|Room|
|`CountryRegion`|`countryRegion`|Country or region where the receipt was issued|USA|
|`ReceiptType`|`string`|Type of receipt|Hotel|
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $10.00 $1.00 $11.00|
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|
|`TaxDetails.*.Rate`|`number`|The rate of the tax detail|10%|
|`TaxDetails.*.NetAmount`|`currency`|The net amount before tax.|$10.00|
|`TaxDetails.*.Description`|`string`|The description of the tax detail|Sales Tax|
