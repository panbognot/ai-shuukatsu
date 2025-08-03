# config.py

# Application Name
APP_NAME = "AI Shuukatsu"
APP_VERSION = "1.0.0"

# Environment (e.g., development, production, testing)
# This is often set via an environment variable, but can have a default
ENV = "development" # Default value

# Database settings (if not using sensitive parts from .env)
# These might point to local development databases
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "your_database_name"
# DB_USER and DB_PASSWORD would come from .env or env vars

# API Endpoints
GEMINI_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
EXTERNAL_SERVICE_URL = "https://api.external.com/v2"

# Other general settings
DEBUG_MODE = True
LOG_LEVEL = "INFO" # INFO, DEBUG, WARNING, ERROR, CRITICAL
PAGE_SIZE = 20

# Directory paths (relative to project root)
# Good for standardizing where things are stored
DATA_DIR = "data/"
LOG_DIR = "logs/"

# You can also define functions or classes if your config is complex
class Settings:
    def __init__(self):
        self.max_retries = 3
        self.timeout_seconds = 10

NETWORK_SETTINGS = Settings()

# Example of loading environment-specific settings (better done with ENV var switching)
# if ENV == "production":
#    DEBUG_MODE = False
#    LOG_LEVEL = "ERROR"