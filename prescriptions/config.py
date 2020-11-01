from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Environment
    ENV: str = "development"

    # Project
    PROJECT_NAME: str = "Prescrições"

    # Database
    # POSTGRE_URL: str = "postgresql+psycopg2://admin:pass@localhost:5432/test"
    POSTGRE_URL: str = "postgresql+psycopg2://usr_prescription:secret@localhost:5432/prescription_db"
    # Security
    ALLOWED_HOSTS: List[str] = ["*"]


settings = Settings()
