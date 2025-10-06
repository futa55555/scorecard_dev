# backend/cruds/leagues.py

from sqlalchemy.orm import Session, joinedload
from backend import models
from backend.utils.db_exception import db_exception_handler

@db_exception_handler
def list_leagues(
    db: Session,
    category_id: int | None = None
) -> list[models.League]:
    """
    リーグ一覧を取得
    フィルター用で、最低限の情報のみ
    """
    query = db.query(models.League)

    if category_id is not None:
        query.filter(
            models.League.categories.any(models.Category.category_id == category_id)
        )

    leagues = query.all()
    return leagues

@db_exception_handler
def get_league(
    db: Session,
    league_id: int
) -> models.League:
    """
    リーグの詳細情報を取得
    管理者、所属チーム、カテゴリーも合わせて取得
    """
    return (
        db.query(models.League)
        .filter(models.League.league_id == league_id)
        .options(
            joinedload(models.League.chief_admin_user),
            joinedload(models.League.teams),
            joinedload(models.League.categories)
        )
        .first()
    )
