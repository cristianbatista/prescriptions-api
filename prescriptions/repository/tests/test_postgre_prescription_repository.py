from unittest.mock import patch

import pytest

from prescriptions.models.prescription_model import PrescriptionModel
from prescriptions.repository.postgre_prescription_repository import (
    PostgrePrescriptionRepository,
)
from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema

add_record_return = PrescriptionModel(
    id=100, clinic_id=2, physician_id=15, patient_id=34, text="Paracetamol 2x ao dia"
)


class TestPostgrePrescriptionRepository:
    @pytest.mark.asyncio
    @patch("prescriptions.infrastructure.postgre.declarative_base")
    @patch("prescriptions.infrastructure.postgre.create_engine_db")
    @patch("prescriptions.infrastructure.postgre.create_session_local")
    async def test_create_prescription_success(
        self, mock_create_session_local, mock_create_engine_db, mock_declarative_base
    ):
        dto = CreatePrescriptionSchema(
            clinic=ClinicSchema(id=123),
            physician=PhysicianSchema(id=456),
            patient=PatientSchema(id=45),
            text="Medicamento Capsula 1x ao dia",
        )

        service = PostgrePrescriptionRepository()
        result = await service.create(dto, mock_create_session_local)

        assert isinstance(result, PrescriptionModel)
