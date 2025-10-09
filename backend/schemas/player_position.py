# backend/schemas/player_position.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import user
from datetime import date

class PlayerPositionBase(BaseModel):
    player_position_id: int
    position_type: models.PositionTypeEnum
    since_date: date
    until_date: date

    model_config = ConfigDict(from_attributes=True)


class PlayerPositionListItem(PlayerPositionBase):
    created_by_user: user.UserBase

    model_config = ConfigDict(from_attributes=True)
