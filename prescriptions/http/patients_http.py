import aiohttp
from fastapi.logger import logger
from prescriptions.config import settings
from prescriptions.exception.exceptions import PatientsHttpError, PatientNotFound


class PatientsHttp:

    async def get(self, id: int) -> dict:
        retry_quantity = 0
        retry = True
        response = None

        while retry:
            try:
                timeout = aiohttp.ClientTimeout(total=settings.PATIENTS_API_TIMEMOUT)
                async with aiohttp.ClientSession() as session:
                    url = f"{settings.PATIENTS_API_URL}/patients/{id}"
                    headers = {
                        "Autorization": settings.PATIENTS_API_TOKEN_AUTH,
                        "Content-Type": "application/json"
                    }
                    async with session.get(
                        url, headers=headers, timeout=timeout
                    ) as response:

                        data = await response.json()
            except Exception as ex:
                logger.error(f"[PatientsHttp.get] {str(ex)}")

            retry_quantity += 1

            if response and response.status == 200:
                return data

            if response and response.status == 404:
                not_found_ex = PatientNotFound()
                logger.error(f"[PatientsHttp.get] {not_found_ex.message}, id: {id}")
                raise not_found_ex

            if retry_quantity > settings.PATIENTS_API_MAX_RETRY:
                retry = False

        if not retry:
            patient_http_ex = PatientsHttpError()
            logger.error(f"[PatientsHttp.get] {patient_http_ex}")
            raise patient_http_ex
