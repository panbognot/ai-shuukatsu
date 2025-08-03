import os
from pathlib import Path
from docx import Document
from docx.opc.exceptions import OpcError
from docx.shared import Inches

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