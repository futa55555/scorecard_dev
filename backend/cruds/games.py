# backend/cruds/games.py

from sqlalchemy.orm import Session
from sqlalchemy import or_
from backend import models
from backend.utils.db_exception import db_exception_handler

@db_exception_handler
def list_games(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None,
    tournament_id: int | None = None,
    team_id: int | None = None,
    user_id: int | None = None
) -> list[models.Game]:
    """
    試合一覧を取得
    チーム、会場、大会も合わせて取得
    カテゴリー、リーグ、大会、チーム、お気に入りでフィルター可
    """
    query = db.query(models.Game)

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

    if tournament_id is not None:
        query = query.filter(models.Game.tournament_id == tournament_id)

    if team_id is not None:
        query = query.filter(
            or_(
                models.Game.top_team_id == team_id,
                models.Game.bottom_team_id == team_id
            )
        )

    if user_id is not None:
        query = query.filter(
            or_(
                models.Game.tournament.has(
                    models.Tournament.fans.any(
                        models.User.user_id == user_id
                    )
                ),
                models.Game.top_team.has(
                    models.Team.fans.any(
                        models.User.user_id == user_id
                    )
                ),
                models.Game.bottom_team.has(
                    models.Team.fans.any(
                        models.User.user_id == user_id
                    )
                )
            )
        )

    games = query.all()
    return games

@db_exception_handler
def get_game(
    db: Session,
    game_id: int
) -> models.Game:
    """
    試合の詳細情報を取得
    チーム、会場、大会、作成者も合わせて取得。
    """
    return (
        db.query(models.Game)
        .filter(models.Game.game_id == game_id)
        .first()
    )
