# backend/constants/play_mapping/inplay.py

from backend import models
from typing import Optional, List
from backend.schemas import score_input as schema
from fastapi import HTTPException

# ------------------------
# 打撃を伴わない進塁
# ------------------------

def make_inplay(
    position: models.PositionEnum,
    ball_direction: models.BattedBallDirectionEnum,
    ball_type: models.BattedBallTypeEnum,
    outs: int,
    runners: List[Optional[models.GameMember]],
    is_runners_steal: List[bool]
) -> List[List[Optional[schema.AdvanceElement]]]:
    res = []
    
    return [[]]