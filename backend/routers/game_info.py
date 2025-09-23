# backend/routers/game_info.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import game_info as schema
from backend.services import game_info as service

router = APIRouter()


@router.get("/api/game_info/{game_id}/top", response_model=schema.GameInfoTop)
def get_game_info_top(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoTop:
    return schema.GameInfoTop(
        game_base=service.get_game_base(db, game_id),
        inning_score=service.get_inning_score(db, game_id),
        starting_order=service.get_starting_order(db, game_id),
        bench_member=service.get_bench_member(db, game_id),
        entry_history=service.get_entry_history(db, game_id),
        battery=service.get_battery(db, game_id)
    )


@router.get("/api/game_info/{game_id}/live", response_model=schema.GameInfoLive)
def get_game_info_live(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoLive:
    return schema.GameInfoLive(
        num=1
    )


@router.get("/api/game_info/{game_id}/progress", response_model=schema.GameInfoProgress)
def get_game_info_progress(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoProgress:
    return schema.GameInfoProgress(
        num=1
    )


@router.get("/api/game_info/{game_id}/stats", response_model=schema.GameInfoStats)
def get_game_info_stats(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoStats:
    return schema.GameInfoStats(
        num=1
    )


@router.get("/api/game_info/{game_id}/members", response_model=schema.GameInfoMembers)
def get_game_info_members(
    game_id: int,
    db: Session = Depends(get_db)
) -> schema.GameInfoMembers:
    return schema.GameInfoMembers(
        starting_member=service.get_starting_order(db, game_id),
        bench_member=service.get_bench_member(db, game_id)
    )
