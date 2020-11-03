import pytest
from starlette.testclient import TestClient

from prescriptions.api.main import app


@pytest.fixture()
def client():
    return TestClient(app)
