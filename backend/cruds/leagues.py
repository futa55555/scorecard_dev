# backend/cruds/leagues.py

from sqlalchemy.orm import Session, joinedload
from backend import models, utils

@utils.db_exception_handler
def get_league_summaries(
    db: Session,
    category_id: int | None = None
) -> list[models.League]:
    """
    リーグの概要一覧を取得
    """
    query = db.query(models.League)

    if category_id is not None:
        query = query.filter(
            models.League.categories.any(models.Category.category_id == category_id)
        )

    league_summaries = query.all()
    return league_summaries


@utils.db_exception_handler
def get_league_list(
    db: Session,
    category_id: int | None = None
) -> list[models.League]:
    """
    リーグ一覧を取得
    """
    query = (
        db.query(models.League)
        .options(
            joinedload(models.League.categories),
            joinedload(models.League.teams)
        )
    )

    if category_id is not None:
        query = query.filter(
            models.League.categories.any(models.Category.category_id == category_id)
        )

    league_list = query.all()
    return league_list


@utils.db_exception_handler
def get_league_detail(
    db: Session,
    league_id: int
) -> models.League:
    """
    リーグの詳細情報を取得
    """
    query = (
        db.query(models.League)
        .filter(models.League.league_id == league_id)
        .options(
            joinedload(models.League.chief_admin_user),
            joinedload(models.League.categories),
            joinedload(models.League.tournaments),
            joinedload(models.League.admin_users),
            joinedload(models.League.teams),
        )
    )

    league_detail = query.first()
    return league_detail
