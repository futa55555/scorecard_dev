# backend/services/categories.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_category_summaries(
    db: Session
) -> schemas.CategorySummaries:
    """
    カテゴリー概要一覧を取得
    """
    categories = cruds.list_categories(db)

    adapter = TypeAdapter(schemas.CategorySummaries)
    return adapter.validate_python(categories)
