# backend/cruds/categories.py

from sqlalchemy.orm import Session
from backend import models, utils

@utils.db_exception_handler
def get_category_summaries(
    db: Session
) -> list[models.Category]:
    """
    カテゴリーの概要一覧を取得
    """
    query = db.query(models.Category)

    category_summaries = query.all()
    return category_summaries
