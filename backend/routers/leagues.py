# backend/router/leagues.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import League

router = APIRouter(prefix="/api/leagues", tags=["leagues"])

@router.get("/")
def list_leagues(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter leagues by category ID.")
):
    """
    リーグ一覧を取得
    フィルター用で、最低限の情報のみ
    """

@router.get("/{league_id}")
def get_league(
    league_id: int,
    db: Session = Depends(get_db)
):
    """
    リーグの詳細情報を取得
    """
