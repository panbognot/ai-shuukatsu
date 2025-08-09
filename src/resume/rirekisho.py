import pandas as pd
import os
import openpyxl
from openpyxl import Workbook

from src.utils.helpers import find_cell_by_value

# TODO: Test robustness of this function with various rirekisho formats.
# (especially since my own rirekisho is quite long and complex, lol)
# It is placed in this file to keep the extraction logic separate from the
# generic text extraction functions.
def extract_data_from_rirekisho(file_path):
    """
    Extracts key information from a Japanese-style resume (.xlsx) file.
    The goal is to create a robust and dynamic parser to locate key info

    Returns:
        dict: A dictionary containing extracted data, or None on failure.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    try:
        # Load the Excel file into a pandas DataFrame, without a header
        df = pd.read_excel(file_path, header=None, engine='openpyxl')

        # Convert the DdataFram to a list of lists for easy cell access
        data = df.values.tolist()

        # Dictionary to store the extracted information
        resume_data = {}

        # --- Extract personal information from specific cell locations ---
        # Note: The cell indices are 0-based.
        resume_data['name'] = data[2][2] # C3 in Excel
        resume_data['name_furigana'] = data[3][2] # C4
        resume_data['date_of_birth'] = data[4][2] # C5
        resume_data['address'] = data[6][2] # C7

        # --- Extract educational/work history table ---
        history_start_row = 10  # Row 11 in Excel, 0-based index 10
        history_table = []
        for row_index in range(history_start_row, len(data)):
            if pd.isna(data[row_index][3]):
                break
            
            if isinstance(data[row_index][1], (int, float)) and data[row_index][3]:
                year = int(data[row_index][1])
                month = int(data[row_index][2])
                description = data[row_index][3]
                history_table.append(f"{year}年{month}月: {description}")
        
        resume_data['educational_work_history'] = history_table

        # --- Extract Licenses and Certifications table ---
        licenses_start_row, _ = find_cell_by_value(data, "免許・資格")
        licenses_table = []
        if licenses_start_row is not None:
            for row_index in range(licenses_start_row + 1, len(data)):
                if pd.isna(data[row_index][3]):
                    break
                
                if isinstance(data[row_index][1], (int, float)) and data[row_index][3]:
                    year = int(data[row_index][1])
                    month = int(data[row_index][2])
                    description = data[row_index][3]
                    licenses_table.append(f"{year}年{month}月: {description}")
        resume_data['licenses_and_certifications'] = licenses_table

        # --- Extract Self-PR section dynamically ---
        self_pr_start_row, self_pr_col = find_cell_by_value(data, "自己PR")
        self_pr_text = ""
        if self_pr_start_row is not None:
            # Assume the text is in the cell two columns to the right
            text_col = self_pr_col + 2 # type: ignore
            # Handle cases where the text might be in the next cell
            if pd.isna(data[self_pr_start_row][text_col]) and not pd.isna(data[self_pr_start_row][self_pr_col + 1]):
                text_col = self_pr_col + 1 # type: ignore
            
            if not pd.isna(data[self_pr_start_row][text_col]):
                self_pr_text = str(data[self_pr_start_row][text_col]).strip()
        
        resume_data['self_pr'] = self_pr_text
        
        # --- Extract Motivation for Application section dynamically ---
        motivation_start_row, motivation_col = find_cell_by_value(data, "志望動機")
        motivation_text = ""
        if motivation_start_row is not None:
            text_col = motivation_col + 2 # type: ignore
            if pd.isna(data[motivation_start_row][text_col]) and not pd.isna(data[motivation_start_row][motivation_col + 1]):
                text_col = motivation_col + 1 # type: ignore
            
            if not pd.isna(data[motivation_start_row][text_col]):
                motivation_text = str(data[motivation_start_row][text_col]).strip()

        resume_data['motivation'] = motivation_text

        return resume_data
    
    except Exception as e:
        print(f"An unexpected error occurred during extraction: {e}")
        return None