from pydantic import BaseModel


class PatientSchema(BaseModel):
    id: int
