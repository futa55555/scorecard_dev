# bacnend/routers/teams.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/teams", tags=["teams"])

@router.get(
    "/summary/",
    response_model=schemas.TeamSummariesResponse,
    summary="チーム概要一覧を取得"
)
def get_team_summaries(
    db: Session = Depends(get_db),
    category: int | None = Query(None, description="Filter teams by category ID.")
) -> schemas.TeamSummariesResponse:
    team_summaries = services.get_team_summaries(db, category)

    return utils.get_response(
        data=team_summaries,
        target="team summaries"
    )


@router.get(
    "/",
    response_model=schemas.TeamListResponse,
    summary="チーム一覧を取得"
)
def get_team_list(
    db: Session = Depends(get_db)
) -> schemas.TeamListResponse:
    team_list = services.get_team_list(db)

    return utils.get_response(
        data=team_list,
        target="team list"
    )


@router.get(
    "/{team_id}/",
    response_model=schemas.TeamDetailResponse,
    summary="チーム詳細を取得"
)
def get_team_detail(
    team_id: int,
    db: Session = Depends(get_db)
) -> schemas.TeamDetailResponse:
    team_detail = services.get_team_detail(db, team_id)

    return utils.get_response(
        data=team_detail,
        target="team detail"
    )
