import os
from pathlib import Path
from docx import Document
from docx.opc.exceptions import OpcError
from docx.shared import Inches

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
    
# Replace later with a resume document creation function
def create_demo_resume_docx(filename = 'demo_resume.docx'):
    """
    Create a sample mock_resume.docx file for demonstration purposes.
    """
    new_doc = Document()
    new_doc.add_heading('Rad Navs', 0)
    new_doc.add_paragraph('Bilingual (English-Japanese) IT Manager and Senior Software Developer with 10+ years of experience in software development, team leadership, and strategic IT planning.')
    
    # Add bullet points
    p = new_doc.add_paragraph('Contact Info:')
    p.add_run('\nEmail: pradoart.jp@gmail.com').italic = True
    p.add_run('\nPhone: +81 xx-xxxx-xxxx').italic = True

    # Add a heading and skills section
    new_doc.add_heading('Skills', level=1)
    skills_list = new_doc.add_paragraph()
    skills_list.add_run('Python, PHP, Angular, AWS, Team Leadership, Strategic IT Planning').bold = True

    # Add a section for language skills
    new_doc.add_heading('Language Skills', level=1)
    languages = new_doc.add_paragraph()
    languages.add_run('English (Native), Japanese (JLPT N2)').italic = True

    # Add a work experience section
    new_doc.add_heading('Work Experience', level=1)

    # Add a table
    table = new_doc.add_table(rows=1, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Project Name'
    hdr_cells[1].text = 'Description'

    # Save the document
    folder = "data"
    new_file_path = f"{folder}/{filename}"
    new_doc.save(new_file_path)
    print(f"Demo document created at: {new_file_path}")

if __name__ == "__main__":
    # Create a demo resume document
    create_demo_resume_docx()