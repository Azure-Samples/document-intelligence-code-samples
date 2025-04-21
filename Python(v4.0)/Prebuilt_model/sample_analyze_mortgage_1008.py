# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Mortgage 1008 operations with the Azure AI Document Intelligence client library. 
The async versions of the samples require Python 3.8 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
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
        "prebuilt-mortgage.us.1008", body=f
    )
mortgage1008 = poller.result()

for idx, document in enumerate(mortgage1008.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    # Document Type
    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    # Borrower Details
    borrower = document.fields.get("Borrower")
    if borrower:
        print("Borrower Details:")
        borrower_name = borrower.value_object.get("Name")
        if borrower_name:
            print(
                "...Borrower Name: {} has confidence: {}".format(
                    borrower_name.value_string, borrower_name.confidence
                )
            )

        number_of_borrowers = borrower.value_object.get("NumberOfBorrowers")
        if number_of_borrowers:
            print(
                "...Number of Borrowers: {} has confidence: {}".format(
                    number_of_borrowers.value_integer, number_of_borrowers.confidence
                )
            )

    # Mortgage Details
    mortgage = document.fields.get("Mortgage")
    if mortgage:
        print("Mortgage Details:")
        broker_name = mortgage.value_object.get("BrokerOrCorrespondentNameAndCompanyName")
        if broker_name:
            print(
                "...Broker Name and Company: {} has confidence: {}".format(
                    broker_name.value_string, broker_name.confidence
                )
            )

        loan_amount = mortgage.value_object.get("LoanAmount")
        if loan_amount:
            print(
                "...Loan Amount: {} has confidence: {}".format(
                    loan_amount.value_number, loan_amount.confidence
                )
            )

        loan_term_months = mortgage.value_object.get("LoanTermInMonths")
        if loan_term_months:
            print(
                "...Loan Term in Months: {} has confidence: {}".format(
                    loan_term_months.value_number, loan_term_months.confidence
                )
            )

        note_rate = mortgage.value_object.get("NoteRatePercentage")
        if note_rate:
            print(
                "...Note Rate: {} has confidence: {}".format(
                    note_rate.value_number, note_rate.confidence
                )
            )

        loan_type = mortgage.value_object.get("LoanType")
        if loan_type:
            print(
                "...Loan Type: {} has confidence: {}".format(
                    loan_type.value_selection_group, loan_type.confidence
                )
            )

        amortization_type = mortgage.value_object.get("AmortizationType")
        if amortization_type:
            print(
                "...Amortization Type: {} has confidence: {}".format(
                    amortization_type.value_selection_group, amortization_type.confidence
                )
            )

        loan_purpose_type = mortgage.value_object.get("LoanPurposeType")
        if loan_purpose_type:
            print(
                "...Loan Purpose Type: {} has confidence: {}".format(
                    loan_purpose_type.value_selection_group, loan_purpose_type.confidence
                )
            )

        lien_position_type = mortgage.value_object.get("LienPositionType")
        if lien_position_type:
            print(
                "...Lien Position Type: {} has confidence: {}".format(
                    lien_position_type.value_selection_group, lien_position_type.confidence
                )
            )

        mortgage_originator_type = mortgage.value_object.get("MortgageOriginatorType")
        if mortgage_originator_type:
            print(
                "...Mortgage Originator Type: {} has confidence: {}".format(
                    mortgage_originator_type.value_selection_group, mortgage_originator_type.confidence
                )
            )

        temporary_buydown_status = mortgage.value_object.get("TemporaryBuydownStatus")
        if temporary_buydown_status:
            print(
                "...Temporary Buydown Status: {} has confidence: {}".format(
                    temporary_buydown_status.value_selection_group, temporary_buydown_status.confidence
                )
            )

    # Property Details
    property = document.fields.get("Property")
    if property:
        print("Property Details:")
        property_address = property.value_object.get("Address")
        if property_address:
            print(
                "...Property Address: {} has confidence: {}".format(
                    property_address.value_address, property_address.confidence
                )
            )

        appraised_value = property.value_object.get("AppraisedValue")
        if appraised_value:
            print(
                "...Appraised Value: {} has confidence: {}".format(
                    appraised_value.value_number, appraised_value.confidence
                )
            )

        sales_price = property.value_object.get("SalesPrice")
        if sales_price:
            print(
                "...Sales Price: {} has confidence: {}".format(
                    sales_price.value_number, sales_price.confidence
                )
            )

        occupancy_status = property.value_object.get("OccupancyStatus")
        if occupancy_status:
            print(
                "...Occupancy Status: {} has confidence: {}".format(
                    occupancy_status.value_selection_group, occupancy_status.confidence
                )
            )

        property_type = property.value_object.get("PropertyType")
        if property_type:
            print(
                "...Property Type: {} has confidence: {}".format(
                    property_type.value_selection_group, property_type.confidence
                )
            )

        freddie_mac_project_classification = property.value_object.get("FreddieMacProjectClassificationType")
        if freddie_mac_project_classification:
            print(
                "...Freddie Mac Project Classification: {} has confidence: {}".format(
                    freddie_mac_project_classification.value_selection_group, freddie_mac_project_classification.confidence
                )
            )

        fannie_mae_project_classification = property.value_object.get("FannieMaeProjectClassificationType")
        if fannie_mae_project_classification:
            print(
                "...Fannie Mae Project Classification: {} has confidence: {}".format(
                    fannie_mae_project_classification.value_selection_group, fannie_mae_project_classification.confidence
                )
            )

        property_rights_type = property.value_object.get("PropertyRightsType")
        if property_rights_type:
            print(
                "...Property Rights Type: {} has confidence: {}".format(
                    property_rights_type.value_selection_group, property_rights_type.confidence
                )
            )

    # Seller Details
    seller = document.fields.get("Seller")
    if seller:
        print("Seller Details:")
        seller_address = seller.value_object.get("Address")
        if seller_address:
            print(
                "...Seller Address: {} has confidence: {}".format(
                    seller_address.value_address, seller_address.confidence
                )
            )

        contact_name = seller.value_object.get("ContactName")
        if contact_name:
            print(
                "...Seller Contact Name: {} has confidence: {}".format(
                    contact_name.value_string, contact_name.confidence
                )
            )

        contact_phone_number = seller.value_object.get("ContactPhoneNumber")
        if contact_phone_number:
            print(
                "...Seller Contact Phone Number: {} has confidence: {}".format(
                    contact_phone_number.value_phone_number, contact_phone_number.confidence
                )
            )

        loan_number = seller.value_object.get("LoanNumber")
        if loan_number:
            print(
                "...Loan Number: {} has confidence: {}".format(
                    loan_number.value_string, loan_number.confidence
                )
            )

        seller_name = seller.value_object.get("Name")
        if seller_name:
            print(
                "...Seller Name: {} has confidence: {}".format(
                    seller_name.value_string, seller_name.confidence
                )
            )

    # Underwriting Details
    underwriting = document.fields.get("Underwriting")
    if underwriting:
        print("Underwriting Details:")
        appraisal_company_name = underwriting.value_object.get("AppraisalCompanyName")
        if appraisal_company_name:
            print(
                "...Appraisal Company Name: {} has confidence: {}".format(
                    appraisal_company_name.value_string, appraisal_company_name.confidence
                )
            )

        appraiser_name_license = underwriting.value_object.get("AppraiserNameAndLicenseNumber")
        if appraiser_name_license:
            print(
                "...Appraiser Name and License Number: {} has confidence: {}".format(
                    appraiser_name_license.value_string, appraiser_name_license.confidence
                )
            )

        funds_required_to_close = underwriting.value_object.get("FundsRequiredToClose")
        if funds_required_to_close:
            print(
                "...Funds Required to Close: {} has confidence: {}".format(
                    funds_required_to_close.value_number, funds_required_to_close.confidence
                )
            )

        proposed_monthly_payment_total = underwriting.value_object.get("ProposedMonthlyPaymentTotal")
        if proposed_monthly_payment_total:
            print(
                "...Proposed Monthly Payment Total: {} has confidence: {}".format(
                    proposed_monthly_payment_total.value_number, proposed_monthly_payment_total.confidence
                )
            )

        rate_used_for_qualifying = underwriting.value_object.get("RateUsedForQualifying")
        if rate_used_for_qualifying:
            print(
                "...Rate Used for Qualifying: {} has confidence: {}".format(
                    rate_used_for_qualifying.value_number, rate_used_for_qualifying.confidence
                )
            )

        total_borrower_income = underwriting.value_object.get("TotalBorrowerIncome")
        if total_borrower_income:
            print(
                "...Total Borrower Income: {} has confidence: {}".format(
                    total_borrower_income.value_number, total_borrower_income.confidence
                )
            )

        underwriter_name = underwriting.value_object.get("UnderwriterName")
        if underwriter_name:
            print(
                "...Underwriter Name: {} has confidence: {}".format(
                    underwriter_name.value_string, underwriter_name.confidence
                )
            )

        verified_assets_amount = underwriting.value_object.get("VerifiedAssetsAmount")
        if verified_assets_amount:
            print(
                "...Verified Assets Amount: {} has confidence: {}".format(
                    verified_assets_amount.value_number, verified_assets_amount.confidence
                )
            )

        qualifying_rate_type = underwriting.value_object.get("QualifyingRateType")
        if qualifying_rate_type:
            print(
                "...Qualifying Rate Type: {} has confidence: {}".format(
                    qualifying_rate_type.value_selection_group, qualifying_rate_type.confidence
                )
            )
