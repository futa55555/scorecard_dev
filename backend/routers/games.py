# backend/routers/games.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/games", tags=["games"])

@router.get(
    "/",
    response_model=schemas.GameListResponse,
    summary="試合一覧を取得"
)
def get_game_list(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter games by category ID."),
    league_id: int | None = Query(None, description="Filter games by league ID.")
) -> schemas.GameListResponse:
    game_list = services.get_game_list(db, category_id, league_id)

    return utils.get_response(
        data=game_list,
        target="game list"
    )


@router.get(
    "/{game_id}/",
    response_model=schemas.GameDetailResponse,
    summary="試合の詳細情報を取得"
)
def get_game_detail(
    game_id: int,
    db: Session = Depends(get_db)
) -> schemas.GameDetailResponse:
    game_detail = services.get_game_detail(db, game_id)

    return utils.get_response(
        data=game_detail,
        target="game detail"
    )
