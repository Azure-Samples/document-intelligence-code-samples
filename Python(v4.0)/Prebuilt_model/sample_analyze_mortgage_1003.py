# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Mortgage 1003 operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-mortgage.us.1003", body=f
    )
mortgage1003 = poller.result()

for idx, document in enumerate(mortgage1003.documents):
    print("--------Recognizing document #{}--------".format(idx + 1))

    doc_type = document.doc_type
    if doc_type:
        print("Document Type: {}".format(doc_type))

    agency_case_number = document.fields.get("AgencyCaseNumber")
    if agency_case_number:
        print(
            "Agency Case Number: {} has confidence: {}".format(
                agency_case_number.value_string, agency_case_number.confidence
            )
        )

    borrowers = document.fields.get("Borrowers")
    if borrowers:
        for borrower_idx, borrower in enumerate(borrowers.value_array):
            print(
                "Borrower #{}: {} has confidence: {}".format(
                    borrower_idx + 1, borrower.value_string, borrower.confidence
                )
            )

            birth_date = borrower.value_object.get("BirthDate")
            if birth_date:
                print(
                    "...Birth Date: {} has confidence: {}".format(
                        birth_date.value_date, birth_date.confidence
                    )
                )

            cell_phone_number = borrower.value_object.get("CellPhoneNumber")
            if cell_phone_number:
                print(
                    "...Cell Phone Number: {} has confidence: {}".format(
                        cell_phone_number.value_phone_number, cell_phone_number.confidence
                    )
                )

            co_borrower_names = borrower.value_object.get("CoBorrowerNames")
            if co_borrower_names:
                print(
                    "...Co-Borrower Names: {} has confidence: {}".format(
                        co_borrower_names.value_string, co_borrower_names.confidence
                    )
                )

            num_borrowers = borrower.value_object.get("NumberOfBorrowers")
            if num_borrowers:
                print(
                    "...Number of Borrowers: {} has confidence: {}".format(
                        num_borrowers.value_integer, num_borrowers.confidence
                    )
                )

            current_address = borrower.value_object.get("CurrentAddress")
            if current_address:
                print(
                    "...Current Address: {} has confidence: {}".format(
                        current_address.value_address, current_address.confidence
                    )
                )

            current_employment = borrower.value_object.get("CurrentEmployment")
            
            if current_employment:
                print("...Current Employment:")
                does_not_apply = current_employment.value_object.get("DoesNotApply")
                if does_not_apply:
                    print(
                        "......Does Not Apply: {} has confidence: {}".format(
                            does_not_apply.value_boolean, does_not_apply.confidence
                        )
                    )

                employer_address = current_employment.value_object.get("EmployerAddress")
                if employer_address:
                    print(
                        "......Employer Address: {} has confidence: {}".format(
                            employer_address.value_address, employer_address.confidence
                        )
                    )

                employer_name = current_employment.value_object.get("EmployerName")
                if employer_name:
                    print(
                        "......Employer Name: {} has confidence: {}".format(
                            employer_name.value_string, employer_name.confidence
                        )
                    )

                employer_phone_number = current_employment.value_object.get("EmployerPhoneNumber")
                if employer_phone_number:
                    print(
                        "......Employer Phone Number: {} has confidence: {}".format(
                            employer_phone_number.value_phone_number, employer_phone_number.confidence
                        )
                    )

                gross_monthly_income_total = current_employment.value_object.get("GrossMonthlyIncomeTotal")
                if gross_monthly_income_total:
                    print(
                        "......Gross Monthly Income: {} has confidence: {}".format(
                            gross_monthly_income_total.value_number, gross_monthly_income_total.confidence
                        )
                    )

                position_or_title = current_employment.value_object.get("PositionOrTitle")
                if position_or_title:
                    print(
                        "......Position / Title: {} has confidence: {}".format(
                            position_or_title.value_string, position_or_title.confidence
                        )
                    )

                start_date = current_employment.value_object.get("StartDate")
                if start_date:
                    print(
                        "......Start Date: {} has confidence: {}".format(
                            start_date.value_date, start_date.confidence
                        )
                    )

            social_security_number = borrower.value_object.get("SocialSecurityNumber")
            if social_security_number:
                print(
                    "...Social Security Number: {} has confidence: {}".format(
                        social_security_number.value_string, social_security_number.confidence
                    )
                )

            number_of_dependents = borrower.value_object.get("NumberOfDependents")
            if number_of_dependents:
                print(
                    "...Number of Dependents: {} has confidence: {}".format(
                        number_of_dependents.value_integer, number_of_dependents.confidence
                    )
                )

            marital_status = borrower.value_object.get("MaritalStatus")
            if marital_status:
                print(
                    "...Marital Status: {} has confidence: {}".format(
                        marital_status.value_selection_group, marital_status.confidence
                    )
                )

    lender_loan_number = document.fields.get("LenderLoanNumber")
    if lender_loan_number:
        print(
            "Lender Loan Number: {} has confidence: {}".format(
                lender_loan_number.value_string, lender_loan_number.confidence
            )
        )

    loan = document.fields.get("Loan")
    
    if loan:
        print("Loan:")
        loan_amount = loan.value_object.get("Amount")
        if loan_amount:
            print(
                "...Loan Amount: {} has confidence: {}".format(
                    loan_amount.value_number, loan_amount.confidence
                )
            )

        purpose_type = loan.value_object.get("PurposeType")
        if purpose_type:
            print(
                "...Purpose Type: {} has confidence: {}".format(
                    purpose_type.value_selection_group, purpose_type.confidence
                )
            )

        refinance_program_type = loan.value_object.get("RefinanceProgramType")
        if refinance_program_type:
            print(
                "...Refinance Program Type: {} has confidence: {}".format(
                    refinance_program_type.value_selection_group, refinance_program_type.confidence
                )
            )

        refinance_type = loan.value_object.get("RefinanceType")
        if refinance_type:
            print(
                "...Refinance Type: {} has confidence: {}".format(
                    refinance_type.value_selection_group, refinance_type.confidence
                )
            )

    property = document.fields.get("Property")
    
    if property:
        print("Property:")
        address = property.value_object.get("Address")
        if address:
            print(
                "...Address: {} has confidence: {}".format(
                    address.value_address, address.confidence
                )
            )

        isFhaSecondaryResidence = property.value_object.get("IsFhaSecondaryResidence")
        if isFhaSecondaryResidence:
            print(
                "...isFhaSecondaryResidence: {} has confidence: {}".format(
                    isFhaSecondaryResidence.value_boolean, isFhaSecondaryResidence.confidence
                )
            )

        num_unit = property.value_object.get("NumberOfUnits")
        if num_unit:
            print(
                "...Number Of Units: {} has confidence: {}".format(
                    num_unit.value_integer, num_unit.confidence
                )
            )


        value = property.value_object.get("Value")
        if value:
            print(
                "...Value: {} has confidence: {}".format(
                    value.value_number, value.confidence
                )
            )

        manufactured_home = property.value_object.get("ManufacturedHome")
        if manufactured_home:
            print(
                "...Manufactured Home: {} has confidence: {}".format(
                    manufactured_home.value_selection_group, manufactured_home.confidence
                )
            )

        mixed_use_property = property.value_object.get("MixedUseProperty")
        if mixed_use_property:
            print(
                "...Mixed Use Property: {} has confidence: {}".format(
                    mixed_use_property.value_selection_group, mixed_use_property.confidence
                )
            )

        occupancy_status = property.value_object.get("OccupancyStatus")
        if occupancy_status:
            print(
                "...Occupancy Status: {} has confidence: {}".format(
                    occupancy_status.value_selection_group, occupancy_status.confidence
                )
            )

    print("--------------------------------------")
