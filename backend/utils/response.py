# backend/utils/response.py

from typing import TypeVar, Generic
from backend.schemas.common import CommonResponse

T = TypeVar("T")

def get_response(
    data: T,
    target: str
) -> CommonResponse[T]:
    return CommonResponse[T](
        status="success",
        data=data,
        message=f"{target.title()} retrieved successfully.",
        code=None
    )
