# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_analyze_tax_us_w2.py

DESCRIPTION:
    This sample demonstrates how to analyze US W-2 tax forms.

    See fields found on a US W-2 tax form here:
    https://aka.ms/V3.1-w-2-field-schema

PREREQUISITES:
    The following prerequisites are necessary to run the code. For more details, please visit the "How-to guides" link: https://aka.ms/How-toguides

    -------Python and IDE------
    1) Install Python 3.7 or later (https://www.python.org/), which should include pip (https://pip.pypa.io/en/stable/).
    2) Install the latest version of Visual Studio Code (https://code.visualstudio.com/) or your preferred IDE. 
    
    ------Azure AI services or Document Intelligence resource------ 
    Create a single-service (https://aka.ms/single-service) or multi-service (https://aka.ms/multi-service) resource.
    You can use the free pricing tier (F0) to try the service and upgrade to a paid tier for production later.
    
    ------Get the key and endpoint------
    1) After your resource is deployed, select "Go to resource". 
    2) In the left navigation menu, select "Keys and Endpoint". 
    3) Copy one of the keys and the Endpoint for use in this sample. 
    
    ------Set your environment variables------
    At a command prompt, run the following commands, replacing <yourKey> and <yourEndpoint> with the values from your resource in the Azure portal.
    1) For Windows:
       setx DI_KEY <yourKey>
       setx DI_ENDPOINT <yourEndpoint>
       • Close the Command Prompt window after you set your environment variables. Restart any running programs that read the environment variable.
    2) For macOS:
       export key=<yourKey>
       export endpoint=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/V3.1-set-environment-variables-for-macOS
    3) For Linux:
       export DI_KEY=<yourKey>
       export DI_ENDPOINT=<yourEndpoint>
       • This is a temporary environment variable setting method that only lasts until you close the terminal session. 
       • To set an environment variable permanently, visit: https://aka.ms/V3.1-set-environment-variables-for-Linux
       
    ------Set up your programming environment------
    At a command prompt,run the following code to install the Azure AI Document Intelligence client library for Python with pip:
    pip install azure-ai-formrecognizer==3.3.0
    
    ------Create your Python application------
    1) Create a new Python file called "sample_analyze_tax_us_w2.py" in an editor or IDE.
    2) Open the "sample_analyze_read.py" file and insert the provided code sample into your application.
    3) At a command prompt, use the following code to run the Python code: 
    python sample_analyze_tax_us_w2.py
