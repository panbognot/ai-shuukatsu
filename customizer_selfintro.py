import pandas as pd
from src.resume.generators import create_custom_self_introduction_from_text, create_demo_custom_self_introduction, create_custom_self_introduction_from_files
from dotenv import load_dotenv

from src.utils.helpers import extract_text_from_docx

load_dotenv()

if __name__ == "__main__":

    # Create a custom self-introduction based on the applicant's profile, company website, and job post
    # create_demo_custom_self_introduction()
    applicant_profile = "user-docs/2025-08 IT Resume.docx"
    create_custom_self_introduction_from_files(
        profile_filepath=applicant_profile,
        job_post_filename="user-docs/job-posts/job.txt",
        website="https://www.medley.jp/"
    )

    # The applicant's profile is stored in a .docx file
    extracted_profile = extract_text_from_docx(applicant_profile)

    # Create custom self-introductions for multiple job posts using an excel file
    # job_posts_file = "user-docs/job-posts/wp-leads.xlsx"
    job_posts_file = "user-docs/job-posts/japan-dev-leads.xlsx"

    try:
        # The header=0 argument specifies that the first row is the header.
        df = pd.read_excel(job_posts_file, header=0, engine='openpyxl')
        for index, row in df.iterrows():
            company_name = row['Company']
            job_post = row['Job-Post']
            website = row.get('Website', None)

            print(f"Creating custom self-introduction for {company_name}...")
            create_custom_self_introduction_from_text(
                profile=extracted_profile,
                company_name=company_name,
                job_post=job_post,
                website=website
            )
    except FileNotFoundError:
        print(f"Error: The file '{job_posts_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")