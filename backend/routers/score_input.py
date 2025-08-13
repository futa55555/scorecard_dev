# backend/routers/score_input.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from backend.database import get_db
from backend import models
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from backend.services import score_input as service
from typing import Tuple, List
from pydantic import BaseModel

router = APIRouter()


@router.post("/api/games/{game_id}/start")
def start_game(game_id: int, db: Session = Depends(get_db)):
    return service.game_start(db, game_id)


@router.get("/api/games/{game_id}/state_all_innings", response_model=schema.StateWithInnings)
def get_state_and_all_atbats(
    game_id: int,
    db: Session = Depends(get_db)
):
    """
    指定試合の現在の状態と全AtBat + PitchEvent + AdvanceEventを返す
    """
    all_innings_with_events = service.get_all_innings_with_events_to_schema(db, game_id)
    state = service.get_latest_state(db, game_id)
    return {
        "state": state,
        "all_innings_with_events": all_innings_with_events
    }


@router.get("/api/games/{game_id}/state", response_model=schema.GameStateResponse)
def get_game_state(
    game_id:int,
    db: Session = Depends(get_db)
 ) -> schema.GameStateResponse:
    """
    現在の試合状況（フロントはこれを表示 -> 次の投球入力へ）
    """
    return service.get_latest_state(db, game_id)


@router.get("/api/games/{game_id}/all_innings", response_model=List[schema.InningSchema])
def get_all_atbats(
    game_id: int,
    db: Session = Depends(get_db)
):
    """
    指定試合の全AtBat + PitchEvent + AdvanceEventを返す
    """
    return service.get_all_innings_with_events_to_schema(db, game_id)


@router.post("/api/games/{game_id}/pitch")
def register_pitch(
    game_id: int,
    input_data: schema.ScoreInput,
    db: Session = Depends(get_db)
) -> schema.MainAdvenceCandidates:
    """
    投球を登録 -> 進塁候補を返す
    """
    atbat = crud.get_latest_atbat(db, game_id)
    crud.create_pitch_event(db, atbat.id, input_data)
    main_advance_events = service.suggest_main_advance_events(db, game_id, input_data)
    return {
        "num_of_candidates": len(main_advance_events),
        "candidates": main_advance_events
    }
    
@router.post("/api/games/{game_id}/confirm")
def confirm_advance_event(
    game_id: int,
    input_data: schema.SelectedAdvanceCandidate,
    db: Session = Depends(get_db)
) -> schema.AdvanceCandidateConfirm:
    change = False
    
    pitch_event = crud.get_latest_pitch_event(db, game_id)
    atbat = crud.get_latest_atbat(db, game_id)
    selected_candidate = crud.create_advance_event(db, pitch_event.id, input_data.selected_candidate)
    for advance_element in selected_candidate:
        if advance_element.from_base == 0:
            crud.update_atbat_result(db, atbat.id, advance_element.reason)
    game_state = service.get_latest_state(db, game_id)
    if game_state.ball_count.outs == 3:
        change = True
    return {
        "selected_candidate": selected_candidate,
        "change": change
    }
    

@router.post("/api/games/{game_id}/change")
def change_inning(
    game_id: int,
    input_data: schema.ChangeInput,
    db: Session = Depends(get_db)
) -> schema.AtBatSchema:
    if input_data.change:
        last_inning = crud.get_latest_inning(db, game_id)
        outs, score, runners_id = service.aggregate_advance_events(db, game_id)
        crud.update_inning_score(db, last_inning.id, score)
        
        next_inning = service.create_next_inning(db, game_id, last_inning)
        next_batter = service.get_following_batter(db, game_id)
        next_atbat = crud.create_atbat(db, next_inning.id, next_batter.id)
    else:
        latest_inning = crud.get_latest_inning(db, game_id)
        next_batter = service.get_following_batter(db, game_id)
        next_atbat = crud.create_atbat(db, latest_inning.id, next_batter.id)
    
    return schema.AtBatSchema.model_validate(next_atbat, from_attributes=True)
