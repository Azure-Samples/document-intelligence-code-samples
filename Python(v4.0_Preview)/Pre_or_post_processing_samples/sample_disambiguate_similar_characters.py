# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_disambiguate_similar_characters.py

DESCRIPTION:

This sample demonstrates how to use business rules to disambiguate characters that could be confused with the input string due to similar looking characters.

The script defines a dictionary of characters that can be easily confused with each other, such as '0' and 'O', '1', 'I', and 'l'. It then uses a recursive function to generate all possible combinations of the input string with these confusing characters replaced.

This script could be useful in a variety of contexts, such as testing the robustness of a system against confusing inputs, or in a data cleaning process where similar looking characters need to be disambiguated.

USAGE:

python sample_disambiguate_similar_characters.py [input_string]

"""


import re
import sys

# Function to generate strings that can be confusing due to similar looking characters
def generate_confusing_strings(input_string):
    # Define a dictionary of characters that can be confusing
    confusing_chars = {
        '0': ['O'],
        'O': ['0'],
        '1': ['I', 'l'],
        'I': ['1', 'l'],
        'l': ['1', 'I']
    }
    
    result = [input_string]

    # Recursive function to generate all combinations of confusing strings
    def generate_combinations(input_str, index, current_combination):
        # If we have processed all characters in the string, add the current combination to the result
        if index == len(input_str):
            result.append(current_combination)
            return

        char = input_str[index]
        if char in confusing_chars:
            replacements = confusing_chars[char]
            for replacement in replacements:
                new_combination = current_combination[:index] + replacement + current_combination[index+1:]
                generate_combinations(input_str, index+1, new_combination)
        else:
            # If the current character is not in the confusing characters dictionary, just move on to the next character
            generate_combinations(input_str, index+1, current_combination)

    generate_combinations(input_string, 0, input_string)
    return result


# The function returns True if the code is a valid ICD-10 code and False otherwise. It can be replaced with other business rules in your scenario.
def verify_icd10_code(code):
    # Define a regular expression pattern for ICD-10 codes. An ICD-10 code is the 10th revision of the International Statistical Classification of Diseases and Related Health Problems (ICD), a medical classification list by the World Health Organization (WHO).
    # The pattern should start with a letter from A to Z (excluding U), followed by two digits.
    # After that, there may be a decimal point followed by one or two digits.
    # The pattern should match the entire string (^ and $ denote the start and end of the string, respectively).
    pattern = r'^[A-TV-Z]\d\d(\.\d{1,2})?$'
    
    return re.match(pattern, code) is not None


if __name__ == "__main__":
    # Check if the input string is provided as a command-line argument
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
    else:
        print("Usage: python sample_disambiguate_similar_characters.py [input_string]")
        sys.exit(1)

    # Generate confusing strings
    confusing_strings = generate_confusing_strings(input_string)
    print(confusing_strings)

    # Verify if any of the generated strings are ICD-10 codes
    icd10_codes = [code for code in confusing_strings if verify_icd10_code(code)]

    if icd10_codes:
        print("Generated ICD-10 codes:")
        for code in icd10_codes:
            print(code)
    else:
        print("No valid ICD-10 codes generated.")