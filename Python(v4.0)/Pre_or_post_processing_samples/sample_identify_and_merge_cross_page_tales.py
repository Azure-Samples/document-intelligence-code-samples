# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_identify_and_merge_cross_page_tales.py

DESCRIPTION:

This sample demonstrates how to use the output of Layout model and some business rules to identify cross-page tables and merge them into one table in the markdown output based on rules.
Once idenfied, it can be further processed to merge these tables and keep the semantics of a table.

Depending on your document format, there can be different rules applied to idenfity a cross-page table. This sample shows how to use the following rules to identify cross-page tables:

- Vertical layout
    - If the 2 or more tables appear in consecutive pages
    - And there's only page header, page footer or page number beteen them
    - And the tables have the same number of columns
    - These tables could be considered to one vertical table.

- Horizontal layout
    - If there're 2 or more tables appear in consecutive pages
    - And the table's right side is quite close to the right edge of current page
    - And the next table's left side is quite close to the left edge of next page
    - And the tables have the same number of row count
    - These tables could be considered to one horizontal table.

You can customize the rules based on your scenario.

PRE-REQUISITES:

- An Azure AI Document Intelligence resource - follow https://learn.microsoft.com/azure/ai-services/document-intelligence/create-document-intelligence-resource?view=doc-intel-4.0.0 to create one if you don't have.
- Get familiar with the output structure of Layout model - complete this quickstart: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-python#layout-model to learn more.

SETUP:
pip install azure-ai-documentintelligence python-dotenv azure-identity

USAGE:

python sample_identify_cross_page_tables.py [input_file_path]

