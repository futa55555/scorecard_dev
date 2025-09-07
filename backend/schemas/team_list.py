# backend/schemas/team_list.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

class TeamBase(BaseModel):
    id: int
    name: str
    short_name: str
    is_myteam: bool
    is_favorite: bool
    prefecture: models.PrefectureEnum
    league: str
    photo_url: str
    color: str


class AllTeam(BaseModel):
    team: List[TeamBase]