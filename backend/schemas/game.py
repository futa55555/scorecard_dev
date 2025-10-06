# backend/schemas/game.py

from pydantic import BaseModel, ConfigDict
from datetime import date, time
from . import common, location, user, team

class GameItem(BaseModel):
    game_id: int
    date: date
    start_time: time
    end_time: time
    top_team: team.TeamSummary
    bottom_team: team.TeamSummary
    location: location.LocationSummary
    created_by_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)


class GameList(list[GameItem]):
    pass


class GameListResponse(common.CommonResponse[GameList]):
    pass


class GameDetail(BaseModel):
    date: date
    start_time: time
    end_time: time
    top_team: team.TeamSummary
    bottom_team: team.TeamSummary
    location: location.LocationSummary
    created_by_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)


class GameDetailResponse(common.CommonResponse[GameDetail]):
    pass
