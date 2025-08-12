# backend/constants/play_mapping/others.py

from backend import models
from typing import Optional, List
from backend.schemas import score_input as schema
from fastapi import HTTPException
from . import utils

# ------------------------
# 不正投球や妨害
# ------------------------

def make_others(
    pitch_type_detail: models.PitchTypeDetailType,
    runners: List[Optional[models.GameMember]],
    leaving_base: int = None
) -> List[List[Optional[schema.AdvanceElement]]]:
    res = []
    
    # hit_by_pitch, interfere
    if pitch_type_detail in (models.PitchTypeDetailType.hit_by_pitch, models.PitchTypeDetailType.interfere):
        res.append(
            utils.apply_common_advancement(
                runners = runners,
                length = 1,
                is_out = False,
                reason = pitch_type_detail,
                is_break = True,
                exclusion = []
            )
        )
            
    # illegal
    elif pitch_type_detail == models.PitchTypeDetailType.illegal:
        res.append(
            utils.apply_common_advancement(
                runners = runners,
                length = 1,
                is_out = False,
                reason = pitch_type_detail,
                is_break = True,
                exclusion = [0]
            )
        )
    
    # leaivng_base
    elif pitch_type_detail == models.PitchTypeDetailType.leaving_base:
        runner = runners[leaving_base]
        if not runner:
            raise HTTPException(status_code=400, detail="leaving_base is invalid")
        res.append(
            [
                schema.AdvanceElement(
                    runner_id = runner.id,
                    from_base = leaving_base,
                    to_base = leaving_base,
                    is_out = True,
                    reason = pitch_type_detail
                )
            ]
        )

    return res
