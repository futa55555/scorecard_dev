# backend/routers/game_list.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import game_list as schema
from backend.services import game_list as service

router = APIRouter()

@router.get("/api/game_list", response_model=schema.GameWithTeamNameList)
def get_game_list(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100, description="取得する件数")
) -> schema.GameWithTeamNameList:
    """
    試合の一覧を返す
    """
    return schema.GameWithTeamNameList(
        game_list = service.get_game_with_team_name_list(db, limit)
    )
    
