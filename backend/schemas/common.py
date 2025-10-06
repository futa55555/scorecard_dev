# backend/schemas/common.py

from pydantic.generics import GenericModel
from typing import Generic, TypeVar

T = TypeVar("T")

class CommonResponse(GenericModel, Generic[T]):
    status: str
    data: T
    message: str
    code: None = None
