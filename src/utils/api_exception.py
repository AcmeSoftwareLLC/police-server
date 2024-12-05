from typing import cast
from fastapi import Request
from fastapi.responses import JSONResponse


class APIException(Exception):
    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code

    @staticmethod
    async def handler(_: Request, exc: Exception) -> JSONResponse:
        exception = cast(APIException, exc)

        return JSONResponse(
            status_code=exception.status_code,
            content={
                "message": exception.message,
            },
        )
