from sqlalchemy import Column, Integer, String
from prescriptions.infrastructure.postgre import declarative_base

Base = declarative_base()


class PrescriptionModel(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer)
    physician_id = Column(Integer)
    patient_id = Column(Integer)
    text = Column(String(255))
