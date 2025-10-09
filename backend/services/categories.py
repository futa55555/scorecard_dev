# backend/services/categories.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_category_summaries(
    db: Session
) -> list[schemas.CategorySummary]:
    """
    カテゴリーの概要一覧を取得
    """
    category_summaries = cruds.get_category_summaries(db)

    adapter = TypeAdapter(list[schemas.CategorySummary])
    return adapter.validate_python(category_summaries)
