# backend/schemas/tournament.py

from pydantic import BaseModel, ConfigDict
from datetime import date
from . import common

class TournamentBase(BaseModel):
    tournament_id: int
    name: str
    since_date: date
    until_date: date

    model_config = ConfigDict(from_attributes=True)


class TournamentListItem(TournamentBase):
    pass

    model_config = ConfigDict(from_attributes=True)


class TournamentListResponse(common.CommonResponse[list[TournamentListItem]]):
    pass
