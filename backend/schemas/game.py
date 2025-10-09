# backend/schemas/game.py

from pydantic import BaseModel, ConfigDict
from datetime import date, time
from . import common, location, tournament, user, team

class GameBase(BaseModel):
    game_id: int
    date: date
    start_time: time
    end_time: time

    model_config = ConfigDict(from_attributes=True)


class GameListItem(GameBase):
    top_team: team.TeamBase
    bottom_team: team.TeamBase
    location: location.LocationBase
    tournament: tournament.TournamentBase

    model_config = ConfigDict(from_attributes=True)


class GameListResponse(common.CommonResponse[list[GameListItem]]):
    pass


class GameDetail(GameBase):
    top_team: team.TeamBase
    bottom_team: team.TeamBase
    location: location.LocationBase
    tournament: tournament.TournamentBase
    created_by_user: user.UserBase

    model_config = ConfigDict(from_attributes=True)


class GameDetailResponse(common.CommonResponse[GameDetail]):
    pass
