from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field

# Generic Type
T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    code: int = Field(..., description="Status code of the response")
    message: str = Field(..., description="Response message")
    data: Optional[T] = Field(None, description="Response data")

    @classmethod
    def success(cls, data: T) -> "APIResponse[T]":
        return cls(code=200, message="Success", data=data)

    @classmethod
    def error(cls, code: int, message: str) -> "APIResponse[None]":
        return cls(code=code, message=message, data=None)
