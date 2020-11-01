from pydantic import BaseModel


class ClinicSchema(BaseModel):
    id: int
