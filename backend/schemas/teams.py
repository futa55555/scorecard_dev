# backend/schemas/teams.py

from pydantic import BaseModel
from typing import Optional
from backend.models import PrefectureEnum


# 共通フィールド
class TeamBase(BaseModel):
    name: str
    short_name: Optional[str] = None
    prefecture: Optional[PrefectureEnum] = None
    league: Optional[str] = None
    color: Optional[str] = None


# POST追加用（リクエスト）
class TeamCreate(TeamBase):
    pass


# レスポンス用
class TeamResponse(TeamBase):
    id: int
    is_myteam: bool

    class Config:
        from_attributes=True
