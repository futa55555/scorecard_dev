# backend/constants/play_mapping/outfield_poor.py

from sqlalchemy.orm import Session
from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from fastapi import HTTPException
from . import utils

# ------------------------
# 外野凡打
# ------------------------

def make_outfield_poor(
    advance_ingredient: schema.AdvanceIngredient
) -> List[Optional[schema.AdvanceCandidate]]:
    runners = advance_ingredient.runners
    ball_count = advance_ingredient.ball_count
    batting_form = advance_ingredient.batting_form
    position = advance_ingredient.position
    batted_ball_type = advance_ingredient.batted_ball_type
    is_runners_steal = advance_ingredient.is_runners_steal

    res = []
    
    # フライ
    res.append(
        schema.AdvanceCandidate(
            atbat_result = models.AtBatResultEnum.poor,
            advance_elements = [
                schema.AdvanceElement(
                    runner_id = runners[0].id,
                    from_base = 0,
                    to_base = 1,
                    is_out = True,
                    is_by_atbat = True,
                    ball_flow = [position]
                )
            ]
        )
    )
    # ゴロ（打者）
    res.append(
        schema.AdvanceCandidate(
            atbat_result = models.AtBatResultEnum.poor,
            advance_elements = [
                schema.AdvanceElement(
                    runner_id = runners[0].id,
                    from_base = 0,
                    to_base = 1,
                    is_out = True,
                    is_by_atbat = True,
                    ball_flow = [position, models.PositionEnum]
                )
            ]
        )
    )
    # ゴロ（走者）
    
    return res
