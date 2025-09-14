"""
Small config loader. Uses environment variables (and .env if present).
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_VERSION = os.getenv("API_VERSION", "v1.0")
    DATABASE_URL = os.getenv("DATABASE_URL", "")

settings = Settings()

