import pytest
from asynctest import CoroutineMock
from mock import patch

from prescriptions.exception.exceptions import PatientsHttpError
from prescriptions.http.patients_http import PatientsHttp


class TestPatientsHttp:
    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_patient_by_id_success(
        self, mock_aiohttp_get, response_aiohttp_get_success
    ):
        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=response_aiohttp_get_success
        )
        mock_aiohttp_get.return_value.__aenter__.return_value.status = 200

        patients_http = PatientsHttp()
        response = await patients_http.get(1)
        assert isinstance(response, dict)

    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_patient_by_id_error(
        self, mock_aiohttp_get, response_aiohttp_get_success
    ):
        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=PatientsHttpError
        )

        with pytest.raises(PatientsHttpError) as ex:
            patients_http = PatientsHttp()
            await patients_http.get(1)
            assert isinstance(ex, PatientsHttpError)
