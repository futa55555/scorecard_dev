# backend/schemas/game_list.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

class GameWithTeamName(BaseModel):
    id: int
    top_team_short_name: str
    bottom_team_short_name: str
    date: date
    start_time: Optional[time]
    end_time: Optional[time]
    tournament: Optional[str]
    location: Optional[str]
    status: models.GameStatusEnum

class GameWithTeamNameList(BaseModel):
    game_list: List[GameWithTeamName]
