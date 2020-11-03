from unittest.mock import AsyncMock, patch

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


@patch.object(
    PrescriptionService,
    "create_prescription",
    AsyncMock(return_value=mock_prescription_schema()),
)
def test_prescriptions_success(client):
    body = {
        "clinic": {"id": 1},
        "physician": {"id": 4},
        "patient": {"id": 56},
        "text": "Dipirona ao dormir - 30 gotas quando sentir dor",
    }

    response = client.post("/prescriptions", headers={}, json=body)
    assert response.status_code == 201
