# backend/routers/people.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/people", tags=["people"])

@router.get(
    "/",
    response_model=schemas.PersonListResponse,
    summary="メンバー一覧を取得"
)
def get_person_list(
    db: Session = Depends(get_db),
    category_id: int | None = Query(None, description="Filter people by category ID."),
    league_id: int | None = Query(None, description="Filter people by league ID."),
    team_id: int | None = Query(None, description="Filter people by team ID."),
    prefecture: str | None = Query(None, description="Filter people by prefecture."),
    position_type: str | None = Query(None, description="Filter people by position type."),
    favorite: bool | None = Query(None, description="Filter people by favorite status")
) -> schemas.PersonListResponse:
    person_list = services.get_person_list(db, category_id)

    return utils.get_response(
        data=person_list,
        target="person list"
    )


@router.get(
    "/{person_id}/",
    response_model=schemas.PersonDetailResponse,
    summary="メンバー詳細を取得"
)
def get_person_detail(
    person_id: int,
    db: Session = Depends(get_db)
) -> schemas.PersonDetailResponse:
    person_detail = services.get_person_detail(db, person_id)

    return utils.get_response(
        data=person_detail,
        target="person detail"
    )
