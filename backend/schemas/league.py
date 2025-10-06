# backend/schemas/league.py

from pydantic import BaseModel, ConfigDict
from . import common, category, tournament, team, user

class LeagueSummary(BaseModel):
    league_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class LeagueSummaries(list[LeagueSummary]):
    pass


class LeagueSummariesResponse(common.CommonResponse[LeagueSummaries]):
    pass


class LeagueDetail(BaseModel):
    name: str
    chief_admin_user: user.UserSummary
    categories: list[category.CategorySummary]
    tournaments: list[tournament.TournamentSummary]
    admin_users: list[user.UserSummary]
    teams: list[team.TeamSummary]

    model_config = ConfigDict(from_attributes=True)


class LeagueDetailResponse(common.CommonResponse[LeagueDetail]):
    pass