"""


"""
This code loads environment variables using the `dotenv` library and sets the necessary environment variables for Azure services.
The environment variables are loaded from the `.env` file in the same directory as this notebook.
"""
import os, sys
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import ContentFormat

load_dotenv()

BORDER_SYMBOL = "|"
endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")


def get_table_page_numbers(table):
    """
    Returns a list of page numbers where the table appears.

    Args:
        table: The table object.

    Returns:
        A list of page numbers where the table appears.
    """
    return [region.page_number for region in table.bounding_regions]


def get_table_span_offsets(table):
    """
    Calculates the minimum and maximum offsets of a table's spans.

    Args:
        table (Table): The table object containing spans.

    Returns:
        tuple: A tuple containing the minimum and maximum offsets of the table's spans.
               If the tuple is (-1, -1), it means the table's spans is empty.
    """
    if table.spans:
        min_offset = table.spans[0].offset
        max_offset = table.spans[0].offset + table.spans[0].length

        for span in table.spans:
            if span.offset < min_offset:
                min_offset = span.offset
            if span.offset + span.length > max_offset:
                max_offset = span.offset + span.length

        return min_offset, max_offset
    else:
        return -1, -1


def get_merge_table_candidates_and_table_integral_span(tables):
    """
    Find the merge table candidates and calculate the integral span of each table based on the given list of tables.

    Parameters:
    tables (list): A list of tables.

    Returns:
    list: A list of merge table candidates, where each candidate is a dictionary with keys:
          - pre_table_idx: The index of the first candidate table to be merged (the other table to be merged is the next one).
          - start: The start offset of the 2nd candidate table.
          - end: The end offset of the 1st candidate table.
    
    list: A concision list of result.tables. The significance is to store the calculated data to avoid repeated calculations in subsequent reference.
    """
    table_integral_span_list = []
    merge_tables_candidates = []
    pre_table_idx = -1
    pre_table_page = -1
    pre_max_offset = 0

    for table_idx, table in enumerate(tables):
        min_offset, max_offset = get_table_span_offsets(table)
        if min_offset > -1 and max_offset > -1:
            table_page = min(get_table_page_numbers(table))
            print(f"Table {table_idx} has offset range: {min_offset} - {max_offset} on page {table_page}")

            # If there is a table on the next page, it is a candidate for merging with the previous table.
            if table_page == pre_table_page + 1:
                pre_table = {
                    "pre_table_idx": pre_table_idx,
                    "start": pre_max_offset,
                    "end": min_offset,
                    "min_offset": min_offset,
                    "max_offset": max_offset,
                }
                merge_tables_candidates.append(pre_table)
                
            table_integral_span_list.append(
                {
                    "idx": table_idx,
                    "min_offset": min_offset,
                    "max_offset": max_offset,
                }
            )

            pre_table_idx = table_idx
            pre_table_page = table_page
            pre_max_offset = max_offset
        else:
            print(f"Table {table_idx} is empty")
            table_integral_span_list.append(
                {"idx": {table_idx}, "min_offset": -1, "max_offset": -1}
            )

    return merge_tables_candidates, table_integral_span_list


def check_paragraph_presence(paragraphs, start, end):
    """
    Checks if there is a paragraph within the specified range that is not a page header, page footer, or page number. If this were the case, the table would not be a merge table candidate.

    Args:
        paragraphs (list): List of paragraphs to check.
        start (int): Start offset of the range.
        end (int): End offset of the range.

    Returns:
        bool: True if a paragraph is found within the range that meets the conditions, False otherwise.
    """
    for paragraph in paragraphs:
        for span in paragraph.spans:
            if span.offset > start and span.offset < end:
                # The logic role of a parapgaph is used to idenfiy if it's page header, page footer, page number, title, section heading, etc. Learn more: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept-layout?view=doc-intel-4.0.0#document-layout-analysis
                if not hasattr(paragraph, 'role'):
                    return True
                elif hasattr(paragraph, 'role') and paragraph.role not in ["pageHeader", "pageFooter", "pageNumber"]:
                    return True
    return False

def check_tables_are_horizontal_distribution(result, pre_table_idx):
    """
    Identify two consecutive pages whether is horizontal distribution.

    Args:
         result: the analysis result from document intelligence service.
         pre_table_idx: previous table's index
    
    Returns:
         bool: the two table are horizontal distribution or not.
    """
    INDEX_OF_X_LEFT_TOP = 0
    INDEX_OF_X_LEFT_BOTTOM = 6
    INDEX_OF_X_RIGHT_TOP = 2
    INDEX_OF_X_RIGHT_BOTTOM = 4

    # For these threshold rate, could be adjusted based on different document's table layout. 
    # When debugging document instance, it's better to print the actual cover rate until the two horizontal candiacate tables are merged.
    THRESHOLD_RATE_OF_RIGHT_COVER = 0.99
    THRESHOLD_RATE_OF_LEFT_COVER = 0.01

    is_right_covered = False
    is_left_covered = False

    if (
        result.tables[pre_table_idx].row_count
        == result.tables[pre_table_idx + 1].row_count
    ):
        for region in result.tables[pre_table_idx].bounding_regions:
            page_width = result.pages[region.page_number - 1].width
            x_right = max(
                region.polygon[INDEX_OF_X_RIGHT_TOP],
                region.polygon[INDEX_OF_X_RIGHT_BOTTOM],
            )
            right_cover_rate = x_right / page_width
            if right_cover_rate > THRESHOLD_RATE_OF_RIGHT_COVER:
                is_right_covered = True
                break

        for region in result.tables[pre_table_idx + 1].bounding_regions:
            page_width = result.pages[region.page_number - 1].width
            x_left = min(
                region.polygon[INDEX_OF_X_LEFT_TOP],
                region.polygon[INDEX_OF_X_LEFT_BOTTOM],
            )
            left_cover_rate = x_left / page_width
            if left_cover_rate < THRESHOLD_RATE_OF_LEFT_COVER:
                is_left_covered = True
                break

    return is_left_covered and is_right_covered


def remove_header_from_markdown_table(markdown_table) :
    """
    If an actual table is distributed into two pages vertically. From analysis result, it will be generated as two tables in markdown format.
    Before merging them into one table, it need to be removed the markdown table-header format string. This function implement that.

    Args:
        markdown_table: the markdown table string which need to be removed the markdown table-header.
    Returns:
        string: the markdown table string without table-header.
    """
    HEADER_SEPARATOR_CELL_CONTENT = " - "

    result = ""
    lines = markdown_table.splitlines()
    for line in lines:
        border_list = line.split(HEADER_SEPARATOR_CELL_CONTENT)
        border_set = set(border_list)
        if len(border_set) == 1 and border_set.pop() == BORDER_SYMBOL:
            continue
        else:
            result += f"{line}\n"

    return result


def merge_horizontal_tables(md_table_1, md_table_2):
    """
    Merge two consecutive horizontal markdown tables into one markdown table.

    Args:
        md_table_1: markdown table 1
        md_table_2: markdown table 2
    
    Returns:
        string: merged markdown table
    """
    rows1 = md_table_1.strip().splitlines()
    rows2 = md_table_2.strip().splitlines()

    merged_rows = []
    for row1, row2 in zip(rows1, rows2):
        merged_row = (
            (row1[:-1] if row1.endswith(BORDER_SYMBOL) else row1)
            + BORDER_SYMBOL
            + (row2[1:] if row2.startswith(BORDER_SYMBOL) else row2)
        )
        merged_rows.append(merged_row)

    merged_table = "\n".join(merged_rows)
    return merged_table


def merge_vertical_tables(md_table_1, md_table_2) :
    """
    Merge two consecutive vertical markdown tables into one markdown table.

    Args:
        md_table_1: markdown table 1
        md_table_2: markdown table 2
    
    Returns:
        string: merged markdown table
    """
    table2_without_header = remove_header_from_markdown_table(md_table_2)
    rows1 = md_table_1.strip().splitlines()
    rows2 = table2_without_header.strip().splitlines()

    num_columns1 = len(rows1[0].split(BORDER_SYMBOL)) - 2
    num_columns2 = len(rows2[0].split(BORDER_SYMBOL)) - 2

    if num_columns1 != num_columns2:
        raise ValueError("Different count of columns")

    merged_rows = rows1 + rows2
    merged_table = '\n'.join(merged_rows)

    return merged_table


def identify_and_merge_cross_page_tables(input_file_path):
    """
    Identifies and merges tables that span across multiple pages in a document.
    
    Args:
        input_file_path: the file path which need to be analysis.
    Returns:
        None
    """
    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    file_path = input_file_path

    # You can also use a URL instead of a local file with begin_analyze_document_from_url().
    with open(file_path, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-layout",
            analyze_request=f,
            content_type="application/octet-stream",
            output_content_format=ContentFormat.MARKDOWN,
        )

    result = poller.result()

    merge_tables_candidates, table_integral_span_list = get_merge_table_candidates_and_table_integral_span(result.tables)

    print("----------------------------------------")

    SEPARATOR_LENGTH_IN_MARKDOWN_FORMAT = 2
    merged_table_list = []
    for i, merged_table in enumerate(merge_tables_candidates):
        pre_table_idx = merged_table["pre_table_idx"]
        start = merged_table["start"]
        end = merged_table["end"]
        has_paragraph = check_paragraph_presence(result.paragraphs, start, end)

        is_horizontal = check_tables_are_horizontal_distribution(result, pre_table_idx)
        is_vertical = (
            not has_paragraph and
            result.tables[pre_table_idx].column_count
            == result.tables[pre_table_idx + 1].column_count
            and table_integral_span_list[pre_table_idx + 1]["min_offset"]
            - table_integral_span_list[pre_table_idx]["max_offset"]
            <= SEPARATOR_LENGTH_IN_MARKDOWN_FORMAT
        )

        if is_vertical or is_horizontal:
            print(f"Merge table: {pre_table_idx} and {pre_table_idx + 1}")
            print("----------------------------------------")

            remark = ""
            cur_content = result.content[table_integral_span_list[pre_table_idx + 1]["min_offset"] : table_integral_span_list[pre_table_idx + 1]["max_offset"]]

            if is_horizontal:
                    remark = result.content[table_integral_span_list[pre_table_idx]["max_offset"] : table_integral_span_list[pre_table_idx + 1]["min_offset"]]
            
            merged_list_len = len(merged_table_list)
            if merged_list_len > 0 and len(merged_table_list[-1]["table_idx_list"]) > 0 and merged_table_list[-1]["table_idx_list"][-1] == pre_table_idx:
                merged_table_list[-1]["table_idx_list"].append(pre_table_idx + 1)
                merged_table_list[-1]["offset"]["max_offset"]= table_integral_span_list[pre_table_idx + 1]["max_offset"]
                if is_vertical:
                    merged_table_list[-1]["content"] = merge_vertical_tables(merged_table_list[-1]["content"], cur_content)
                elif is_horizontal:
                    merged_table_list[-1]["content"] = merge_horizontal_tables(merged_table_list[-1]["content"], cur_content)
                    merged_table_list[-1]["remark"] += remark

            else:
                pre_content = result.content[table_integral_span_list[pre_table_idx]["min_offset"] : table_integral_span_list[pre_table_idx]["max_offset"]]
                merged_table = {
                    "table_idx_list": [pre_table_idx, pre_table_idx + 1],
                    "offset": {
                        "min_offset": table_integral_span_list[pre_table_idx]["min_offset"],
                        "max_offset": table_integral_span_list[pre_table_idx + 1]["max_offset"],
                        },
                    "content": merge_vertical_tables(pre_content, cur_content) if is_vertical else merge_horizontal_tables(pre_content, cur_content),
                    "remark": remark.strip() if is_horizontal else ""
                    }
                
                if merged_list_len <= 0:
                    merged_table_list = [merged_table]
                else:
                    merged_table_list.append(merged_table)

    
    optimized_content= ""
    if merged_table_list:
        print(f"{len(merged_table_list)} merged result totally.")
        print("=========================================================")
        start_idx = 0
        for merged_table in merged_table_list:
            print(f"Merged result of table {", ".join([str(idx) for idx in merged_table["table_idx_list"]])}")
            print("-----------------------------------------------------")
            print(merged_table["content"])
            print("-----------------------------------------------------")

            optimized_content += result.content[start_idx : merged_table["offset"]["min_offset"]] + merged_table["content"] + merged_table["remark"]
            start_idx = merged_table["offset"]["max_offset"]
        
        optimized_content += result.content[start_idx:]
    else:
        optimized_content = result.content

    # Due to the optimized_content may be quite long, if want to check it, just uncomment below line:
    #print(f"this is the optimize content: {optimized_content}")

if __name__ == "__main__":
    # Check if the input string is provided as a command-line argument
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    else:
        print("Usage: python sample_identify_cross_page_tables.py [input_file_path]")
        sys.exit(1)

    identify_and_merge_cross_page_tables(input_file_path)
