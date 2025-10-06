# backend/schemas/team.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import common, category, league, location, tournament, user, person, game

class TeamSummary(BaseModel):
    team_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class TeamSummaries(list[TeamSummary]):
    pass


class TeamSummariesResponse(common.CommonResponse[TeamSummaries]):
    pass


class TeamItem(BaseModel):
    team_id: int
    name: str
    short_name: str
    prefecture: models.PrefectureEnum
    chief_admin_user: user.UserSummary
    league: league.LeagueSummary

    model_config = ConfigDict(from_attributes=True)


class TeamList(list[TeamItem]):
    pass


class TeamListResponse(common.CommonResponse[TeamList]):
    pass


class TeamDetail(BaseModel):
    name: str
    short_name: str
    prefecture: models.PrefectureEnum
    chief_admin_user: user.UserSummary
    league: league.LeagueSummary
    categories: list[category.CategorySummary]
    locations: list[location.LocationSummary]
    tournaments: list[tournament.TournamentSummary]
    admin_users: list[user.UserSummary]
    people: list[person.PersonItem]
    games: list[game.GameItem]

    model_config = ConfigDict(from_attributes=True)


class TeamDetailResponse(common.CommonResponse[TeamDetail]):
    pass
