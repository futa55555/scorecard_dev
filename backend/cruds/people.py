# backend/cruds/people.py

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from backend import models, utils

@utils.db_exception_handler
def get_person_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[models.Person]:
    """
    メンバー一覧を取得
    """
    query = (
        db.query(models.Person)
        .options(
            joinedload(models.Person.person_profiles),
            joinedload(models.Person.player_positions)
        )
    )

    if category_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                models.PersonProfile.team.has(
                    models.Team.categories.any(models.Category.category_id == category_id)
                )
            )
        )

    if league_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                models.PersonProfile.team.has(models.Team.league_id == league_id)
            )
        )

    person_list = query.all()
    return person_list


@utils.db_exception_handler
def get_person_list_with_page(
    db: Session,
    current_page: int,
    limit: int,
    category_id: int | None = None,
    league_id: int | None = None
) -> tuple[list[models.Person], int]:
    """
    ページ付きのメンバー一覧を取得
    """
    query = (
        db.query(models.Person)
        .options(
            joinedload(models.Person.person_profiles),
            joinedload(models.Person.player_positions)
        )
    )

    if category_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                models.PersonProfile.team.has(
                    models.Team.categories.any(models.Category.category_id == category_id)
                )
            )
        )

    if league_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                models.PersonProfile.team.has(models.Team.league_id == league_id)
            )
        )

    person_total_count = query.count()
    person_list = query.offset((current_page - 1) * limit).limit(limit).all()

    return person_list, person_total_count


@utils.db_exception_handler
def get_person_detail(
    db: Session,
    person_id: int
) -> models.Person:
    """
    メンバーの詳細情報を取得
    """
    query = (
        db.query(models.Person)
        .filter(models.Person.person_id == person_id)
        .options(
            joinedload(models.Person.created_by_user),
            joinedload(models.Person.person_profiles),
            joinedload(models.Person.player_positions),
            joinedload(models.Person.own_user)
        )
    )

    person_detail = query.first()
    return person_detail
