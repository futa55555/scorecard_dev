# backend/cruds/tournaments.py

from sqlalchemy.orm import Session, joinedload
from backend import models
from backend.utils.db import db_exception_handler

@db_exception_handler
def list_tournaments(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None,
    team_id: int | None = None,
    user_id: int | None = None
) -> list[models.Tournament]:
    """
    大会一覧を取得
    カテゴリー、リーグ、チーム、お気に入りでフィルター可
    """
    query = db.query(models.Tournament)

    if category_id is not None:
        query = query.filter(
            models.Tournament.categories.any(models.Category.category_id == category_id)
        )

    if league_id is not None:
        query = query.filter(
            models.Tournament.leagues.any(models.League.league_id == league_id)
        )

    if team_id is not None:
        query = query.filter(
            models.Tournament.teams.any(models.Team.team_id == team_id)
        )

    if user_id is not None:
        query = query.filter(
            models.Tournament.fans.any(
                models.User.user_id == user_id
            )
        )

    tournaments = query.all()
    return tournaments

@db_exception_handler
def get_tournament(
    db: Session,
    tournament_id: int
) -> models.Tournament:
    """
    大会詳細を取得
    """
    return (
        db.query(models.Tournament)
        .filter(models.Tournament.tournament_id == tournament_id)
        .options(
            joinedload(models.Tournament.games)
                .joinedload(models.Game.top_team),
            joinedload(models.Tournament.games)
                .joinedload(models.Game.bottom_team),
            joinedload(models.Tournament.categories),
            joinedload(models.Tournament.leagues),
            joinedload(models.Tournament.locations)
            )
        .first()
    )
