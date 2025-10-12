# backend/cruds/teams.py

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from backend import models, utils

@utils.db_exception_handler
def get_team_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[models.Team]:
    """
    チーム一覧を取得
    """
    query = (
        db.query(models.Team)
        .options(
            joinedload(models.Team.categories),
            joinedload(models.Team.league)
        )
    )

    if category_id is not None:
        query = query.filter(
            models.Team.categories.any(models.Category.category_id == category_id)
        )

    if league_id is not None:
        query = query.filter(models.Team.league_id == league_id)

    team_list = query.all()
    return team_list


@utils.db_exception_handler
def get_team_list_with_page(
    db: Session,
    current_page: int,
    limit: int,
    category_id: int | None = None,
    league_id: int | None = None
) -> tuple[list[models.Team], int]:
    """
    ページ付きのチーム一覧を取得
    """
    query = (
        db.query(models.Team)
        .options(
            joinedload(models.Team.categories),
            joinedload(models.Team.league)
        )
    )

    if category_id is not None:
        query = query.filter(
            models.Team.categories.any(models.Category.category_id == category_id)
        )

    if league_id is not None:
        query = query.filter(models.Team.league_id == league_id)

    team_total_count = query.count()

    team_list = query.offset((current_page - 1) * limit).limit(limit).all()

    return team_list, team_total_count


@utils.db_exception_handler
def get_team_detail(
    db: Session,
    team_id: int
) -> models.Team:
    """
    チームの詳細情報を取得
    """
    query = (
        db.query(models.Team)
        .filter(
            and_(
                models.Team.team_id == team_id,
                models.Team.person_profiles.any(
                    models.PersonProfile.until_date.is_(None)
                )
            )
        )
        .options(
            joinedload(models.Team.chief_admin_user),
            joinedload(models.Team.league),
            joinedload(models.Team.categories),
            joinedload(models.Team.locations),
            joinedload(models.Team.tournaments),
            joinedload(models.Team.admin_users),
            joinedload(models.Team.person_profiles)
                .joinedload(models.PersonProfile.person)
                    .joinedload(models.Person.person_profiles)
                    .joinedload(models.Person.player_positions),
            joinedload(models.Team.games_as_bottom_team),
            joinedload(models.Team.games_as_top_team)
        )
    )

    team_detail = query.first()
    return team_detail
