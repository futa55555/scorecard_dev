# backend/cruds/people.py

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from backend import models
from backend.utils.db import db_exception_handler

@db_exception_handler
def list_people(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None,
    team_id: int | None = None,
    prefecture: str | None = None,
    position_type: str | None = None,
    user_id: int | None = None
) -> list[models.Person]:
    """
    人物一覧を取得。
    カテゴリー、リーグ、チーム、出身都道府県、ポジション、お気に入りでフィルター可。
    現在の所属チームと背番号、役割とポジションを合わせて取得。
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
                and_(
                    models.PersonProfile.until_date.is_(None),
                    models.PersonProfile.team.has(
                        models.Team.categories.any(models.Category.category_id == category_id)
                    )
                )
            )
        )

    if league_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                and_(
                    models.PersonProfile.until_date.is_(None),
                    models.PersonProfile.team.has(
                        models.Team.league_id == league_id
                    )
                )
            )
        )

    if team_id is not None:
        query = query.filter(
            models.Person.person_profiles.any(
                and_(
                    models.PersonProfile.until_date.is_(None),
                    models.PersonProfile.team_id == team_id
                )
            )
        )

    if prefecture is not None:
        query = query.filter(models.Person.prefecture == prefecture)

    if position_type is not None:
        query = query.filter(
            models.Person.player_positions.any(
                and_(
                    models.PlayerPosition.until_date.is_(None),
                    models.PlayerPosition.position_type == position_type
                )
            )
        )

    if user_id is not None:
        query = query.filter(
            models.Person.fans.any(
                models.User.user_id == user_id
            )
        )

    people = query.all()
    return people

@db_exception_handler
def get_person(
    db: Session,
    person_id: int
) -> models.Person:
    """
    人物の詳細情報を取得
    過去のチーム遍歴やポジションの変遷も合わせて取得
    """
    return (
        db.query(models.Person)
        .filter(models.Person.person_id == person_id)
        .options(
            joinedload(models.Person.person_profiles),
            joinedload(models.Person.player_positions)
        )
        .first()
    )
