# backend/routers/people.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import utils, schemas, services

router = APIRouter(prefix="/api/people", tags=["people"])

@router.get(
    "/",
    response_model=schemas.PersonListWithPageResponse,
    summary="メンバー一覧を取得"
)
def get_person_list(
    db: Session = Depends(get_db),
    current_page: int = Query(1, description="Current page number."),
    limit: int = Query(30, description="Max number of team per page."),
    category_id: int | None = Query(None, description="Filter people by category ID."),
    league_id: int | None = Query(None, description="Filter people by league ID.")
) -> schemas.PersonListWithPageResponse:
    person_list_with_page = services.get_person_list_with_page(db, current_page, limit, category_id, league_id)

    return utils.get_response(
        data=person_list_with_page,
        target="person list with page"
    )


@router.get(
    "/{person_id}/",
    response_model=schemas.PersonDetailResponse,
    summary="メンバーの詳細情報を取得"
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
