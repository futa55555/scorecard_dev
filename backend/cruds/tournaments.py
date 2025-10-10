# backend/cruds/tournaments.py

from sqlalchemy.orm import Session
from backend import models, utils

@utils.db_exception_handler
def get_tournament_list(
    db: Session,
    category_id: int | None = None
) -> list[models.Tournament]:
    """
    大会一覧を取得
    """
    query = db.query(models.Tournament)

    if category_id is not None:
        query = query.filter(
            models.Tournament.categories.any(models.Category.category_id == category_id)
        )

    tournament_list = query.all()
    return tournament_list
