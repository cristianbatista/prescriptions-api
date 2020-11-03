from fastapi import APIRouter, Depends
from starlette import status

from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema
from prescriptions.schemas.response_create_prescription_schema import (
    RegisterPrescriptionSchema,
    ResponseCreatePrescriptionSchema,
)
from prescriptions.service.prescription_service import PrescriptionService

router = APIRouter()


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_prescription(
    payload: CreatePrescriptionSchema, service: PrescriptionService = Depends()
) -> ResponseCreatePrescriptionSchema:
    prescription_schema = await service.create_prescription(payload)

    return ResponseCreatePrescriptionSchema(
        data=RegisterPrescriptionSchema(**prescription_schema.dict())
    )
