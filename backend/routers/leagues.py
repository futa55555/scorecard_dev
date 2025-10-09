# backend/router/leagues.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/leagues", tags=["leagues"])

@router.get(
    "/summary/",
    response_model=schemas.LeagueSummariesResponse,
    summary="リーグの概要一覧を取得"
)
def get_league_summaries(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter leagues by category ID.")
) -> schemas.LeagueSummariesResponse:
    league_summaries = services.get_league_summaries(db, category_id)

    return utils.get_response(
        data=league_summaries,
        target="league summaries"
    )


@router.get(
    "/",
    response_model=schemas.LeagueListResponse,
    summary="リーグ一覧を取得"
)
def get_league_list(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter leagues by category ID.")
) -> schemas.LeagueListResponse:
    league_list = services.get_league_list(db, category_id)

    return utils.get_response(
        data=league_list,
        target="league list"
    )


@router.get(
    "/{league_id}/",
    response_model=schemas.LeagueDetailResponse,
    summary="リーグの詳細情報を取得"
)
def get_league_detail(
    league_id: int,
    db: Session = Depends(get_db)
) -> schemas.LeagueDetailResponse:
    league_detail = services.get_league_detail(db, league_id)

    return utils.get_response(
        data=league_detail,
        target="league detail"
    )
