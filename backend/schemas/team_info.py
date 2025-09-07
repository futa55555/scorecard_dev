# backend/schemas/team_info.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

#-----------------
# for top
#-----------------

class TeamBase(BaseModel):
    name: int
    short_name: int
    is_myteam: bool
    is_favorite: bool
    prefecture: models.PrefectureEnum
    league: str
    photo_url: str
    color: str
    

class ForTeamMember(BaseModel):
    grade: models.GradeEnum
    player_count: int
    manager_count: int
    analyst_count: int
    
    
class TeamMember(BaseModel):
    grade_count: List[ForTeamMember]


class ForRecentGame(BaseModel):
    my_team_score: int
    opposite_team_score: int
    win_lose: str
    opposite_team_short_name: str
    date: date
    tournament: str
    

class RecentGame(BaseModel):
    game: List[ForRecentGame]


#-----------------
# for members
#-----------------

class ForAllMembers(BaseModel):
    person_id: int
    role: models.RoleEnum
    uniform_number: int
    name: str
    throw: models.DominantHandEnum
    bat: models.DominantHandEnum
    height_cm: int
    weight_kg: int
    prefecture: models.PrefectureEnum
    birthday: date
    grade: models.GradeEnum
    position_type: models.PositionTypeEnum


class AllMembers(BaseModel):
    team_name: str
    member: List[ForAllMembers]
    

#-----------------
# for member_detail
#-----------------

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


class MemberPage(BaseModel):
    role: models.RoleEnum
    uniform_number: int
    name: str
    throw: models.DominantHandEnum
    bat: models.DominantHandEnum
    height_cm: int
    weight_kg: int
    prefecture: models.PrefectureEnum
    birthday: date
    grade: models.GradeEnum
    position_type: models.PositionTypeEnum
    batter_stats: BatterStats
    pitcher_stats: PitcherStats
