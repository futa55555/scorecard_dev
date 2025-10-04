# backend/routers/games.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Game

router = APIRouter(prefix="/api/games", tags=["games"])

@router.get("/")
def list_games(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter games by category ID."),
    league_id: int | None = Query(None, description="Filter games by league ID."),
    tournament_id: int | None = Query(None, description="Filter games by tournament ID."),
    team_id: int | None = Query(None, description="Filter games by team ID.")
):
    """
    試合一覧を取得
    カテゴリー、リーグ、大会、チームでフィルター可
    """

@router.get("/{game_id}")
def get_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    """
    試合の詳細情報を取得
    """
