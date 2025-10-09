# backend/cruds/games.py

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
from backend import models, utils

@utils.db_exception_handler
def get_game_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[models.Game]:
    """
    試合一覧を取得
    """
    query = (
        db.query(models.Game)
        .options(
            joinedload(models.Game.top_team),
            joinedload(models.Game.bottom_team),
            joinedload(models.Game.location),
            joinedload(models.Game.tournament)
        )
    )

    if category_id is not None:
        query = query.filter(
            or_(
                models.Game.top_team.has(
                    models.Team.categories.any(models.Category.category_id == category_id)
                ),
                models.Game.bottom_team.has(
                    models.Team.categories.any(models.Category.category_id == category_id)
                )
            )
        )

    if league_id is not None:
        query = query.filter(
            or_(
                models.Game.top_team.has(models.Team.league_id == league_id),
                models.Game.bottom_team.has(models.Team.league_id == league_id)
            )
        )

    games = query.all()
    return games


@utils.db_exception_handler
def get_game_detail(
    db: Session,
    game_id: int
) -> models.Game:
    """
    試合の詳細情報を取得
    """
    query = (
        db.query(models.Game)
        .filter(models.Game.game_id == game_id)
        .options(
            joinedload(models.Game.top_team),
            joinedload(models.Game.bottom_team),
            joinedload(models.Game.location),
            joinedload(models.Game.tournament),
            joinedload(models.Game.created_by_user)
        )
    )

    game_detail = query.first()
    return game_detail
