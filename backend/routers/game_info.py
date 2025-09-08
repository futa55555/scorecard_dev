# backend/routers/game_info.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import game_info as schema
from backend.services import game_info as service

router = APIRouter()


@router.get("/api/game_info/{game_id}/top", response_model = schema.GameInfoTop)
def get_game_info_top(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoTop:
    return schema.GameInfoTop(num = 1)


@router.get("/api/game_info/{game_id}/live", response_model = schema.GameInfoLive)
def get_game_info_live(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoLive:
    return schema.GameInfoLive(num = 1)



@router.get("/api/game_info/{game_id}/progress", response_model = schema.GameInfoProgress)
def get_game_info_progress(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoProgress:
    return schema.GameInfoProgress(num = 1)



@router.get("/api/game_info/{game_id}/stats", response_model = schema.GameInfoStats)
def get_game_info_stats(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoStats:
    return schema.GameInfoStats(num = 1)
