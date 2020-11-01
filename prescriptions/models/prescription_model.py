from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from prescriptions.infrastructure.postgre import Base, engine


class PrescriptionModel(Base):
    __tablename__ = "prescription"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer)
    physician_id = Column(Integer)
    patient_id = Column(Integer)
    text = Column(String(255))


Session = sessionmaker(engine)
session = Session()
Base.metadata.create_all(engine)
