# backend/routers/people.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Person

router = APIRouter(prefix="/api/people", tags=["people"])

@router.get("/")
def list_people(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter people by category ID."),
    league_id: int | None = Query(None, description="Filter people by league ID."),
    team_id: int | None = Query(None, description="Filter people by team ID."),
    prefecture: str | None = Query(None, description="Filter people by prefecture."),
    position_type: str | None = Query(None, description="Filter people by position type."),
    favorite: bool | None = Query(None, description="Filter people by favorite status")
):
    """
    人物一覧を取得
    カテゴリー、リーグ、チーム、出身都道府県、ポジション、お気に入りでフィルター可
    現在の所属チームと背番号、役割とポジションを合わせて取得
    """

@router.get("/{person_id}")
def get_person(
    person_id: int,
    db: Session = Depends(get_db)
):
    """
    人物の詳細情報を取得
    過去のチーム遍歴やポジションの変遷も合わせて取得
    """
