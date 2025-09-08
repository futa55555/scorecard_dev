# backend/schemas/person_info.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models


#-----------------
# for person_info
#-----------------

class ForPerson(BaseModel):
    person_id: int
    role: models.RoleEnum
    uniform_number: int
    name: str
    pitching_side: models.DominantHandEnum
    batting_side: models.DominantHandEnum
    height_cm: int
    weight_kg: int
    birthday: date
    grade: models.GradeEnum
    position_type: models.PositionTypeEnum
    

class BatterStats(BaseModel):
    average: float
    atbat: int
    hit: int
    rbi: int
    homerun: int
    steal: int
    
    
class PitcherStats(BaseModel):
    era: float
    win: int
    lose: int
    hold: int
    save: int
    strikeout: int


class PersonPage(BaseModel):
    person: ForPerson
    batter_stats: BatterStats
    pitcher_stats: PitcherStats
