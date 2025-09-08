# backend/routers/game_edit.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import game_edit as schema
from backend.services import game_edit as service

router = APIRouter()

@router.get("/api/game_edit/{game_id}/top", response_model = schema.GameEditTop)
def get_game_edit_top(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameEditTop:
    return schema.GameEditTop(num = 1)
    

@router.get("/api/game_edit/{game_id}/substitution", response_model = schema.GameEditSubstitution)
def get_game_edit_substitution(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameEditSubstitution:
    return schema.GameEditSubstitution(num = 1)
    

@router.get("/api/game_edit/{game_id}/play", response_model = schema.GameEditPlay)
def get_game_edit_play(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameEditPlay:
    return schema.GameEditPlay(num = 1)
