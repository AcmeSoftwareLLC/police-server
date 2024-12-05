from pydantic import BaseModel


class SocketMessageModel[T: BaseModel](BaseModel):
    event: str
    data: T
