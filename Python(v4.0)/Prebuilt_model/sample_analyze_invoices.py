# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt Invoice operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]

# sample document
formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/invoice_sample.jpg"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

poller = document_intelligence_client.begin_analyze_document(
    "prebuilt-invoice", AnalyzeDocumentRequest(url_source=formUrl)
)
invoices = poller.result()

for idx, invoice in enumerate(invoices.documents):
    print("--------Recognizing invoice #{}--------".format(idx + 1))
    vendor_name = invoice.fields.get("VendorName")
    if vendor_name:
        print(
            "Vendor Name: {} has confidence: {}".format(
                vendor_name.value_string, vendor_name.confidence
            )
        )
    vendor_address = invoice.fields.get("VendorAddress")
    if vendor_address:
        print(
            "Vendor Address: {} has confidence: {}".format(
                vendor_address.value_address, vendor_address.confidence
            )
        )
    vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
    if vendor_address_recipient:
        print(
            "Vendor Address Recipient: {} has confidence: {}".format(
                vendor_address_recipient.value_string, vendor_address_recipient.confidence
            )
        )
    customer_name = invoice.fields.get("CustomerName")
    if customer_name:
        print(
            "Customer Name: {} has confidence: {}".format(
                customer_name.value_string, customer_name.confidence
            )
        )
    customer_id = invoice.fields.get("CustomerId")
    if customer_id:
        print(
            "Customer Id: {} has confidence: {}".format(
                customer_id.value_string, customer_id.confidence
            )
        )
    customer_address = invoice.fields.get("CustomerAddress")
    if customer_address:
        print(
            "Customer Address: {} has confidence: {}".format(
                customer_address.value_address, customer_address.confidence
            )
        )
    customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
    if customer_address_recipient:
        print(
            "Customer Address Recipient: {} has confidence: {}".format(
                customer_address_recipient.value_string,
                customer_address_recipient.confidence,
            )
        )
    invoice_id = invoice.fields.get("InvoiceId")
    if invoice_id:
        print(
            "Invoice Id: {} has confidence: {}".format(
                invoice_id.value_string, invoice_id.confidence
            )
        )
    invoice_date = invoice.fields.get("InvoiceDate")
    if invoice_date:
        print(
            "Invoice Date: {} has confidence: {}".format(
                invoice_date.value_date, invoice_date.confidence
            )
        )
    invoice_total = invoice.fields.get("InvoiceTotal")
    if invoice_total:
        print(
            "Invoice Total: {} has confidence: {}".format(
                invoice_total.value_currency.amount, invoice_total.confidence
            )
        )
    due_date = invoice.fields.get("DueDate")
    if due_date:
        print(
            "Due Date: {} has confidence: {}".format(
                due_date.value_date, due_date.confidence
            )
        )
    purchase_order = invoice.fields.get("PurchaseOrder")
    if purchase_order:
        print(
            "Purchase Order: {} has confidence: {}".format(
                purchase_order.value_string, purchase_order.confidence
            )
        )
    billing_address = invoice.fields.get("BillingAddress")
    if billing_address:
        print(
            "Billing Address: {} has confidence: {}".format(
                billing_address.value_address, billing_address.confidence
            )
        )
    billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
    if billing_address_recipient:
        print(
            "Billing Address Recipient: {} has confidence: {}".format(
                billing_address_recipient.value_string,
                billing_address_recipient.confidence,
            )
        )
    shipping_address = invoice.fields.get("ShippingAddress")
    if shipping_address:
        print(
            "Shipping Address: {} has confidence: {}".format(
                shipping_address.value_address, shipping_address.confidence
            )
        )
    shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
    if shipping_address_recipient:
        print(
            "Shipping Address Recipient: {} has confidence: {}".format(
                shipping_address_recipient.value_string,
                shipping_address_recipient.confidence,
            )
        )
    print("Invoice items:")
    for idx, item in enumerate(invoice.fields.get("Items").value_array):
        print("...Item #{}".format(idx + 1))
        item_description = item.value_object.get("Description")
        if item_description:
            print(
                "......Description: {} has confidence: {}".format(
                    item_description.value_string, item_description.confidence
                )
            )
        item_quantity = item.value_object.get("Quantity")
        if item_quantity:
            print(
                "......Quantity: {} has confidence: {}".format(
                    item_quantity.value_number, item_quantity.confidence
                )
            )
        unit = item.value_object.get("Unit")
        if unit:
            print(
                "......Unit: {} has confidence: {}".format(
                    unit.value_number, unit.confidence
                )
            )
        unit_price = item.value_object.get("UnitPrice")
        if unit_price:
            print(
                "......Unit Price: {} has confidence: {}".format(
                    unit_price.value_currency.amount, unit_price.confidence
                )
            )
        product_code = item.value_object.get("ProductCode")
        if product_code:
            print(
                "......Product Code: {} has confidence: {}".format(
                    product_code.value_string, product_code.confidence
                )
            )
        item_date = item.value_object.get("Date")
        if item_date:
            print(
                "......Date: {} has confidence: {}".format(
                    item_date.value_date, item_date.confidence
                )
            )
        tax = item.value_object.get("Tax")
        if tax:
            print(
                "......Tax: {} has confidence: {}".format(tax.value_string, tax.confidence)
            )
        amount = item.value_object.get("Amount")
        if amount:
            print(
                "......Amount: {} has confidence: {}".format(
                    amount.value_currency.amount, amount.confidence
                )
            )
    subtotal = invoice.fields.get("SubTotal")
    if subtotal:
        print(
            "Subtotal: {} has confidence: {}".format(
                subtotal.value_currency.amount, subtotal.confidence
            )
        )
    total_tax = invoice.fields.get("TotalTax")
    if total_tax:
        print(
            "Total Tax: {} has confidence: {}".format(
                total_tax.value_currency.amount, total_tax.confidence
            )
        )
    previous_unpaid_balance = invoice.fields.get("PreviousUnpaidBalance")
    if previous_unpaid_balance:
        print(
            "Previous Unpaid Balance: {} has confidence: {}".format(
                previous_unpaid_balance.value_currency.amount, previous_unpaid_balance.confidence
            )
        )
    amount_due = invoice.fields.get("AmountDue")
    if amount_due:
        print(
            "Amount Due: {} has confidence: {}".format(
                amount_due.value_currency.amount, amount_due.confidence
            )
        )
    service_start_date = invoice.fields.get("ServiceStartDate")
    if service_start_date:
        print(
            "Service Start Date: {} has confidence: {}".format(
                service_start_date.value_date, service_start_date.confidence
            )
        )
    service_end_date = invoice.fields.get("ServiceEndDate")
    if service_end_date:
        print(
            "Service End Date: {} has confidence: {}".format(
                service_end_date.value_date, service_end_date.confidence
            )
        )
    service_address = invoice.fields.get("ServiceAddress")
    if service_address:
        print(
            "Service Address: {} has confidence: {}".format(
                service_address.value_address, service_address.confidence
            )
        )
    service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
    if service_address_recipient:
        print(
            "Service Address Recipient: {} has confidence: {}".format(
                service_address_recipient.value_string,
                service_address_recipient.confidence,
            )
        )
    remittance_address = invoice.fields.get("RemittanceAddress")
    if remittance_address:
        print(
            "Remittance Address: {} has confidence: {}".format(
                remittance_address.value_address, remittance_address.confidence
            )
        )
    remittance_address_recipient = invoice.fields.get("RemittanceAddressRecipient")
    if remittance_address_recipient:
        print(
            "Remittance Address Recipient: {} has confidence: {}".format(
                remittance_address_recipient.value_string,
                remittance_address_recipient.confidence,
            )
        )
    print("----------------------------------------")
