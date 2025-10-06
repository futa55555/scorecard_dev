# backend/schemas/tournament.py

from pydantic import BaseModel, ConfigDict

class TournamentSummary(BaseModel):
    tournament_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
