# Document Intelligence receipt model

## 2024-07-31-preview

### Supported languages

#### Thermal receipts (retail, meal, parking, etc.)

| Language name | Language code | Language name | Language code |
|:--------------|:-------------:|:--------------|:-------------:|
|English|``en``|Malagasy|`mg`|
|Afrikaans|``af``|Malay|`ms`|
|Akan|``ak``|Maltese|`mt`|
|Albanian|``sq``|Maori|`mi`|
|Arabic|``ar``|Marathi|`mr`|
|Azerbaijani|``az``|Maya, Yucatán|`yua`|
|Bambara|``bm``|Mongolian|`mn`|
|Basque|``eu``|Nepali|`ne`|
|Belarusian|``be``|Northern Sotho|`nso`|
|Bhojpuri|``bho``|Norwegian|`no`|
|Bosnian|``bs``|Nyanja|`ny`|
|Bulgarian|``bg``|Oromo|`om`|
|Catalan|``ca``|Pashto|`ps`|
|Cebuano|``ceb``|Persian|`fa`|
|Corsican|``co``|Persian (Dari)|`prs`|
|Croatian|``hr``|Polish|`pl`|
|Czech|``cs``|Portuguese|`pt`|
|Danish|``da``|Punjabi|`pa`|
|Dutch|``nl``|Quechua|`qu`|
|Estonian|``et``|Romanian|`ro`|
|Faroese|``fo``|Russian|`ru`|
|Fijian|``fj``|Samoan|`sm`|
|Filipino|``fil``|Sanskrit|`sa`|
|Finnish|``fi``|Scottish Gaelic|`gd`|
|French|``fr``|Serbian (Cyrillic)|`sr-cyrl`|
|Galician|``gl``|Serbian (Latin)|`sr-latn`|
|Ganda|``lg``|Shona|`sn`|
|German|``de``|Slovak|`sk`|
|Greek|``el``|Slovenian|`sl`|
|Guarani|``gn``|Somali (Latin)|`so-latn`|
|Haitian Creole|``ht``|Southern Sotho|`st`|
|Hawaiian|``haw``|Spanish|`es`|
|Hebrew|``he``|Sundanese|`su`|
|Hindi|``hi``|Swahili|`sw`|
|Hmong Daw|``mww``|Swedish|`sv`|
|Hungarian|``hu``|Tahitian|`ty`|
|Icelandic|``is``|Tajik|`tg`|
|Igbo|``ig``|Tamil|`ta`|
|Iloko|``ilo``|Tatar|`tt`|
|Indonesian|``id``|Tatar (Latin)|`tt-latn`|
|Irish|``ga``|Thai|`th`|
|Italian|``it``|Tongan|`to`|
|Japanese|``ja``|Tsonga|`ts`|
|Javanese|``jv``|Turkish|`tr`|
|Kazakh|``kk``|Turkmen|`tk`|
|Kazakh (Latin)|``kk-latn``|Ukrainian|`uk`|
|Kinyarwanda|``rw``|Upper Sorbian|`hsb`|
|Korean|``ko``|Uyghur|`ug`|
|Kurdish|``ku``|Uyghur (Arabic)|`ug-arab`|
|Kurdish (Latin)|``ku-latn``|Uzbek|`uz`|
|Kyrgyz|``ky``|Uzbek (Latin)|`uz-latn`|
|Latin|``la``|Vietnamese|`vi`|
|Latvian|``lv``|Welsh|`cy`|
|Lingala|``ln``|Western Frisian|`fy`|
|Lithuanian|``lt``|Xhosa|`xh`|
|Luxembourgish|``lb``|Zulu|`zu`|
|Macedonian|``mk``|||
#### Hotel receipts

| Language name | Language code | Language name | Language code |
|:--------------|:-------------:|:--------------|:-------------:|
|English|``en``|Japanese|`ja`|
|French|``fr``|Portuguese|`pt`|
|German|``de``|Spanish|`es`|
|Italian|``it``|||

### Model ID

**prebuilt-receipt**

### Supported document fields

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
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $1.00 |
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
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
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $1.00 |
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
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
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $1.00 |
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
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
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $1.00 |
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
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
|`TaxDetails`|`array`|List of tax details||
|`TaxDetails.*`|`object`|A single tax detail|Sales Tax(10%) $1.00 |
|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$1.00|
#### receipt.hotel

| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
|`MerchantAddress`|`address`|Listed address of merchant|123 Main St Redmond WA 98052|
|`Total`|`currency`|Full transaction total of receipt|$14.34|
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
