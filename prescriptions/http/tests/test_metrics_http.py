import pytest
from asynctest import CoroutineMock
from mock import patch

from prescriptions.exception.exceptions import MetricsHttpError
from prescriptions.http.metrics_http import MetricsHttp


class TestMetricsHttp:
    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.post")
    async def test_post_metrics_success(
        self, mock_aiohttp_post, mock_response_metrics_http_post
    ):
        mock_aiohttp_post.return_value.__aenter__.return_value.json = CoroutineMock(
            return_value=mock_response_metrics_http_post
        )
        mock_aiohttp_post.return_value.__aenter__.return_value.status = 201

        body = {
            "clinic_id": 1,
            "clinic_name": "Clínica A",
            "physician_id": 1,
            "physician_name": "José",
            "physician_crm": "SP293893",
            "patient_id": 1,
            "patient_name": "Rodrigo",
            "patient_email": "rodrigo@gmail.com",
            "patient_phone": "(16)998765625",
        }
        metrics_http = MetricsHttp()
        response = await metrics_http.post(body)

        assert isinstance(response, dict)
        assert response["clinic_name"] == "Clínica A"
        assert response["patient_email"] == "rodrigo@gmail.com"

    @pytest.mark.asyncio
    @patch("aiohttp.ClientSession.post")
    async def test_post_metrics_excpetion(
        self, mock_aiohttp_post, mock_response_metrics_http_post
    ):
        mock_aiohttp_post.return_value.__aenter__.return_value.json = CoroutineMock(
            side_effect=MetricsHttpError
        )

        body = {
            "clinic_id": 1,
            "clinic_name": "Clínica A",
            "physician_id": 1,
            "physician_name": "José",
            "physician_crm": "SP293893",
            "patient_id": 1,
            "patient_name": "Rodrigo",
            "patient_email": "rodrigo@gmail.com",
            "patient_phone": "(16)998765625",
        }

        with pytest.raises(MetricsHttpError) as ex:
            metrics_http = MetricsHttp()
            await metrics_http.post(body)

        assert ex.typename == "MetricsHttpError"
