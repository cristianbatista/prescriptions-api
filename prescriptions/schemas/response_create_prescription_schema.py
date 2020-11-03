from pydantic import BaseModel

from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema


class RegisterPrescriptionSchema(BaseModel):
    id: int
    clinic: ClinicSchema
    physician: PhysicianSchema
    patient: PatientSchema
    text: str


class ResponseCreatePrescriptionSchema(BaseModel):
    data: RegisterPrescriptionSchema
