# backend/schemas/game_info.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

class GameBase(BaseModel):
    top_team_id: int
    bottom_team_id: int
    top_team_short_name: str
    bottom_team_short_name: str
    date: date
    start_time: time
    end_time: time
    tournament: str
    location: str
    status: models.GameStatusEnum


class InningScore(BaseModel):
    top_team_short_name: str
    bottom_team_short_name: str
    top_team_inning_score: List[int]
    bottom_team_inning_score: List[int]
    top_team_total_score: int
    bottom_team_total_score: int
    top_team_hit: int
    bottom_team_hit: int

