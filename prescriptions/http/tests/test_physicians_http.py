import pytest
from asynctest import CoroutineMock
from mock import patch

from prescriptions.exception.exceptions import PhysicianNotFound, PhysiciansHttpError
from prescriptions.http.physicians_http import PhysiciansHttp


class TestPhysiciansHttp:

    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_physicians_by_id_success(
        self, mock_aiohttp_get, response_aiohttp_get_physicians_success
    ):
        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=response_aiohttp_get_physicians_success
        )
        mock_aiohttp_get.return_value.__aenter__.return_value.status = 200

        physicians_http = PhysiciansHttp()
        response = await physicians_http.get(1)
        assert isinstance(response, dict)
        assert response["name"] == "Dr. Jose Silva"

    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_physicians_by_id_not_found(
        self, mock_aiohttp_get, response_aiohttp_get_physicians_success
    ):

        mock_aiohttp_get.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=response_aiohttp_get_physicians_success
        )
        mock_aiohttp_get.return_value.__aenter__.return_value.status = 404

        with pytest.raises(PhysicianNotFound) as ex:

            physicians_http = PhysiciansHttp()
            await physicians_http.get(1)

        assert ex.typename == "PhysicianNotFound"


    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.get")
    async def test_get_patient_by_id_error(
        self, response_aiohttp_get_physicians_success
    ):
        response_aiohttp_get_physicians_success.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=PhysiciansHttpError
        )

        with pytest.raises(PhysiciansHttpError) as ex:
            physicians_http = PhysiciansHttp()
            await physicians_http.get(1)

        assert ex.typename == "PhysiciansHttpError"
