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
    result: Optional[models.AtBatResultEnum] = None,
    out_type: models.OutTypeEnum = None,
    ball_flow: Optional[List[models.PositionEnum]] = [],
    advance_by_pitch: Optional[models.AdvanceByPitchEnum] = None,
) -> schema.AdvanceCandidate:
    atbat_result = str()
    if result:
        atbat_result = str(result)
        if result not in (models.AtBatResultEnum.strikeout, models.AtBatResultEnum.walk):
            atbat_result = str(ball_flow[0]) + atbat_result
            if result == models.AtBatResultEnum.hit:
                atbat_result = atbat_result + str(step)
    
    advance_elements = []
    
    for base, runner in enumerate(runners):
        if is_only_runners and base == 0:
            continue
        
        if not runner:
            if is_break:
                break
            else:
                continue
        
        advance_elements.append(
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
    
    return schema.AdvanceCandidate(
        atbat_result = atbat_result,
        advance_elements = advance_elements
    )
