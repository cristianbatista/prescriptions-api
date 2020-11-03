import pytest


@pytest.fixture()
def response_aiohttp_get_patient_success():
    return {
        "id": "1",
        "name": "Fulano de Tal",
        "email": "seuemail@email.com",
        "phone": "55-12365-1",
    }


@pytest.fixture()
def response_aiohttp_get_physicians_success():
    return {
        "id": "3",
        "name": "Dr. Jose Silva",
        "crm": "SPE12345"
    }


@pytest.fixture()
def response_aiohttp_get_clinics_success():
    return {
        "id": "4",
        "name": "Clinica Saúde"
    }


@pytest.fixture()
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
        "patient_name": "Rodrigo"
    }