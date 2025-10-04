# backend/routers/tournaments.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Tournament

router = APIRouter(prefix="/api/tournaments", tags=["tournaments"])

@router.get("/")
def list_tournaments(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter tournaments by category ID."),
    league_id: int | None = Query(None, description="Filter tournaments by league ID."),
    team_id: int | None = Query(None, description="Filter tournaments by team ID."),
    favorite: bool | None = Query(None, description="Filter tournaments by favorite status")
):
    """
    大会一覧を取得
    カテゴリー、リーグ、チーム、お気に入りでフィルター可
    """

@router.get("/{tournament_id}")
def get_tournament(
    tournament_id: int,
    db: Session = Depends(get_db)
):
    """
    大会詳細を取得
    """
