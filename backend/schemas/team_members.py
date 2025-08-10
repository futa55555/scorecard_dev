# backend/schemas/team_members.py

from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date
from backend.models import PrefectureEnum, DominantHandEnum, RoleEnum


class MemberBase(BaseModel):
    name: str
    pitching_side: Optional[DominantHandEnum] = None
    batting_side: Optional[DominantHandEnum] = None
    photo_url: Optional[HttpUrl] = None
    height_cm: Optional[int] = None
    weight_kg: Optional[int] = None
    birthday: Optional[date] = None
    

class MemberProfileBase(BaseModel):
    since_date: Optional[date] = None
    until_date: Optional[date] = None
    uniform_number: Optional[int] = None
    role: Optional[RoleEnum] = None
    

class MemberWithProfiles(MemberBase):
    member_profiles: List[MemberProfileBase]


class TeamBase(BaseModel):
    id: int
    name: str
    is_myteam: bool
    short_name: Optional[str] = None
    prefecture: Optional[PrefectureEnum] = None
    league: Optional[str] = None
    color: Optional[str] = None


class TeamMembersCreate(BaseModel):
    members: List[MemberBase]


class TeamMembersResponse(TeamBase):
    member_with_profiles: List[MemberWithProfiles]
    
    class Config:
        from_attributes = True
