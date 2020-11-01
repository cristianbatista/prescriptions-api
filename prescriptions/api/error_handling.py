from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from prescriptions.exception.base_exception import ExceptionBase
from prescriptions.exception.exception import MalformedRequestError
from prescriptions.schemas.error_response_schema import ErrorDto, ErrorResponseDto


def init_error_handling(app):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        error_response_dto = ErrorResponseDto(
            error=ErrorDto(
                message=MalformedRequestError().message,
                code=MalformedRequestError().code,
            )
        )
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=error_response_dto.dict(),
        )

    @app.exception_handler(ExceptionBase)
    async def base_exception_handler(request: Request, exc: ExceptionBase):
        error_response_dto = ErrorResponseDto(
            error=ErrorDto(message=exc.message, code=exc.code)
        )
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=error_response_dto.dict(),
        )

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        error_response_dto = ErrorResponseDto(error=ErrorDto(message=str(exc), code=0))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response_dto.dict(),
        )
