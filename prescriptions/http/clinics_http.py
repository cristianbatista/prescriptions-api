from typing import Optional
from fastapi.logger import  logger
import aiohttp

from prescriptions.config import settings
from prescriptions.exception.exceptions import PhysiciansHttpError, PhysicianNotFound, ClinicsHttpError


class ClinicsHttp:

    async def get(self, id: int) -> Optional[dict]:
        retry_quantity = 0
        retry = True
        response = None

        while retry:
            try:
                timeout = aiohttp.ClientTimeout(total=settings.PHYSICIANS_API_TIMEMOUT)
                async with aiohttp.ClientSession() as session:
                    url = f"{settings.PHYSICIANS_API_URL}/clinics/{id}"
                    headers = {
                        "Autorization": settings.PHYSICIANS_API_TOKEN_AUTH,
                        "Content-Type": "application/json"
                    }
                    async with session.get(
                        url, headers=headers, timeout=timeout
                    ) as response:

                        data = await response.json()
            except Exception as ex:
                logger.error(f"[ClinicsHttp.get] {str(ex)}")

            retry_quantity += 1

            if response and response.status == 200:
                return data

            if response and response.status == 404:
                logger.warn(f"[ClinicsHttp.get] Clinic not found, id: {id}")
                return None

            if retry_quantity > settings.PHYSICIANS_API_MAX_RETRY:
                retry = False

        if not retry:
            clinic_http_ex = ClinicsHttpError()
            logger.error(f"[PatientsHttp.get] {clinic_http_ex}")
            raise clinic_http_ex
