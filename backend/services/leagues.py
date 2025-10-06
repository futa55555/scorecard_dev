# backend/services/leagues.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_league_summaries(
    db: Session
) -> schemas.LeagueSummaries:
    """

    """


def get_league_detail(
    db: Session,
    league_id: int
) -> schemas.LeagueDetail:
    """

    """
