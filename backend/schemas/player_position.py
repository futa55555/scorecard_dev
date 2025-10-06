# backend/schemas/player_position.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import user, person
from datetime import date

class PlayerPositionItem(BaseModel):
    player_position_id: int
    position_type: models.PositionTypeEnum
    since_date: date
    until_date: date
    person: person.PersonSummary
    created_by_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)
