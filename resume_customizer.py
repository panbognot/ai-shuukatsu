from src.resume.generators import create_custom_self_introduction
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    # Create a custom self-introduction based on the applicant's profile, company website, and job post
    create_custom_self_introduction()