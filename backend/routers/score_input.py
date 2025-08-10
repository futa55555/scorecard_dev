# backend/routers/score_input.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from backend.database import get_db
from backend import models
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from backend.services import score_input as service
from typing import List
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

@router.get("/api/games/{game_id}/all_atbats", response_model=schema.StateWithAtBats)
def get_all_atbats(game_id: int, db: Session = Depends(get_db)):
    """
    指定試合の全AtBat + PitchEvent + AdvanceEventを返す（デバッグ用）
    """
    atbats = (
        db.query(models.AtBat)
        .filter(models.AtBat.game_id == game_id)
        .options(
            joinedload(models.AtBat.pitch_events)
            .joinedload(models.PitchEvent.advance_events)
        )
        .all()
    )
    state = service.get_latest_state(db, game_id)
    return {"state": state, "atbats": atbats}


@router.get("/api/games/{game_id}/state", response_model=schema.GameStateResponse)
def get_game_state(game_id: int, db: Session = Depends(get_db)):
    """
    現在の試合状況（フロントはこれを表示→次の投球入力へ）
    """
    return service.get_latest_state(db, game_id)


@router.post("/api/games/{game_id}/pitch", response_model=schema.GameStateResponse)
def post_pitch(game_id: int, input_data: schema.ScoreInput, db: Session = Depends(get_db)):
    """
    1球登録 → 四球/三振なら自動確定 → 3アウトならチェンジ → 最新状態を返す
    """
    # ここで service 側は「四球・三振・チェンジのみ完全対応」する実装に
    # 例: service.register_pitch_event_and_auto_finish(db, game_id, input_data)
    return service.register_pitch_event_and_auto_finish(db, game_id, input_data)


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
