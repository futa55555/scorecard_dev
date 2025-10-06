# backend/schemas/location.py

from pydantic import BaseModel, ConfigDict

class LocationSummary(BaseModel):
    location_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
