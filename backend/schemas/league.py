# backend/schemas/league.py

from pydantic import BaseModel, ConfigDict
from . import common, category, tournament, user
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .team import TeamBase

class LeagueBase(BaseModel):
    league_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class LeagueSummary(BaseModel):
    league_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class LeagueSummariesResponse(common.CommonResponse[list[LeagueSummary]]):
    pass


class LeagueListItem(LeagueBase):
    categories: list[category.CategoryBase]
    teams: list["TeamBase"]

    model_config = ConfigDict(from_attributes=True)


class LeagueListResponse(common.CommonResponse[list[LeagueListItem]]):
    pass


class LeagueDetail(LeagueBase):
    chief_admin_user: user.UserBase
    categories: list[category.CategoryBase]
    tournaments: list[tournament.TournamentBase]
    admin_users: list[user.UserBase]
    teams: list["TeamBase"]

    model_config = ConfigDict(from_attributes=True)


class LeagueDetailResponse(common.CommonResponse[LeagueDetail]):
    pass
