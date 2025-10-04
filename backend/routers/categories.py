# backend/routers/categories.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Category

router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get("/")
def list_categories(
    db: Session = Depends(get_db),
    include: list[str] | None = Query([], description="Include related leagues.")
):
    """
    カテゴリー一覧を取得
    include=leaguesで所属するリーグ一覧も取得
    """

@router.get("/{category_id}")
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    """
    カテゴリー詳細を取得
    所属するリーグ一覧、さらに各リーグに所属するチーム一覧、無所属のチーム一覧も取得
    """
