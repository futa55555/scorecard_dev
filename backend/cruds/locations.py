# backend/cruds/locations.py

from sqlalchemy.orm import Session, joinedload
from backend import models
from backend.utils.db_exception import db_exception_handler

@db_exception_handler
def list_locations(
    db: Session,
    prefecture: str | None = None
) -> list[models.Location]:
    """
    試合会場一覧を取得
    都道府県でフィルター可
    """
    query = db.query(models.Location)

    if prefecture is not None:
        query = query.filter(models.Location.prefecture == prefecture)

    locations = query.all()
    return locations

@db_exception_handler
def get_location(
    db: Session,
    location_id: int
) -> models.Location:
    """
    試合会場の詳細情報を取得
    作成者も合わせて取得
    """
    return (
        db.query(models.Location)
        .filter(models.Location.location_id == location_id)
        .options(
            joinedload(models.Location.created_by_user)
        )
        .first()
    )
