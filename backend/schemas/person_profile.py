# backend/schemas/person_profile.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import user
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .team import TeamBase

class PersonProfileBase(BaseModel):
    person_profile_id: int
    uniform_number: int
    role: models.RoleEnum
    since_date: date
    until_date: date

    model_config = ConfigDict(from_attributes=True)


class PersonProfileListItem(PersonProfileBase):
    team: "TeamBase"
    created_by_user: user.UserBase

    model_config = ConfigDict(from_attributes=True)
