import os
from pathlib import Path
from docx import Document
from docx.opc.exceptions import OpcError
from docx.shared import Inches

from src.utils.helpers import extract_text_from_docx
    
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
    # create_demo_resume_docx()

    # Example usage of the extract_text_from_docx function
    file_to_extract = "user-docs/2025-08 IT Resume.docx"

    print(f"Extracting text from: {file_to_extract}...")
    resume_text = extract_text_from_docx(file_to_extract)

    if resume_text:
        print("\n--- Extracted Resume Text ---")
        print(resume_text)
        print("\n--- End of Extracted Text ---")