"""
Application settings configuration.

✅ Uses Pydantic's BaseSettings for type safety and environment variable support.
✅ Automatically loads from a `.env` file if present.
✅ Provides sensible defaults for local development.
"""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load variables from .env into environment before Pydantic reads them
load_dotenv()

class Settings(BaseSettings):
    API_VERSION: str = "v1.0"

    # Database connection URLs
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/anna_sewa"
    DYNAMODB_URL: str = "http://localhost:8000"

    # Pydantic v2 config
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

# Create a single instance to import elsewhere
settings = Settings()

