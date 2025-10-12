# backend/schemas/team.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import common, category, league, location, tournament, user, person
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import GameListItem

class TeamBase(BaseModel):
    team_id: int
    name: str
    short_name: str
    prefecture: models.PrefectureEnum

    model_config = ConfigDict(from_attributes=True)


class TeamListItem(TeamBase):
    categories: list[category.CategoryBase]
    league: league.LeagueBase

    model_config = ConfigDict(from_attributes=True)


class TeamListResponse(common.CommonResponse[list[TeamListItem]]):
    pass


class TeamListWithPage(BaseModel):
    teams: list[TeamListItem]
    current_page: int
    total_page: int


class TeamListWithPageResponse(common.CommonResponse[TeamListWithPage]):
    pass


class TeamDetail(TeamBase):
    chief_admin_user: user.UserBase
    league: league.LeagueBase
    categories: list[category.CategoryBase]
    locations: list[location.LocationBase]
    tournaments: list[tournament.TournamentBase]
    admin_users: list[user.UserBase]
    active_people: list[person.PersonListItem]
    games: list["GameListItem"]

    model_config = ConfigDict(from_attributes=True)


class TeamDetailResponse(common.CommonResponse[TeamDetail]):
    pass
