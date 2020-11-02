from typing import Optional

from pydantic import BaseModel


class ClinicSchema(BaseModel):
    id: Optional[int]
