# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Mortgage Closing Disclosure operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = os.environ["DOCUMENTINTELLIGENCE_ENDPOINT"]
key = os.environ["DOCUMENTINTELLIGENCE_API_KEY"]
filepath = "YOUR_FILE_PATH"

document_intelligence_client  = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

with open(filepath, "rb") as f:
    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-mortgage.us.closingDisclosure", body=f
    )
mortgage_closing = poller.result()

for idx, document in enumerate(mortgage_closing.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    # Document Type
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    # Applicant Confirmation Signature
    applicant_confirmation = document.fields.get("ApplicantConfirmReceiptSignature")
    if applicant_confirmation:
        print("Applicant Confirmation:")
        if applicant_confirmation:
            print(
                "...Applicant Signature: {} has confidence: {}".format(
                    applicant_confirmation.value_signature, applicant_confirmation.confidence
                )
            )

    # Closing Details
    closing = document.fields.get("Closing")
    if closing:
        print("Closing Details:")
        closing_date = closing.value_object.get("ClosingDate")
        if closing_date:
            print(
                "...Closing Date: {} has confidence: {}".format(
                    closing_date.value_date, closing_date.confidence
                )
            )

        disbursement_date = closing.value_object.get("DisbursementDate")
        if disbursement_date:
            print(
                "...Disbursement Date: {} has confidence: {}".format(
                    disbursement_date.value_date, disbursement_date.confidence
                )
            )

        file_number = closing.value_object.get("FileNumber")
        if file_number:
            print(
                "...File Number: {} has confidence: {}".format(
                    file_number.value_string, file_number.confidence
                )
            )

        issue_date = closing.value_object.get("IssueDate")
        if issue_date:
            print(
                "...Issue Date: {} has confidence: {}".format(
                    issue_date.value_date, issue_date.confidence
                )
            )

        property_address = closing.value_object.get("PropertyAddress")
        if property_address:
            print(
                "...Property Address: {} has confidence: {}".format(
                    property_address.value_address, property_address.confidence
                )
            )

        sale_price = closing.value_object.get("SalePrice")
        if sale_price:
            print(
                "...Sale Price: {} has confidence: {}".format(
                    sale_price.value_number, sale_price.confidence
                )
            )

        settlement_agent = closing.value_object.get("SettlementAgent")
        if settlement_agent:
            print(
                "...Settlement Agent: {} has confidence: {}".format(
                    settlement_agent.value_string, settlement_agent.confidence
                )
            )

    # Co-Applicant Confirmation Signature
    co_applicant_confirmation = document.fields.get("CoApplicantConfirmReceiptSignature")
    if co_applicant_confirmation:
        print("Co-Applicant Confirmation:")
        if co_applicant_confirmation:
            print(
                "...Co-Applicant Signature: {} has confidence: {}".format(
                    co_applicant_confirmation.value_signature, co_applicant_confirmation.confidence
                )
            )

    # Loan Details
    loan = document.fields.get("Loan")
    if loan:
        print("Loan Details:")
        loan_amount = loan.value_object.get("Amount")
        if loan_amount:
            print(
                "...Loan Amount: {} has confidence: {}".format(
                    loan_amount.value_number, loan_amount.confidence
                )
            )

        estimated_tax_insurance = loan.value_object.get("EstimatedTaxInsuranceAndAssessmentsPerMonth")
        if estimated_tax_insurance:
            print(
                "...Estimated Tax, Insurance, and Assessments per Month: {} has confidence: {}".format(
                    estimated_tax_insurance.value_number, estimated_tax_insurance.confidence
                )
            )

        identification_number = loan.value_object.get("IdentificationNumber")
        if identification_number:
            print(
                "...Identification Number: {} has confidence: {}".format(
                    identification_number.value_string, identification_number.confidence
                )
            )

        interest_rate = loan.value_object.get("InterestRate")
        if interest_rate:
            print(
                "...Interest Rate: {} has confidence: {}".format(
                    interest_rate.value_number, interest_rate.confidence
                )
            )

        monthly_principal_interest = loan.value_object.get("MonthlyPrincipalAndInterest")
        if monthly_principal_interest:
            print(
                "...Monthly Principal and Interest: {} has confidence: {}".format(
                    monthly_principal_interest.value_number, monthly_principal_interest.confidence
                )
            )

        mortgage_case_number = loan.value_object.get("MortgageInsuranceCaseNumber")
        if mortgage_case_number:
            print(
                "...Mortgage Insurance Case Number: {} has confidence: {}".format(
                    mortgage_case_number.value_string, mortgage_case_number.confidence
                )
            )

        product_type = loan.value_object.get("Product")
        if product_type:
            print(
                "...Loan Product Type: {} has confidence: {}".format(
                    product_type.value_string, product_type.confidence
                )
            )

        loan_purpose = loan.value_object.get("Purpose")
        if loan_purpose:
            print(
                "...Loan Purpose: {} has confidence: {}".format(
                    loan_purpose.value_string, loan_purpose.confidence
                )
            )

        loan_term = loan.value_object.get("Term")
        if loan_term:
            print(
                "...Loan Term: {} has confidence: {}".format(
                    loan_term.value_string, loan_term.confidence
                )
            )

        loan_type = loan.value_object.get("Type")
        if loan_type:
            print(
                "...Loan Type: {} has confidence: {}".format(
                    loan_type.value_selection_group, loan_type.confidence
                )
            )

    # Transaction Details
    transaction = document.fields.get("Transaction")
    if transaction:
        print("Transaction Details:")
        borrower_address = transaction.value_object.get("BorrowerAddress")
        if borrower_address:
            print(
                "...Borrower Address: {} has confidence: {}".format(
                    borrower_address.value_address, borrower_address.confidence
                )
            )

        borrower_cash_to_close = transaction.value_object.get("BorrowerCashToCloseAmount")
        if borrower_cash_to_close:
            print(
                "...Borrower Cash to Close: {} has confidence: {}".format(
                    borrower_cash_to_close.value_number, borrower_cash_to_close.confidence
                )
            )

        borrower_closing_costs = transaction.value_object.get("BorrowerClosingCosts")
        if borrower_closing_costs:
            print(
                "...Borrower Closing Costs: {} has confidence: {}".format(
                    borrower_closing_costs.value_number, borrower_closing_costs.confidence
                )
            )

        borrower_name = transaction.value_object.get("BorrowerName")
        if borrower_name:
            print(
                "...Borrower Name: {} has confidence: {}".format(
                    borrower_name.value_string, borrower_name.confidence
                )
            )

        lender_name = transaction.value_object.get("LenderName")
        if lender_name:
            print(
                "...Lender Name: {} has confidence: {}".format(
                    lender_name.value_string, lender_name.confidence
                )
            )

        seller_address = transaction.value_object.get("SellerAddress")
        if seller_address:
            print(
                "...Seller Address: {} has confidence: {}".format(
                    seller_address.value_address, seller_address.confidence
                )
            )

        seller_cash_to_close = transaction.value_object.get("SellerCashToCloseAmount")
        if seller_cash_to_close:
            print(
                "...Seller Cash to Close: {} has confidence: {}".format(
                    seller_cash_to_close.value_number, seller_cash_to_close.confidence
                )
            )

        seller_name = transaction.value_object.get("SellerName")
        if seller_name:
            print(
                "...Seller Name: {} has confidence: {}".format(
                    seller_name.value_string, seller_name.confidence
                )
            )

        borrower_cash_to_close_type = transaction.value_object.get("BorrowerCashToCloseType")
        if borrower_cash_to_close_type:
            print(
                "...Borrower Cash to Close Type: {} has confidence: {}".format(
                    borrower_cash_to_close_type.value_selection_group, borrower_cash_to_close_type.confidence
                )
            )

        seller_cash_to_close_type = transaction.value_object.get("SellerCashToCloseType")
        if seller_cash_to_close_type:
            print(
                "...Seller Cash to Close Type: {} has confidence: {}".format(
                    seller_cash_to_close_type.value_selection_group, seller_cash_to_close_type.confidence
                )
            )
