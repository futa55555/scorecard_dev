# backend/schemas/shared.py

from pydantic import BaseModel
from typing import Optional

class MemberBase(BaseModel):
    id: int
    name: str
    uniform_number: Optional[int]
    team_id: int
    
    model_config = {
        "from_attributes": True
    }

class GameBase(BaseModel):
    id: int
    team1_id: int
    team2_id: int
    score_team1: int
    score_team2: int
    current_inning: int
    is_top: bool
    is_offense_team1: bool
    outs: int
    ball_count: int
    strike_count: int
    
    model_config = {
        "from_attributes": True
    }

class PitchEventBase(BaseModel):
    id: int
    atbat_id: int
    result: str
    ball_count_before: int
    strike_count_before: int
    outs_before: int
    ball_count_after: int
    strike_count_after: int
    outs_after: int
    
    model_config = {
        "from_attributes": True
    }

class AdvanceEventBase(BaseModel):
    id: int
    member_id: int
    base_from: int
    base_to: int
    type: str
    result: Optional[str]
    
    model_config = {
        "from_attributes": True
    }
