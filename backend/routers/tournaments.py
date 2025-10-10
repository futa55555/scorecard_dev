# backend/routers/tournaments.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/tournaments", tags=["tournaments"])

@router.get(
    "/",
    response_model=schemas.TournamentListResponse,
    summary="大会一覧を取得"
)
def get_tournament_list(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter tournaments by category ID")
) -> schemas.TournamentListResponse:
    tournament_list = services.get_tournament_list(db, category_id)

    return utils.get_response(
        data=tournament_list,
        target="tournament list"
    )
