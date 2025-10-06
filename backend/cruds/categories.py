# backend/cruds/categories.py

from sqlalchemy.orm import Session
from backend import models
from backend.utils.db_exception import db_exception_handler

@db_exception_handler
def list_categories(
    db: Session
) -> list[models.Category]:
    """
    カテゴリー一覧を取得
    """
    query = db.query(models.Category)

    categories = query.all()
    return categories
