# backend/constants/play_mapping/pitch_only.py

from sqlalchemy.orm import Session
from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from fastapi import HTTPException
from . import utils

# ------------------------
# 打撃を伴わない進塁
# ------------------------

def make_pitch_only(
    runners: List[Optional[models.GameMember]],
    pitch_type: models.PitchTypeEnum,
    ball_count: schema.BallCount,
    is_runners_steal: schema.RunnersSteal
) -> List[Optional[schema.AdvanceCandidate]]:
    if ball_count.strikes == 3:
        # 三振
        # 振り逃げなし
        base_atbat_result = "strikeout"
        base_advance_elements = [
            schema.AdvanceElement(
                runner_id = runners[0].id,
                from_base = 0,
                to_base = 0,
                is_out = True,
                is_by_atbat = True
            )
        ]
        return [
            schema.AdvanceCandidate(
                atbat_result = base_atbat_result,
                advance_elements = base_advance_elements
            )
        ]
            
    elif ball_count.balls == 4:
        # 打者の四球 + 強制進塁
        base_atbat_result = "walk"
        base_advance_elements = utils.apply_common_advance(
            runners = runners,
            step = 1,
            is_break = True,
            is_only_runners = False,
            is_by_atbat = True
        )
        return [
            schema.AdvanceCandidate(
                atbat_result = base_atbat_result,
                advance_elements = base_advance_elements
            )
        ]

    else:
        return []

### 今できてること
# 振り逃げなし三振
# 四球 + 強制進塁

### 足すべきこと
# 振り逃げなし三振 + 進塁
# 振り逃げあり三振
# 振り逃げあり三振 + 進塁
# 四球 + 進塁