# backend/cruds/categories.py

from sqlalchemy.orm import Session, joinedload
from backend import models
from backend.utils.db import db_exception_handler

@db_exception_handler
def list_categories(
    db: Session,
    include: list[str]
) -> list[models.Category]:
    """
    カテゴリー一覧を取得
    include=leaguesで所属するリーグ一覧も取得
    """
    query = db.query(models.Category)

    if "leagues" in include:
        query = query.options(
            joinedload(models.Category.leagues)
        )

    categories = query.all()
    return categories

@db_exception_handler
def get_category(
    db: Session,
    category_id: int
) -> models.Category:
    """
    カテゴリー詳細を取得
    所属するリーグ一覧、各リーグに所属するチーム一覧、無所属のチーム一覧も取得
    """
    return (
        db.query(models.Category)
        .filter(models.Category.category_id == category_id)
        .options(
            joinedload(models.Category.leagues)
                .joinedload(models.League.teams),
            joinedload(models.Category.teams)
        )
        .first()
    )
