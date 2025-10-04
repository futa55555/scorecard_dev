# backend/routers/locations.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Location

router = APIRouter(prefix="/api/locations", tags=["locations"])

@router.get("/")
def list_locations(
    db: Session = Depends(get_db),
    prefecture: str | None = Query(None, description="Filter locations by prefecture")
):
    """
    試合会場一覧を取得
    都道府県でフィルター可
    """

@router.get("/{location_id}")
def get_location(
    location_id: int,
    db: Session = Depends(get_db)
):
    """
    試合会場の詳細情報を取得
    """
