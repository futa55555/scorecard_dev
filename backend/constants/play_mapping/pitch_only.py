# backend/constants/play_mapping/pitch_only.py

from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema
from fastapi import HTTPException
from . import utils

# ------------------------
# 打撃を伴わない進塁
# ------------------------

def make_pitch_only(
    pitch_type: models.PitchTypeEnum,
    ball_count: schema.BallCount,
    runners: List[Optional[models.GameMember]],
    is_runners_steal: schema.RunnersSteal
) -> List[List[Optional[schema.AdvanceElement]]]:
    res = []
    
    if ball_count.balls == 4:
        res.append(
            utils.apply_common_advancement(
                runners = runners,
                length = 1,
                is_out = False,
                reason = "walk",
                is_break = True,
                exclusion = []
            )
        )

    elif ball_count.strikes == 3:
        tmp = [
            schema.AdvanceElement(
                runner_id = runners[0].id,
                from_base = 0,
                to_base = 0,
                is_out = True,
                reason = "strikeout"
            )
        ]
        res.append(tmp)
        
        if any(runners[1:]):
            res.append(
                tmp + utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "WP",
                    is_break = False,
                    exclusion = [0]
                )
            )
            res.append(
                tmp + utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "PB",
                    is_break = False,
                    exclusion = [0]
                )
            )
        
        if not runners[1]:
            res.append(
                [
                    schema.AdvanceElement(
                        runner_id = runners[0].id,
                        from_base = 0,
                        to_base = 1,
                        is_out = True,
                        reason = "strikeout"
                    )
                ],
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "WP",
                    is_break = False,
                    exclusion = []
                )
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "PB",
                    is_break = False,
                    exclusion = []
                )
            )
        
        elif ball_count.outs == 2:
            res.append(
                [
                    schema.AdvanceElement(
                        runner_id = runners[0].id,
                        from_base = 0,
                        to_base = 1,
                        is_out = True,
                        reason = "strikeout"
                    )
                ]
            )
            res.append(
                [
                    schema.AdvanceElement(
                        runner_id = runners[3].id,
                        from_base = 3,
                        to_base = 4,
                        is_out = True,
                        reason = "strikeout"
                    )
                ]
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "WP",
                    is_break = False,
                    exclusion = []
                )
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "PB",
                    is_break = False,
                    exclusion = []
                )
            )
        
    else:
        res.append([])
        if any(runners[1:]):
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "WP",
                    is_break = False,
                    exclusion = [0]
                )
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "PB",
                    is_break = False,
                    exclusion = [0]
                )
            )
            res.append(
                utils.apply_common_advancement(
                    runners = runners,
                    length = 1,
                    is_out = False,
                    reason = "steal",
                    is_break = False,
                    exclusion = [0]
                )
            )
    
    return res
