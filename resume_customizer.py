from src.resume.generators import create_demo_custom_self_introduction, create_custom_self_introduction
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    # Create a custom self-introduction based on the applicant's profile, company website, and job post
    # create_demo_custom_self_introduction()
    create_custom_self_introduction(
        profile_filepath="user-docs/2025-08 IT Resume.docx",
        job_post_filename="user-docs/job-posts/job.txt",
        website="https://www.medley.jp/"
    )