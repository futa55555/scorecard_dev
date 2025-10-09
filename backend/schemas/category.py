# backend/schemas/category.py

from pydantic import BaseModel, ConfigDict
from . import common

class CategoryBase(BaseModel):
    category_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class CategorySummary(BaseModel):
    category_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class CategorySummariesResponse(common.CommonResponse[list[CategorySummary]]):
    pass