"""

import os


def format_address_value(address_value):
    return f"\n......House/building number: {address_value.house_number}\n......Road: {address_value.road}\n......City: {address_value.city}\n......State: {address_value.state}\n......Postal code: {address_value.postal_code}"


def analyze_tax_us_w2():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.formrecognizer import DocumentAnalysisClient

    # For how to obtain the endpoint and key, please see PREREQUISITES above.
    endpoint = os.environ["DI_ENDPOINT"]
    key = os.environ["DI_KEY"]

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Analyze a document at a URL:
    url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/w2.png"
    # Replace with your actual url:
    # If you use the URL of a public website, to find more URLs, please visit: https://aka.ms/V3.1-more-URLs 
    # If you analyze a document in Blob Storage, you need to generate Public SAS URL, please visit: https://aka.ms/create-sas-tokens
    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-tax.us.w2", document_url=url, locale="en-US"
    )

    # # If analyzing a local document, remove the comment markers (#) at the beginning of these 8 lines.
    # # Delete or comment out the part of "Analyze a document at a URL" above.
    # # Replace <path to your sample file>  with your actual file path.
    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_analysis_client.begin_analyze_document(
    #         "prebuilt-tax.us.w2", document=f, locale="en-US"
    #     )
    w2s = poller.result()

    # [START analyze_tax_us_w2]
    for idx, w2 in enumerate(w2s.documents):
        print(f"--------Analyzing US Tax W-2 Form #{idx + 1}--------")
        form_variant = w2.fields.get("W2FormVariant")
        if form_variant:
            print(
                f"Form variant: {form_variant.value} has confidence: "
                f"{form_variant.confidence}"
            )
        tax_year = w2.fields.get("TaxYear")
        if tax_year:
            print(f"Tax year: {tax_year.value} has confidence: {tax_year.confidence}")
        w2_copy = w2.fields.get("W2Copy")
        if w2_copy:
            print(f"W-2 Copy: {w2_copy.value} has confidence: {w2_copy.confidence}")
        employee = w2.fields.get("Employee")
        if employee:
            print("Employee data:")
            employee_name = employee.value.get("Name")
            if employee_name:
                print(
                    f"...Name: {employee_name.value} has confidence: {employee_name.confidence}"
                )
            employee_ssn = employee.value.get("SocialSecurityNumber")
            if employee_ssn:
                print(
                    f"...SSN: {employee_ssn.value} has confidence: {employee_ssn.confidence}"
                )
            employee_address = employee.value.get("Address")
            if employee_address:
                print(f"...Address: {format_address_value(employee_address.value)}")
                print(f"......has confidence: {employee_address.confidence}")
            employee_zipcode = employee.value.get("ZipCode")
            if employee_zipcode:
                print(
                    f"...Zipcode: {employee_zipcode.value} has confidence: "
                    f"{employee_zipcode.confidence}"
                )
        control_number = w2.fields.get("ControlNumber")
        if control_number:
            print(
                f"Control Number: {control_number.value} has confidence: "
                f"{control_number.confidence}"
            )
        employer = w2.fields.get("Employer")
        if employer:
            print("Employer data:")
            employer_name = employer.value.get("Name")
            if employer_name:
                print(
                    f"...Name: {employer_name.value} has confidence: {employer_name.confidence}"
                )
            employer_id = employer.value.get("IdNumber")
            if employer_id:
                print(
                    f"...ID Number: {employer_id.value} has confidence: {employer_id.confidence}"
                )
            employer_address = employer.value.get("Address")
            if employer_address:
                print(f"...Address: {format_address_value(employer_address.value)}")
                print(f"\n......has confidence: {employer_address.confidence}")
            employer_zipcode = employer.value.get("ZipCode")
            if employer_zipcode:
                print(
                    f"...Zipcode: {employer_zipcode.value} has confidence: {employer_zipcode.confidence}"
                )
        wages_tips = w2.fields.get("WagesTipsAndOtherCompensation")
        if wages_tips:
            print(
                f"Wages, tips, and other compensation: {wages_tips.value} "
                f"has confidence: {wages_tips.confidence}"
            )
        fed_income_tax_withheld = w2.fields.get("FederalIncomeTaxWithheld")
        if fed_income_tax_withheld:
            print(
                f"Federal income tax withheld: {fed_income_tax_withheld.value} has "
                f"confidence: {fed_income_tax_withheld.confidence}"
            )
        social_security_wages = w2.fields.get("SocialSecurityWages")
        if social_security_wages:
            print(
                f"Social Security wages: {social_security_wages.value} has confidence: "
                f"{social_security_wages.confidence}"
            )
        social_security_tax_withheld = w2.fields.get("SocialSecurityTaxWithheld")
        if social_security_tax_withheld:
            print(
                f"Social Security tax withheld: {social_security_tax_withheld.value} "
                f"has confidence: {social_security_tax_withheld.confidence}"
            )
        medicare_wages_tips = w2.fields.get("MedicareWagesAndTips")
        if medicare_wages_tips:
            print(
                f"Medicare wages and tips: {medicare_wages_tips.value} has confidence: "
                f"{medicare_wages_tips.confidence}"
            )
        medicare_tax_withheld = w2.fields.get("MedicareTaxWithheld")
        if medicare_tax_withheld:
            print(
                f"Medicare tax withheld: {medicare_tax_withheld.value} has confidence: "
                f"{medicare_tax_withheld.confidence}"
            )
        social_security_tips = w2.fields.get("SocialSecurityTips")
        if social_security_tips:
            print(
                f"Social Security tips: {social_security_tips.value} has confidence: "
                f"{social_security_tips.confidence}"
            )
        allocated_tips = w2.fields.get("AllocatedTips")
        if allocated_tips:
            print(
                f"Allocated tips: {allocated_tips.value} has confidence: {allocated_tips.confidence}"
            )
        verification_code = w2.fields.get("VerificationCode")
        if verification_code:
            print(
                f"Verification code: {verification_code.value} has confidence: {verification_code.confidence}"
            )
        dependent_care_benefits = w2.fields.get("DependentCareBenefits")
        if dependent_care_benefits:
            print(
                f"Dependent care benefits: {dependent_care_benefits.value} has confidence: {dependent_care_benefits.confidence}"
            )
        non_qualified_plans = w2.fields.get("NonQualifiedPlans")
        if non_qualified_plans:
            print(
                f"Non-qualified plans: {non_qualified_plans.value} has confidence: {non_qualified_plans.confidence}"
            )
        additional_info = w2.fields.get("AdditionalInfo")
        if additional_info:
            print("Additional information:")
            for item in additional_info.value:
                letter_code = item.value.get("LetterCode")
                if letter_code:
                    print(
                        f"...Letter code: {letter_code.value} has confidence: {letter_code.confidence}"
                    )
                amount = item.value.get("Amount")
                if amount:
                    print(
                        f"...Amount: {amount.value} has confidence: {amount.confidence}"
                    )
        is_statutory_employee = w2.fields.get("IsStatutoryEmployee")
        if is_statutory_employee:
            print(
                f"Is statutory employee: {is_statutory_employee.value} has confidence: {is_statutory_employee.confidence}"
            )
        is_retirement_plan = w2.fields.get("IsRetirementPlan")
        if is_retirement_plan:
            print(
                f"Is retirement plan: {is_retirement_plan.value} has confidence: {is_retirement_plan.confidence}"
            )
        third_party_sick_pay = w2.fields.get("IsThirdPartySickPay")
        if third_party_sick_pay:
            print(
                f"Is third party sick pay: {third_party_sick_pay.value} has confidence: {third_party_sick_pay.confidence}"
            )
        other_info = w2.fields.get("Other")
        if other_info:
            print(
                f"Other information: {other_info.value} has confidence: {other_info.confidence}"
            )
        state_tax_info = w2.fields.get("StateTaxInfos")
        if state_tax_info:
            print("State Tax info:")
            for tax in state_tax_info.value:
                state = tax.value.get("State")
                if state:
                    print(f"...State: {state.value} has confidence: {state.confidence}")
                employer_state_id_number = tax.value.get("EmployerStateIdNumber")
                if employer_state_id_number:
                    print(
                        f"...Employer state ID number: {employer_state_id_number.value} has "
                        f"confidence: {employer_state_id_number.confidence}"
                    )
                state_wages_tips = tax.value.get("StateWagesTipsEtc")
                if state_wages_tips:
                    print(
                        f"...State wages, tips, etc: {state_wages_tips.value} has confidence: "
                        f"{state_wages_tips.confidence}"
                    )
                state_income_tax = tax.value.get("StateIncomeTax")
                if state_income_tax:
                    print(
                        f"...State income tax: {state_income_tax.value} has confidence: "
                        f"{state_income_tax.confidence}"
                    )
        local_tax_info = w2.fields.get("LocalTaxInfos")
        if local_tax_info:
            print("Local Tax info:")
            for tax in local_tax_info.value:
                local_wages_tips = tax.value.get("LocalWagesTipsEtc")
                if local_wages_tips:
                    print(
                        f"...Local wages, tips, etc: {local_wages_tips.value} has confidence: "
                        f"{local_wages_tips.confidence}"
                    )
                local_income_tax = tax.value.get("LocalIncomeTax")
                if local_income_tax:
                    print(
                        f"...Local income tax: {local_income_tax.value} has confidence: "
                        f"{local_income_tax.confidence}"
                    )
                locality_name = tax.value.get("LocalityName")
                if locality_name:
                    print(
                        f"...Locality name: {locality_name.value} has confidence: "
                        f"{locality_name.confidence}"
                    )
    # [END analyze_tax_us_w2]


if __name__ == "__main__":
    import sys
    from azure.core.exceptions import HttpResponseError

    try:
        analyze_tax_us_w2()
    except HttpResponseError as error:
        print(
            "For more information about troubleshooting errors, see the following guide: "
            "https://aka.ms/azsdk/python/formrecognizer/troubleshooting"
        )
        # Examples of how to check an HttpResponseError
        # Check by error code:
        if error.error is not None:
            if error.error.code == "InvalidImage":
                print(f"Received an invalid image error: {error.error}")
            if error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            # Raise the error again after printing it
            raise
        # If the inner error is None and then it is possible to check the message to get more information:
        if "Invalid request".casefold() in error.message.casefold():
            print(f"Uh-oh! Seems there was an invalid request: {error}")
        # Raise the error again
        raise

# Next steps:
# Learn more about US W2 Tax model: https://aka.ms/V3.1-concept-tax-document
# Find more sample code: https://github.com/Azure-Samples/document-intelligence-code-samples