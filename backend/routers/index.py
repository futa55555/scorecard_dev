# backend/routers/index.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Team

router = APIRouter()

@router.get("/api/myteam")
def get_myteam(db: Session = Depends(get_db)):
    """
    マイチーム（is_myteam=True の Team）を取得
    """
    team = db.query(Team).filter(Team.is_myteam == True).first()
    if team:
        return {"id": team.id, "name": team.name}
    return {"id": None, "name": None}
