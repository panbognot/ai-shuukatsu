import pandas as pd
import os
import openpyxl

from docx import Document
from openpyxl import Workbook

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

# To do: Create demo resume pdf file 

# Replace later with a rirekisho document creation function
# Note: This is still NOT good enough but it is a start.
# Create a demo rirekisho document (Japanese resume)
def create_demo_rirekisho_xlsx(filename='demo_rirekisho.xlsx'):
    """
    Create a sample Japanese-style resume (rirekisho) as an Excel file
    for demonstration purposes. This uses an A3-sized layout.
    """
    try:
        # Create a new workbook and select the active sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "IT Rirekisho" # type: ignore

        # --- Fill in simulated data based on a common A3 rirekisho layout ---
        # The data is spread across more columns to simulate a wider sheet
        # Personal Information (Left Side)
        ws['A1'] = "履歴書" # type: ignore
        ws['A3'] = "氏名"  # type: ignore # Name
        ws['C3'] = "紙神 ラッド" # type: ignore # Kamigami Rad (Example name)
        ws['A4'] = "フリガナ" # type: ignore # Furigana
        ws['C4'] = "カミガミ ラッド" # type: ignore # Kamigami Rad (Furigana)
        ws['A5'] = "生年月日" # type: ignore # Date of Birth
        ws['C5'] = "1990年1月1日" # type: ignore # Jan 1, 1990
        
        # Address
        ws['A7'] = "住所" # type: ignore # Address
        ws['C7'] = "東京都新宿区西新宿1-1-1" # type: ignore # Tokyo, Shinjuku
        
        # Educational History (Left Side)
        ws['A9'] = "学歴・職歴" # type: ignore # Educational & Work History
        ws['B10'] = "年" # type: ignore # Year
        ws['C10'] = "月" # type: ignore # Month
        ws['D10'] = "学歴・職歴" # type: ignore # History Details
        
        ws['B11'] = 2008 # type: ignore
        ws['C11'] = 3 # type: ignore
        ws['D11'] = "〇〇高等学校 卒業" # type: ignore # Graduated from XX High School
        
        ws['B12'] = 2012 # type: ignore
        ws['C12'] = 3 # type: ignore
        ws['D12'] = "〇〇大学 経済学部 卒業" # type: ignore # Graduated from XX University, Faculty of Economics
        
        ws['B13'] = 2012 # type: ignore
        ws['C13'] = 4 # type: ignore
        ws['D13'] = "株式会社〇〇 入社" # type: ignore # Joined XX Co., Ltd.
        
        ws['B14'] = 2018 # type: ignore
        ws['C14'] = 6 # type: ignore
        ws['D14'] = "米国法人〇〇 出向" # type: ignore # Transferred to XX USA Corporation
        
        ws['B15'] = 2023 # type: ignore
        ws['C15'] = 3 # type: ignore
        ws['D15'] = "株式会社〇〇 退職" # type: ignore # Resigned from XX Co., Ltd.
        
        ws['B16'] = 2023 # type: ignore
        ws['C16'] = 4 # type: ignore
        ws['D16'] = "株式会社〇〇 入社" # type: ignore # Joined YY Co., Ltd.

        # Licenses and Certifications (Left Side)
        ws['A18'] = "免許・資格" # type: ignore # Licenses and Certifications
        ws['B19'] = 2012 # type: ignore
        ws['C19'] = 5 # type: ignore
        ws['D19'] = "普通自動車第一種運転免許" # type: ignore # Class 1 Ordinary Vehicle Driver's License
        
        ws['B20'] = 2020 # type: ignore
        ws['C20'] = 11 # type: ignore
        ws['D20'] = "TOEIC L&R Test 900点" # type: ignore # TOEIC L&R Test Score 900

        # Self-PR (Right Side)
        # These are now in a new column to simulate the A3 width
        ws['E1'] = "自己PR" # type: ignore # Self-PR
        ws['G1'] = "私は、これまでの職務経験で培った課題解決能力とコミュニケーション能力に自信があります。特に、米国法人への出向経験では、多様な文化を持つチームメンバーと協力し、プロジェクトを成功に導きました。貴社においても、この経験を活かし、チームに貢献できると確信しております。" # type: ignore

        # Motivation for Application (Right Side)
        ws['E3'] = "志望動機" # type: ignore # Motivation for Application
        ws['G3'] = "貴社の「イノベーションを通じて社会に貢献する」という企業理念に深く共感いたしました。これまでの経験を活かし、新たな技術開発に挑戦することで、貴社の事業拡大に貢献したいと考えております。特に、〇〇分野への貴社の取り組みに強い関心を持っており、ぜひ貢献したいと考えております。" # type: ignore

        # Save the workbook
        folder = "data"
        new_file_path = f"{folder}/{filename}"
        wb.save(new_file_path)
        print(f"Demo rirekisho created at: {new_file_path}")

    except Exception as e:
        print(f"Error creating demo rirekisho: {e}")
        return False