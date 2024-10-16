# Document Intelligence credit card model

## 2024-07-31-preview

### Model ID

**prebuilt-creditCard**

### Supported document fields


| Field | Type | Description | Example |
|:------|:-----|:------------|:--------|
|`CardNumber`|`string`|A unique identifier for the card|4275 0000 0000 0000|
|`IssuingBank`|`string`|The name of the bank that issued the card|Woodgrove Bank|
|`PaymentNetwork`|`string`|The payment network that processes the card transactions|VISA|
|`CardHolderName`|`string`|The name of the person who owns the card|JOHN SMITH|
|`CardHolderCompanyName`|`string`|The name of the company that the card is associated with|CONTOSO SOFTWARE|
|`ValidDate`|`date`|Valid from date|01/16|
|`ExpirationDate`|`date`|Expiration date|01/19|
|`CardVerificationValue`|`string`|Card verification value (CVV)|764|
|`CustomerServicePhoneNumbers`|`array`|||
|`CustomerServicePhoneNumbers.*`|`phoneNumber`|A phone number that can be used to contact the customer service of the issuing bank or the card network|+1 (987) 123-4567|
