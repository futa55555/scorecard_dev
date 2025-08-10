# backend/schemas/people.py

from pydantic import BaseModel
from typing import Optional
from backend.models import DominantHandEnum
from datetime import date


class PersonBase(BaseModel):
    name: str
    pitching_side: Optional[DominantHandEnum] = None
    batting_side: Optional[DominantHandEnum] = None
    height_cm: Optional[int] = None
    weight_kg: Optional[int] = None
    birthday: Optional[date] = None
    

class PersonResponse(PersonBase):
    id: int
    
    class Config:
        from_attributes=True