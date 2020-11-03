import json

import aiohttp
from fastapi.logger import logger
from prescriptions.config import settings
from prescriptions.exception.exceptions import PhysiciansHttpError, PhysicianNotFound, MetricsHttpError
from prescriptions.schemas.create_metrics_schema import CreateMetricsSchema


class MetricsHttp:

    async def post(self, body: dict) -> dict:
        retry_quantity = 0
        retry = True
        response = None

        while retry:
            try:
                timeout = aiohttp.ClientTimeout(total=settings.METRICS_API_TIMEMOUT)
                async with aiohttp.ClientSession() as session:
                    url = f"{settings.METRICS_API_URL}/metrics"
                    headers = {
                        "Autorization": settings.METRICS_API_TOKEN_AUTH,
                        "Content-Type": "application/json"
                    }
                    async with session.post(
                        url, data=json.dumps(body), headers=headers, timeout=timeout
                    ) as response:

                        data = await response.json()
            except Exception as ex:
                logger.error(f"[MetricsHttp.post] {str(ex)}")

            retry_quantity += 1

            if response and response.status == 201:
                return data

            if response and response.status != 201:
                logger.error(f"[MetricsHttp.post] Create metrics failed - status: {response.status}")

            if retry_quantity > settings.METRICS_API_MAX_RETRY:
                retry = False

        if not retry:
            metrics_http_ex = MetricsHttpError()
            logger.error(f"[PatientsHttp.post] {metrics_http_ex}")
            raise metrics_http_ex
