from pydantic import BaseModel

from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema


class CreatePrescriptionSchema(BaseModel):
    clinic: ClinicSchema
    physician: PhysicianSchema
    patient: PatientSchema
    text: str
