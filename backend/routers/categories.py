# backend/routers/categories.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get(
    "/summary/",
    response_model=schemas.CategorySummariesResponse,
    summary="カテゴリーの概要一覧を取得"
)
def get_category_summaries(
    db: Session = Depends(get_db)
) -> schemas.CategorySummariesResponse:
    category_summaries = services.get_category_summaries(db)

    return utils.get_response(
        data=category_summaries,
        target="category summaries"
    )
