# backend/constants/play_mapping/utils.py

from backend import models
from typing import Optional, List
from backend.schemas import score_input as schema

def calc_to_base(n: int):
    return n if n < 4 else 4

# 打席結果 + 強制進塁を課す
def apply_common_advance(
    runners: List[Optional[models.GameMember]],
    step: int,
    is_break: bool,
    is_only_runners: bool,
    is_by_atbat: bool,
    out_type: models.OutTypeEnum = None,
    ball_flow: Optional[List[models.PositionEnum]] = [],
    advance_by_pitch: Optional[models.AdvanceByPitchEnum] = None,
) -> List[Optional[schema.AdvanceElement]]:
    res = []
    
    for base, runner in enumerate(runners):
        if is_only_runners and base == 0:
            continue
        
        if not runner:
            if is_break:
                break
            else:
                continue
        
        res.append(
            schema.AdvanceElement(
                runner_id = runner.id,
                from_base = base,
                to_base = calc_to_base(base + step),
                is_out = False,
                is_by_atbat = is_by_atbat,
                out_type = out_type,
                ball_flow = ball_flow,
                advance_by_pitch = advance_by_pitch,
            )
        )
    
    return res
