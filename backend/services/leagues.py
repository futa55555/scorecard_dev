# backend/services/leagues.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_league_summaries(
    db: Session,
    category_id: int | None = None
) -> list[schemas.LeagueSummary]:
    """
    リーグの概要一覧を取得
    """
    league_summaries = cruds.get_league_summaries(db, category_id)

    adapter = TypeAdapter(list[schemas.LeagueSummary])
    return adapter.validate_python(league_summaries)


def get_league_list(
    db: Session,
    category_id: int | None = None
) -> list[schemas.LeagueListItem]:
    """
    リーグ一覧を取得
    """
    league_list = cruds.get_league_list(db, category_id)

    adapter = TypeAdapter(list[schemas.LeagueListItem])
    return adapter.validate_python(league_list)


def get_league_detail(
    db: Session,
    league_id: int
) -> schemas.LeagueDetail:
    """
    リーグの詳細情報を取得
    """
    league_detail = cruds.get_league_detail(db, league_id)

    adapter = TypeAdapter(schemas.LeagueDetail)
    return adapter.validate_python(league_detail)
