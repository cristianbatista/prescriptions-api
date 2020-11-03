from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Environment
    ENV: str = "development"

    # Project
    PROJECT_NAME: str = "Prescriptions API"

    # Database
    POSTGRE_URL: str = "postgresql+psycopg2://admin:pass@localhost:5432/test"

    # Security
    ALLOWED_HOSTS: List[str] = ["*"]

    # Dependencies APIs
    PATIENTS_API_URL: str = "http:url-api.com"
    PATIENTS_API_TOKEN_AUTH: str = "Bearer token"
    PATIENTS_API_MAX_RETRY: int = 2
    PATIENTS_API_TIMEMOUT: float = 3

    PHYSICIANS_API_URL: str = "http:url-api.com"
    PHYSICIANS_API_TOKEN_AUTH: str = "Bearer token"
    PHYSICIANS_API_MAX_RETRY: int = 2
    PHYSICIANS_API_TIMEMOUT: float = 4

    CLINICS_API_URL: str = "http:url-api.com"
    CLINICS_API_TOKEN_AUTH: str = "Bearer token"
    CLINICS_API_MAX_RETRY: int = 5
    CLINICS_API_TIMEMOUT: float = 6

    METRICS_API_URL: str = "http:url-api.com"
    METRICS_API_TOKEN_AUTH: str = "Bearer token"
    METRICS_API_MAX_RETRY: int = 5
    METRICS_API_TIMEMOUT: float = 5


settings = Settings()
