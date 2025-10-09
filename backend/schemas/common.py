# backend/schemas/common.py

from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class CommonResponse(BaseModel, Generic[T]):
    status: str
    data: T
    message: str
    code: None = None
