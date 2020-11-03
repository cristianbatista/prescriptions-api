from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from prescriptions.config import settings


def create_engine_db():
    engine = create_engine(settings.POSTGRE_URL)
    return engine


def create_session_local():
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=create_engine_db()
    )
    db = SessionLocal()
    return db
