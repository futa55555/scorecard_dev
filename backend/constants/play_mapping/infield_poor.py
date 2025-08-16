# backend/constants/play_mapping/infield_poor.py

from sqlalchemy.orm import Session
from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from fastapi import HTTPException
from . import utils

# ------------------------
# 内野凡打
# ------------------------

def make_infield_poor(
    advance_ingredient: schema.AdvanceIngredient
) -> List[Optional[schema.AdvanceCandidate]]:
    runners = advance_ingredient.runners
    ball_count = advance_ingredient.ball_count
    batting_form = advance_ingredient.batting_form
    position = advance_ingredient.position
    batted_ball_type = advance_ingredient.batted_ball_type
    is_runners_steal = advance_ingredient.is_runners_steal

    res = []
    
    
    
    return res
