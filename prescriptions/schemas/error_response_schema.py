from pydantic import BaseModel


class ErrorDto(BaseModel):
    message: str
    code: str


class ErrorResponseDto(BaseModel):
    error: ErrorDto
