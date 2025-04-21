# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Pay Stubs operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from dotenv import find_dotenv, load_dotenv

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""

load_dotenv(find_dotenv())

endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]
filepath = "YOUR_FILE_PATH"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open(filepath, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-payStub.us", body=f
    )
paystubs = poller.result()

for idx, document in enumerate(paystubs.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))
    
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))
    
    employee_name = document.fields.get("EmployeeName")
    if employee_name:
        print(
            "Employee Name: {} has confidence: {}".format(
                employee_name.value_string, employee_name.confidence
            )
        )
    
    employee_address = document.fields.get("EmployeeAddress")
    if employee_address:
        print(
            "Employee Address: {} has confidence: {}".format(
                employee_address.value_address, employee_address.confidence
            )
        )
    
    employee_ssn = document.fields.get("EmployeeSSN")
    if employee_ssn:
        print(
            "Employee SSN: {} has confidence: {}".format(
                employee_ssn.value_string, employee_ssn.confidence
            )
        )
    
    employer_name = document.fields.get("EmployerName")
    if employer_name:
        print(
            "Employer Name: {} has confidence: {}".format(
                employer_name.value_string, employer_name.confidence
            )
        )
    
    employer_address = document.fields.get("EmployerAddress")
    if employer_address:
        print(
            "Employer Address: {} has confidence: {}".format(
                employer_address.value_address, employer_address.confidence
            )
        )
    
    pay_date = document.fields.get("PayDate")
    if pay_date:
        print(
            "Pay Date: {} has confidence: {}".format(
                pay_date.value_date, pay_date.confidence
            )
        )
    
    pay_period_start = document.fields.get("PayPeriodStartDate")
    if pay_period_start:
        print(
            "Pay Period Start Date: {} has confidence: {}".format(
                pay_period_start.value_date, pay_period_start.confidence
            )
        )
    
    pay_period_end = document.fields.get("PayPeriodEndDate")
    if pay_period_end:
        print(
            "Pay Period End Date: {} has confidence: {}".format(
                pay_period_end.value_date, pay_period_end.confidence
            )
        )
    
    current_gross_pay = document.fields.get("CurrentPeriodGrossPay")
    if current_gross_pay:
        print(
            "Current Period Gross Pay: {} has confidence: {}".format(
                current_gross_pay.value_number, current_gross_pay.confidence
            )
        )
    
    current_taxes = document.fields.get("CurrentPeriodTaxes")
    if current_taxes:
        print(
            "Current Period Taxes: {} has confidence: {}".format(
                current_taxes.value_number, current_taxes.confidence
            )
        )
    
    current_deductions = document.fields.get("CurrentPeriodDeductions")
    if current_deductions:
        print(
            "Current Period Deductions: {} has confidence: {}".format(
                current_deductions.value_number, current_deductions.confidence
            )
        )
    
    current_net_pay = document.fields.get("CurrentPeriodNetPay")
    if current_net_pay:
        print(
            "Current Period Net Pay: {} has confidence: {}".format(
                current_net_pay.value_number, current_net_pay.confidence
            )
        )
    
    ytd_gross_pay = document.fields.get("YearToDateGrossPay")
    if ytd_gross_pay:
        print(
            "Year-To-Date Gross Pay: {} has confidence: {}".format(
                ytd_gross_pay.value_number, ytd_gross_pay.confidence
            )
        )
    
    ytd_taxes = document.fields.get("YearToDateTaxes")
    if ytd_taxes:
        print(
            "Year-To-Date Taxes: {} has confidence: {}".format(
                ytd_taxes.value_number, ytd_taxes.confidence
            )
        )
    
    ytd_deductions = document.fields.get("YearToDateDeductions")
    if ytd_deductions:
        print(
            "Year-To-Date Deductions: {} has confidence: {}".format(
                ytd_deductions.value_number, ytd_deductions.confidence
            )
        )
    
    ytd_net_pay = document.fields.get("YearToDateNetPay")
    if ytd_net_pay:
        print(
            "Year-To-Date Net Pay: {} has confidence: {}".format(
                ytd_net_pay.value_number, ytd_net_pay.confidence
            )
        )
    
    print("--------------------------------------")
