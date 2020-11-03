import asyncio

import asynctest
import pytest

from prescriptions.http.metrics_http import MetricsHttp
from prescriptions.http.patients_http import PatientsHttp
from prescriptions.models.prescription_model import PrescriptionModel
from prescriptions.repository.postgre_prescription_repository import (
    PostgrePrescriptionRepository,
)


def mock_add_record():
    return PrescriptionModel(
        id=100,
        clinic_id=2,
        physician_id=15,
        patient_id=34,
        text="Paracetamol 2x ao dia",
    )


def mock_response_patients_http_get():
    return {
        "id": "2",
        "name": "Fulano de Tal",
        "email": "seuemail@email.com",
        "phone": "55-12365-1",
    }


def mock_response_physician_http_get():
    return {"id": "3", "name": "Dr. Jose Silva", "crm": "SPE12345"}


def mock_response_clinic_http_get():
    return {"id": "4", "name": "Clinica Saúde"}


def mock_response_metrics_http_post():
    return {
        "id": "1",
        "clinic_id": 1,
        "clinic_name": "Clínica A",
        "physician_id": 1,
        "physician_name": "José",
        "physician_crm": "SP293893",
        "patient_id": 1,
        "patient_email": "rodrigo@gmail.com",
        "patient_phone": "(16)998765625",
        "patient_name": "Rodrigo",
    }


@pytest.fixture()
def mock_patients_http_get_success():
    mock_patients_http_get = asynctest.Mock(PatientsHttp())
    mock_patients_http_get.get.return_value = asyncio.Future()
    mock_patients_http_get.get.return_value.set_result(
        mock_response_patients_http_get()
    )
    return mock_patients_http_get


@pytest.fixture()
def mock_physicians_http_get_success():
    mock_physicians_http_get = asynctest.Mock(PatientsHttp())
    mock_physicians_http_get.get.return_value = asyncio.Future()
    mock_physicians_http_get.get.return_value.set_result(
        mock_response_physician_http_get()
    )
    return mock_physicians_http_get


@pytest.fixture()
def mock_clinics_http_get_success():
    mock_clinics_http_get = asynctest.Mock(PatientsHttp())
    mock_clinics_http_get.get.return_value = asyncio.Future()
    mock_clinics_http_get.get.return_value.set_result(mock_response_clinic_http_get())
    return mock_clinics_http_get


@pytest.fixture()
def mock_clinics_http_get_not_found():
    mock_clinics_http_get = asynctest.Mock(PatientsHttp())
    mock_clinics_http_get.get.return_value = asyncio.Future()
    mock_clinics_http_get.get.return_value.set_result(None)
    return mock_clinics_http_get


@pytest.fixture()
def mock_metrics_http_post_success():
    mock_metrics_http_post = asynctest.Mock(MetricsHttp())
    mock_metrics_http_post.post.return_value = asyncio.Future()
    mock_metrics_http_post.post.return_value.set_result(mock_response_metrics_http_post)
    return mock_metrics_http_post


@pytest.fixture()
def mock_prescription_repo_create():
    mock_prescripton_repo = asynctest.Mock(PostgrePrescriptionRepository())
    mock_prescripton_repo.create.return_value = asyncio.Future()
    mock_prescripton_repo.create.return_value.set_result(mock_add_record())
    return mock_prescripton_repo


@pytest.fixture()
def mock_prescription_repo_create_exception():
    mock_prescripton_repo = asynctest.Mock(PostgrePrescriptionRepository())
    mock_prescripton_repo.create.side_effect = RuntimeError("Error I/O database")
    return mock_prescripton_repo
