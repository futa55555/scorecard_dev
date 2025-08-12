# backend/constants/play_mapping/utils.py

from backend import models
from typing import Optional, List
from backend.schemas import score_input as schema

def calc_to_base(n: int):
    return n if n < 4 else 4

def apply_common_advancement(
    runners: List[Optional[models.GameMember]],
    length: int,
    is_out: bool,
    reason: str,
    is_break: bool,
    exclusion: List[int] = []
) -> List[Optional[schema.AdvanceElement]]:
    res = []
    
    for base, runner in enumerate(runners):
        if not runner:
            if is_break:
                break
            else:
                continue
            
        if base in exclusion:
            continue
        
        res.append(
            schema.AdvanceElement(
                runner_id = runner.id,
                from_base = base,
                to_base = calc_to_base(base + length),
                is_out = is_out,
                reason = reason
            )
        )
    
    return res

