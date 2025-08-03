from google import genai
import enum
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class JobType(enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"

class JobIndustry(enum.Enum):
    IT = "it"
    MARKETING = "marketing"
    SALES = "sales"
    ENGINEERING = "engineering"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    OTHERS = "others"

class CompanyGrade(enum.Enum):
    STARTUP = "startup"
    SME = "sme"
    ENTERPRISE = "enterprise"
    GOVERNMENT = "government"
    NGO = "ngo"

class DocumentScreeningChance(enum.Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class JobPost(BaseModel):
    id: int
    job_title: str
    document_screening_chance: DocumentScreeningChance
    company_name: str
    company_grade: CompanyGrade
    job_type: JobType
    job_industry: JobIndustry
    job_description: str
    location: str
    salary_range: str
    requirements: list[str]
    benefits: list[str]
    application_deadline: str

desired_job = "AI / ML Engineer"
desired_industry = JobIndustry.IT
applicant_profile = """
Bilingual (English-Japanese) IT Manager and Senior Software Developer with 10+ 
years of experience in software development, team leadership, and strategic IT 
planning. Proficient in Python, PHP, Angular, and AWS, with a proven track record of 
delivering scalable solutions for multinational teams. JLPT N2 certified with a strong 
interest in Japanese culture and technology.

I have no prior work experience in Japan, but I am eager to start my career here.
I am currently holding a student visa and looking for a full-time job in Japan.
I'm particularly interested in roles that involve AI and machine learning,
as I have a strong background in software development and a keen interest in these fields.
I may not have work experience in AI/ML, but I have completed several online courses and 
I am working on personal projects in this area.
"""

gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="""
        You are a recruiter and talent acquisition expert with 10+ years of experience
        in Japan's {desired_industry} industry. Your task is to help a job seeker find the most suitable job
        opportunities in Japan based on their target job.

        target_job: {desired_job}
        applicant_profile: {applicant_profile}

        Please provide a list of 10 job posts.
        """,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[JobPost],
    },
)

print(response.text)  # Use the response as a JSON string.