# backend/routers/people.py

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import people as people_schema
from backend.cruds import people as people_crud

# このルーターは人物管理に関するAPI（JSON形式）を提供する
# GET: 一覧取得
# POST: 追加 / 編集
# DELETE: 削除

router = APIRouter()


@router.get("/api/people", response_model=list[people_schema.PersonResponse])
def get_people(db: Session = Depends(get_db)):
    """
    人物一覧を取得してJSONで返す
    """
    stmt = select(models.Person)
    people = db.scalars(stmt).all()
    return people
