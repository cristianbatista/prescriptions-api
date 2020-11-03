from unittest.mock import Mock

import pytest
from starlette.testclient import TestClient

from prescriptions.api.main import app
from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema
from prescriptions.schemas.prescription_schema import PrescriptionSchema
from prescriptions.service.prescription_service import PrescriptionService


def mock_prescription_schema():
    return PrescriptionSchema(
        id=1,
        clinic=ClinicSchema(id=1),
        physician=PhysicianSchema(id=4),
        patient=PatientSchema(id=56),
        text="Dipirona ao dormir - 30 gotas quando sentir dor",
    )


@pytest.fixture()
def client():
    app.dependency_overrides[PrescriptionService] = mock_prescripton_service_success
    return TestClient(app)


def mock_prescripton_service_success():
    mock_prescripton_service = Mock(PrescriptionService())
    mock_prescripton_service.create_prescription.return_value = (
        mock_prescription_schema()
    )
    return mock_prescripton_service
