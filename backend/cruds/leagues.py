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
    category_id が指定されている場合は、そのカテゴリに属するチームを持つリーグのみ返す
    また、各リーグに含まれる teams も指定カテゴリ所属のものに限定する
    """
    query = db.query(models.League)

    # ===== category_id が指定されている場合 =====
    if category_id is not None:
        query = (
            query
            .filter(
                models.League.teams.any(
                    models.Team.categories.any(models.Category.category_id == category_id)
                )
            )
            .options(
                joinedload(models.League.categories),
                joinedload(models.League.teams)
                .joinedload(models.Team.categories)
            )
            .distinct()
        )
    # ===== category_id が None の場合 =====
    else:
        query = query.options(
            joinedload(models.League.categories),
            joinedload(models.League.teams)
            .joinedload(models.Team.categories)
        )

    league_list = query.all()

    # 各リーグ内の teams を category_id に応じて絞る
    if category_id is not None:
        for league in league_list:
            league.teams = [
                team for team in league.teams
                if any(cat.category_id == category_id for cat in team.categories)
            ]

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
