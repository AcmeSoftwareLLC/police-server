from fastapi import Request, status
from fastapi.security import HTTPBearer
from hashlib import sha256

from src.utils.api_exception import APIException


class AuthBearer(HTTPBearer):
    def __init__(self):
        super().__init__()

    async def __call__(self, request: Request):
        authorization = request.headers.get("Authorization")
        if not authorization:
            raise APIException(
                "Oops! We couldn't find your authentication token. Please make sure to include it in the request.",
                status.HTTP_401_UNAUTHORIZED,
            )

        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise APIException(
                "Hmm, there seems to be an issue with the format of your token. Please ensure it's in the form of 'Bearer <token>'.",
            )

        if not self.validate_token(token):
            raise APIException(
                "Something went wrong! The provided token is not valid. Please check and try again.",
                status.HTTP_401_UNAUTHORIZED,
            )

        return await super().__call__(request)

    def validate_token(self, token: str):
        return token == sha256("acmesoftwarellc".encode()).hexdigest()
