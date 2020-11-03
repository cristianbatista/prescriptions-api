import pytest
from asynctest import CoroutineMock
from mock import patch

from prescriptions.exception.exceptions import ClinicsHttpError
from prescriptions.http.clinics_http import ClinicsHttp


class TestClinicsHttp:

    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_clinics_by_id_success(
        self, mock_aiohttp_get, response_aiohttp_get_clinics_success
    ):
        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=response_aiohttp_get_clinics_success
        )
        mock_aiohttp_get.return_value.__aenter__.return_value.status = 200

        clinics_http = ClinicsHttp()
        response = await clinics_http.get(1)
        assert isinstance(response, dict)
        assert response["name"] == "Clinica Saúde"


    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_clinics_by_id_not_found(
        self, mock_aiohttp_get, response_aiohttp_get_clinics_success
    ):

        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=response_aiohttp_get_clinics_success
        )
        mock_aiohttp_get.return_value.__aenter__.return_value.status = 404

        clinics_http = ClinicsHttp()
        response = await clinics_http.get(1)

        assert response is None


    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_patient_by_id_error(
        self, response_aiohttp_get_clinics_success
    ):
        response_aiohttp_get_clinics_success.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=ClinicsHttpError
        )

        with pytest.raises(ClinicsHttpError) as ex:
            clinics_http = ClinicsHttp()
            await clinics_http.get(1)

        assert ex.typename == "ClinicsHttpError"
