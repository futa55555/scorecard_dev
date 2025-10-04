# bacnend/routers/teams.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy import Session
from backend.database import get_db
from backend.models import Team

router = APIRouter(prefix="/api/teams", tags=["teams"])

@router.get("/")
def list_teams(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter teams by category ID."),
    league_id: int | None = Query(None, description="Filter teams by league ID."),
    prefecture: str | None = Query(None, description="Filter teams by prefecture."),
    favorite: bool | None = Query(None, description="Filter teams by favorite status.")
):
    """
    試合一覧を取得
    カテゴリー、リーグ、都道府県、お気に入りでフィルター可
    """

@router.get("/{team_id}")
def get_team(
    team_id: int,
    db: Session = Depends(get_db)
):
    """
    チームの詳細情報を取得
    管理者、人物一覧、試合一覧も合わせて取得
    """
