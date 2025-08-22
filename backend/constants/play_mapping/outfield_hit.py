# backend/constants/play_mapping/outfield_hit.py

from sqlalchemy.orm import Session
from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from fastapi import HTTPException
from . import utils

# ------------------------
# 外野ヒット
# ------------------------

def make_outfield_hit(
    advance_ingredient: schema.AdvanceIngredient
) -> List[Optional[schema.AdvanceCandidate]]:
    runners = advance_ingredient.runners
    ball_count = advance_ingredient.ball_count
    batting_form = advance_ingredient.batting_form
    position = advance_ingredient.position
    batted_ball_type = advance_ingredient.batted_ball_type
    is_runners_steal = advance_ingredient.is_runners_steal

    base = []
    
    # 単打
    for i in [1, 2, 3, 4]:
        base.append(
            utils.apply_common_advance(
                runners = runners,
                step = i,
                is_break = False,
                is_only_runners = False,
                is_by_atbat = True,
                result = models.AtBatResultEnum.hit,
                ball_flow = [position],
                advance_by_pitch = True
            )
        )
    
    return base
