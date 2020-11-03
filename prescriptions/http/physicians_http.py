import aiohttp
from fastapi.logger import logger

from prescriptions.config import settings
from prescriptions.exception.exceptions import PhysicianNotFound, PhysiciansHttpError


class PhysiciansHttp:
    async def get(self, id: int) -> dict:
        retry_quantity = 0
        retry = True
        response = None

        while retry:
            try:
                timeout = aiohttp.ClientTimeout(total=settings.PHYSICIANS_API_TIMEMOUT)
                async with aiohttp.ClientSession() as session:
                    url = f"{settings.PHYSICIANS_API_URL}/physicians/{id}"
                    headers = {
                        "Autorization": settings.PHYSICIANS_API_TOKEN_AUTH,
                        "Content-Type": "application/json",
                    }
                    async with session.get(
                        url, headers=headers, timeout=timeout
                    ) as response:

                        data = await response.json()
            except Exception as ex:
                logger.error(f"[PhysiciansHttp.get] {str(ex)}")

            retry_quantity += 1

            if response and response.status == 200:
                return data

            if response and response.status == 404:
                logger.error(
                    f"[PhysiciansHttp.get] {PhysicianNotFound().message}, id: {id}"
                )
                raise PhysicianNotFound()

            if retry_quantity > settings.PHYSICIANS_API_MAX_RETRY:
                retry = False

        if not retry:
            physicians_http_ex = PhysiciansHttpError()
            logger.error(f"[PatientsHttp.get] {physicians_http_ex}")
            raise physicians_http_ex
