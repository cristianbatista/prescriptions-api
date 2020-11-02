import pytest


@pytest.fixture()
def response_aiohttp_get_success():
    data = {
        "id": "1",
        "name": "Fulano de Tal",
        "email": "seuemail@email.com",
        "phone": "55-12365-1",
    }
    return data
