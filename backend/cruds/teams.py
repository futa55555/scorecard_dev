# backend/cruds/teams.py

from sqlalchemy.orm import Session, joinedload
from backend import models
from backend.utils.db_exception import db_exception_handler

@db_exception_handler
def list_teams(
    db: Session,
    category: int | None = None,
    league: int | None = None,
    prefecture: str | None = None,
    user: int | None = None
) -> list[models.Team]:
    """
    チーム一覧を取得。
    カテゴリー、カテゴリーも合わせて取得。
    カテゴリー、リーグ、都道府県、お気に入りでフィルター可。
    """
    query = (
        db.query(models.Team)
        .options(
            joinedload(models.Team.categories),
            joinedload(models.Team.league)
        )
    )

    if category is not None:
        query = query.filter(
            models.Team.categories.any(
                models.Category.category_id == category
            )
        )

    if league is not None:
        query = query.filter(models.Team.league_id == league)

    if prefecture is not None:
        query = query.filter(models.Team.prefecture == prefecture)

    if user is not None:
        query = query.filter(
            models.Team.fans.any(
                models.User.user_id == user
            )
        )

    teams = query.all()
    return teams

@db_exception_handler
def get_team(
    db: Session,
    team: int
) -> models.Team:
    """
    チームの詳細情報を取得
    カテゴリー、リーグ、管理者、人物一覧、試合一覧も合わせて取得
    """
    return (
        db.query(models.Team)
        .filter(models.Team.team_id == team)
        .options(
            joinedload(models.Team.categories),
            joinedload(models.Team.league),
            joinedload(models.Team.chief_admin_user),
            joinedload(models.Team.person_profiles)
                .joinedload(models.PersonProfile.person)
                .joinedload(models.Person.player_positions),
            joinedload(models.Team.games_as_bottom_team),
            joinedload(models.Team.games_as_top_team)
        )
        .first()
    )
