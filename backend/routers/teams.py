# bacnend/routers/teams.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/teams", tags=["teams"])

@router.get(
    "/",
    response_model=schemas.TeamListResponse,
    summary="チーム一覧を取得"
)
def get_team_list(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter people by category ID."),
    league_id: int | None = Query(None, description="Filter people by league ID.")
) -> schemas.TeamListResponse:
    team_list = services.get_team_list(db, category_id, league_id)

    return utils.get_response(
        data=team_list,
        target="team list"
    )


@router.get(
    "/{team_id}/",
    response_model=schemas.TeamDetailResponse,
    summary="チームの詳細情報を取得"
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
