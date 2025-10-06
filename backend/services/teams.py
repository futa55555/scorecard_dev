# backend/services/teams.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_team_summaries(
    db: Session,
    category_id: int | None = None
) -> schemas.TeamSummaries:
    """

    """


def get_team_list(
    db: Session,
    category: int | None = None,
    league: int | None = None,
    prefecture: str | None = None,
    user: int | None = None
) -> schemas.TeamList:
    """
    チーム一覧を取得
    """
    teams = cruds.list_teams(db, category, league, prefecture, user)

    adapter = TypeAdapter(list[schemas.TeamSummary])
    return adapter.validate_python(teams)


def get_team_detail(
    db: Session,
    team_id: int
) -> schemas.TeamDetail:
    """

    """
