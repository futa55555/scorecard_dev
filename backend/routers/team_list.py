# backend/routers/team_list.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import team_list as schema
from backend.services import team_list as service

router = APIRouter()

@router.get("/api/team_list", response_model=schema.AllTeam)
def get_team_list(
    db: Session = Depends(get_db)
) -> schema.AllTeam:
    """
    チームの一覧を返す
    """
    return schema.AllTeam(
        team = service.get_team_list(db)
    )