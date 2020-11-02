import asyncio

import asynctest as asynctest
from unittest.mock import patch, Mock
import pytest

from prescriptions.http.patients_http import PatientsHttp
from prescriptions.models.prescription_model import PrescriptionModel
from prescriptions.repository.postgre_prescription_repository import (
    PostgrePrescriptionRepository,
)
from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema
from prescriptions.schemas.prescription_schema import PrescriptionSchema
from prescriptions.service.prescription_service import PrescriptionService


class TestPrescriptionService:
    @pytest.mark.asyncio
    @patch("prescriptions.infrastructure.postgre.create_session_local")
    async def test_create_prescription_success(
        self,
        mock_create_session_local,
        mock_patients_http_get_sucess,
        mock_physicians_http_get_sucess,
        mock_clinics_http_get_sucesss,
        mock_prescription_repo_create
    ):

        dto = CreatePrescriptionSchema(
            clinic=ClinicSchema(id=2),
            physician=PhysicianSchema(id=3),
            patient=PatientSchema(id=45),
            text="Medicamento Capsula 1x ao dia",
        )

        service = PrescriptionService(
            mock_create_session_local,
            mock_prescription_repo_create,
            mock_patients_http_get_sucess,
            mock_physicians_http_get_sucess,
            mock_clinics_http_get_sucesss
        )

        result = await service.create_prescription(dto)

        assert isinstance(result, PrescriptionSchema)
        assert result.id == 100

    @pytest.mark.asyncio
    @patch("prescriptions.infrastructure.postgre.create_session_local")
    async def test_create_prescription_clinic_id_none_success(
            self,
            mock_create_session_local,
            mock_patients_http_get_sucess,
            mock_physicians_http_get_sucess,
            mock_clinics_http_get_sucesss,
            mock_prescription_repo_create

    ):
        dto = CreatePrescriptionSchema(
            clinic=ClinicSchema(id=456),
            physician=PhysicianSchema(id=3),
            patient=PatientSchema(id=45),
            text="Medicamento Capsula 1x ao dia",
        )

        service = PrescriptionService(
            mock_create_session_local,
            mock_prescription_repo_create,
            mock_patients_http_get_sucess,
            mock_physicians_http_get_sucess,
            mock_clinics_http_get_sucesss
        )
        result = await service.create_prescription(dto)

        assert isinstance(result, PrescriptionSchema)
        assert result.id == 100


    @pytest.mark.asyncio
    @patch("prescriptions.infrastructure.postgre.create_session_local")
    async def test_create_prescription_exception(
        self,
        mock_create_session_local,
        mock_patients_http_get_sucess,
        mock_physicians_http_get_sucess,
        mock_clinics_http_get_sucesss,
        mock_prescription_repo_create_exception
    ):

        with pytest.raises(RuntimeError) as ex:
            dto = CreatePrescriptionSchema(
                clinic=ClinicSchema(id=123),
                physician=PhysicianSchema(id=456),
                patient=PatientSchema(id=45),
                text="Medicamento Capsula 1x ao dia",
            )

            service = PrescriptionService(
                mock_create_session_local,
                mock_prescription_repo_create_exception,
                mock_patients_http_get_sucess,
                mock_physicians_http_get_sucess,
                mock_clinics_http_get_sucesss
            )
            await service.create_prescription(dto)

            assert str(ex.value) == "Error I/O database"
