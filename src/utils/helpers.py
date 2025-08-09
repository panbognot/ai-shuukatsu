import os
import io
from pathlib import Path
from docx import Document
from docx.opc.exceptions import OpcError
from docx.shared import Inches
import fitz

def find_cell_by_value(data, target_value):
    """
    Finds the row and column of the first cell that contains a specific value.
    Returns a tuple (row_index, col_index) or (None, None) if not found.
    """
    for row_index, row_data in enumerate(data):
        for col_index, cell_value in enumerate(row_data):
            if isinstance(cell_value, str) and target_value in cell_value:
                return row_index, col_index
    return None, None

def save_df_to_excel(file_name, df):
    """
    Save the DataFrame of companies to an Excel file.
    
    Parameters:
    file_name (str): Name of the Excel file to save.
    df_companies (pd.DataFrame): DataFrame containing company data.
    """
    from pathlib import Path
    
    # Define folder and file path
    folder = Path("../data")
    file_path = folder / f"{file_name}.xlsx" # Use f-string for dynamic file name
    
    # Create folder if it doesn't exist
    folder.mkdir(parents=True, exist_ok=True)

    # Save DataFrame to Excel
    df.to_excel(file_path, index=False)

# This is designed ONLY for .docx files. The .doc format is not supported.
def extract_text_from_docx(file_path):
    """
    Extract text from a .docx file.
    Args:
        file_path (str): The full path to the .docx file.
    Returns:
        str: The extracted text content, or None if an error occurs.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    
    # Note: delete this check later for a higher version
    # Check if the file is a .docx file
    if not file_path.lower().endswith('.docx'):
        print(f"Error: The file '{file_path}' is not a .docx file. This script only supports .docx files.")
        print("Please convert any .doc files to .docx before running.")
        return None
    
    try:
        # Open the .docx file
        doc = Document(file_path)

        # Initialize a list to hold the text from each paragraph
        full_text = []

        # Iterate through all paragraphs in the document and append their text
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)

        # Join the list of strings into a single string with newlines
        return '\n'.join(full_text)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except OpcError:
        print(f"Error: Could not open '{file_path}'. The file may be corrupt or not a valid .docx file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def extract_text_from_pdf(file_path):
    """
    Extracls all text content from a PDF file.
    Args:
        file_path (str): The full path to the PDF file.
    Returns:
        str: The extracted text content, or None if an error occurs.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    
    # Check if the file is a PDF
    if not file_path.lower().endswith('.pdf'):
        print(f"Error: The file '{file_path}' is not a PDF file.")
        return None
    
    try:
        # Open the PDF file
        with fitz.open(file_path) as doc:
            full_text = []
            # Iterate through each page and extract text
            for page in doc:
                text = page.get_text() # type: ignore
                full_text.append(text)

            # Join the text from all pages into a single string
            return "\n".join(full_text)
        
    except fitz.FileDataError:
        print(f"Error: Could not open '{file_path}. The file may be corrupt or not a valid PDF.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None