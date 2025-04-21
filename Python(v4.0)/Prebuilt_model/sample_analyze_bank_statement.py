# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
This code sample shows Prebuilt US Bank Statement operations with the Azure AI Document Intelligence client library. 
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
        "prebuilt-bankStatement.us", body=f
    )
bankstatements = poller.result()

for idx, statement in enumerate(bankstatements.documents):
    print("--------Recognizing statement #{}--------".format(idx + 1))
    
    account_holder_name = statement.fields.get("AccountHolderName")
    if account_holder_name:
        print(
            "Account Holder Name: {} has confidence: {}".format(
                account_holder_name.value_string, account_holder_name.confidence
            )
        )
    
    account_holder_address = statement.fields.get("AccountHolderAddress")
    if account_holder_address:
        print(
            "Account Holder Address: {} has confidence: {}".format(
                account_holder_address.value_address, account_holder_address.confidence
            )
        )
    
    bank_name = statement.fields.get("BankName")
    if bank_name:
        print(
            "Bank Name: {} has confidence: {}".format(
                bank_name.value_string, bank_name.confidence
            )
        )
    
    bank_address = statement.fields.get("BankAddress")
    if bank_address:
        print(
            "Bank Address: {} has confidence: {}".format(
                bank_address.value_address, bank_address.confidence
            )
        )
    
    statement_start_date = statement.fields.get("StatementStartDate")
    if statement_start_date:
        print(
            "Statement Start Date: {} has confidence: {}".format(
                statement_start_date.value_date, statement_start_date.confidence
            )
        )
    
    statement_end_date = statement.fields.get("StatementEndDate")
    if statement_end_date:
        print(
            "Statement End Date: {} has confidence: {}".format(
                statement_end_date.value_date, statement_end_date.confidence
            )
        )
    
    accounts = statement.fields.get("Accounts")
    if accounts:
        for account_idx, account in enumerate(accounts.value_array):
            print("...Account #{}".format(account_idx + 1))
            account_number = account.value_object.get("AccountNumber")
            if account_number:
                print(
                    "......Account Number: {} has confidence: {}".format(
                        account_number.value_string, account_number.confidence
                    )
                )
            
            account_type = account.value_object.get("AccountType")
            if account_type:
                print(
                    "......Account Type: {} has confidence: {}".format(
                        account_type.value_string, account_type.confidence
                    )
                )
            
            beginning_balance = account.value_object.get("BeginningBalance")
            if beginning_balance:
                print(
                    "......Beginning Balance: {} has confidence: {}".format(
                        beginning_balance.value_number, beginning_balance.confidence
                    )
                )
            
            ending_balance = account.value_object.get("EndingBalance")
            if ending_balance:
                print(
                    "......Ending Balance: {} has confidence: {}".format(
                        ending_balance.value_number, ending_balance.confidence
                    )
                )
            
            total_service_fees = account.value_object.get("TotalServiceFees")
            if total_service_fees:
                print(
                    "......Total Service Fees: {} has confidence: {}".format(
                        total_service_fees.value_number, total_service_fees.confidence
                    )
                )
            
            transactions = account.value_object.get("Transactions")
            if transactions:
                print("......Transactions:")
                for transaction_idx, transaction in enumerate(transactions.value_array):
                    print(".........Transaction #{}".format(transaction_idx + 1))
                    transaction_date = transaction.value_object.get("Date")
                    if transaction_date:
                        print(
                            "............Date: {} has confidence: {}".format(
                                transaction_date.value_date, transaction_date.confidence
                            )
                        )
                    
                    description = transaction.value_object.get("Description")
                    if description:
                        print(
                            "............Description: {} has confidence: {}".format(
                                description.value_string, description.confidence
                            )
                        )
                    
                    deposit_amount = transaction.value_object.get("DepositAmount")
                    if deposit_amount:
                        print(
                            "............Deposit Amount: {} has confidence: {}".format(
                                deposit_amount.value_number, deposit_amount.confidence
                            )
                        )
                    
                    withdrawal_amount = transaction.value_object.get("WithdrawalAmount")
                    if withdrawal_amount:
                        print(
                            "............Withdrawal Amount: {} has confidence: {}".format(
                                withdrawal_amount.value_number, withdrawal_amount.confidence
                            )
                        )
    print("--------------------------------------")
