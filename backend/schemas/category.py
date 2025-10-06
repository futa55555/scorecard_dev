# backend/schemas/category.py

from pydantic import BaseModel, ConfigDict
from . import common

class CategorySummary(BaseModel):
    category_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class CategorySummaries(list[CategorySummary]):
    pass


class CategorySummariesResponse(common.CommonResponse[CategorySummaries]):
    pass
