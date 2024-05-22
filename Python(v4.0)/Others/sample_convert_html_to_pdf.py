# coding: utf-8

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_convert_html_to_pdf.py

DESCRIPTION:
    This sample demonstrates how to convert a html file to the pdf file.
    Before using this function, need to install following required component:
        1.Install python-pdfkit:
            "$ pip install pdfkit"
        2.Install wkhtmltopdf:
            -Debian/Ubuntu:
                "$ sudo apt-get install wkhtmltopdf"
            -macOS:
                "$ brew install homebrew/cask/wkhtmltopdf"
            -Windows and other options: check https://wkhtmltopdf.org/downloads.html for wkhtmltopdf binary installers
    More information about pdfkit, reference from https://pypi.org/project/pdfkit/.
USAGE:
    python sample_convert_html_to_pdf.py
"""

import os
import pdfkit


def convert_html_file_to_pdf(html_path, save_pdf_path):
    with open(html_path, "r", encoding="utf-8") as f:
        htmlStr = f.read()

        directory_to_save_pdf = os.path.dirname(save_pdf_path)
        if not os.path.isdir(directory_to_save_pdf):
            os.makedirs(directory_to_save_pdf)

        return pdfkit.from_string(htmlStr, save_pdf_path)


if __name__ == "__main__":
    current_file_path = os.path.abspath(__file__)
    current_folder_path = os.path.dirname(current_file_path)

    path_of_sample_html = os.path.abspath(
        os.path.join(
            current_file_path,
            "..",
            "..",
            "..",
            "./Data/other-doc-type/web-page.html",
        )
    )

    path_to_save_pdf = os.path.abspath(
        os.path.join(
            current_folder_path,
            "./result/converted.pdf",
        )
    )

    isSuccessful = convert_html_file_to_pdf(path_of_sample_html, path_to_save_pdf)
    if isSuccessful:
        print(f"Convert pdf successfully in {path_to_save_pdf}")
    else:
        print("Something wrong. Check the html file please.")
