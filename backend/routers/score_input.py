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


# @router.get("/api/games/{game_id}/all_atbats", response_model=schema.StateWithAtBats)
# def get_all_atbats(game_id: int, db: Session = Depends(get_db)):
#     """
#     指定試合の全AtBat + PitchEvent + AdvanceEventを返す
#     """
#     atbats = (
#         db.query(models.AtBat)
#         .filter(models.AtBat.game_id == game_id)
#         .options(
#             joinedload(models.AtBat.pitch_events)  # AtBat → PitchEvent
#             .joinedload(models.PitchEvent.advance_events)  # PitchEvent → AdvanceEvent
#         )
#         .all()
#     )
    
#     state = service.get_game_state(db, game_id)
    
#     return {"state": state, "atbats": atbats}
    
    
# @router.post("/api/score-input/{game_id}", response_model=schema.ScoreInputResponse)
# def post_score_input(game_id: int, input_data: schema.ScoreInputSchema, db: Session = Depends(get_db)):
#     """
#     投球を受け取り、PitchEvent作成 + 進塁候補サジェスト
#     """
#     response = service.record_pitch_event(db, game_id, input_data)
    
#     return response


# @router.post("/api/score-input/{game_id}/confirm")
# def confirm_score_input(game_id: int, input_data: schema.ConfirmScoreInput, db: Session = Depends(get_db)):
#     response = service.confirm_score_input(db, game_id, input_data)
#     return response

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
    pitch = crud.create_pitch_event(db, atbat.id, input_data)
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
) -> schema.SelectedAdvanceCandidate:
    pitch_event = crud.get_latest_pitch_event(db, game_id)
    selected_candidate = crud.create_advance_event(db, pitch_event.id, input_data.selected_candidate)
    return {"selected_candidate": selected_candidate}



# --- 後でサジェスト機能を戻す時に復活 ---
# @router.post("/api/score-input/{game_id}", response_model=schema.ScoreInputResponse)
# def post_score_input(game_id: int, input_data: schema.ScoreInputSchema, db: Session = Depends(get_db)):
#     return service.record_pitch_event(db, game_id, input_data)
#
# @router.post("/api/score-input/{game_id}/confirm")
# def confirm_score_input(game_id: int, input_data: schema.ConfirmScoreInput, db: Session = Depends(get_db)):
#     return service.confirm_score_input(db, game_id, input_data)


@router.post("/api/score-input/{game_id}/confirm")
def confirm_score_input_disabled(game_id: int, db: Session = Depends(get_db)):
    """
    今はサジェスト/確認フローを使わないので、呼ばれたら 400 を返す
    """
    raise HTTPException(status_code=400, detail="confirm API is disabled in minimal mode")
