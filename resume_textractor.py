import os
from docx import Document

from src.resume.generators import create_demo_resume_docx
from src.utils.helpers import extract_text_from_docx, extract_text_from_pdf

if __name__ == "__main__":
    # Create a demo resume document
    create_demo_resume_docx("new_resume.docx")

    # Example usage of the extract_text_from_pdf function
    file_to_extract = "user-docs/2025-08 IT Resume.pdf"

    print(f"Extracting text from: {file_to_extract}...")
    resume_text = extract_text_from_pdf(file_to_extract)

    if resume_text:
        print("\n--- Extracted Resume Text ---")
        print(resume_text)
        print("\n--- End of Extracted Text ---")