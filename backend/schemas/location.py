# backend/schemas/location.py

from pydantic import BaseModel, ConfigDict
from backend import models

class LocationBase(BaseModel):
    location_id: int
    name: str
    prefecture: models.PrefectureEnum

    model_config = ConfigDict(from_attributes=True)
