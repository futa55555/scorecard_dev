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
    advance_ingredient: schema.AdvanceIngredient
) -> List[Optional[schema.AdvanceCandidate]]:
    runners = advance_ingredient.runners
    ball_count = advance_ingredient.ball_count
    pitch_type = advance_ingredient.pitch_type
    pitch_type_detail = advance_ingredient.pitch_type_detail
    leaving_base = advance_ingredient.leaving_base
    
    if pitch_type == models.PitchTypeEnum.foul:
        # ファウル
        if ball_count.strikes == 3:
            # スリーバント失敗
            return [
                schema.AdvanceCandidate(
                    atbat_result = "strikeout",
                    advance_elements = [
                        schema.AdvanceElement(
                            runner_id = runners[0].id,
                            from_base = 0,
                            to_base = 0,
                            is_out = True,
                            is_by_atbat = True
                        )
                    ]
                )
            ]
        else:
            # ただのファウル
            return [
                schema.AdvanceCandidate()
            ]
    
    if pitch_type_detail in (models.PitchTypeDetailEnum.hit_by_pitch, models.PitchTypeDetailEnum.interfere):
        # 死球
        return [
            schema.AdvanceCandidate(
                atbat_result = pitch_type_detail,
                advance_elements = utils.apply_common_advance(
                    runners = runners,
                    step = 1,
                    is_break = True,
                    is_only_runners = False,
                    is_by_atbat = True,
                )
            )
        ]

    elif pitch_type_detail == models.PitchTypeDetailEnum.illegal:
        # イリーガルピッチ
        if ball_count == 4:
            return [
                schema.AdvanceCandidate(
                    atbat_result = "walk",
                    advance_elements = utils.apply_common_advance(
                        runners = runners,
                        step = 1,
                        is_break = True,
                        is_only_runners = False,
                        is_by_atbat = True,
                    )
                )
            ]
        else:
            return [
                schema.AdvanceCandidate(
                    advance_elements = utils.apply_common_advance(
                        runners = runners,
                        step = 1,
                        is_break = True,
                        is_only_runners = True,
                        is_by_atbat = False,
                    )
                )
            ]
    
    elif pitch_type_detail == models.PitchTypeDetailEnum.leaving_base:
        # 離塁アウト
        runner = runners[leaving_base]
        if not runner:
            raise HTTPException(status_code=400, detail="leaving_base is invalid")
        return [
            schema.AdvanceCandidate(
                advance_elements = [
                    schema.AdvanceElement(
                        runner_id = runner.id,
                        from_base = leaving_base,
                        to_base = leaving_base,
                        is_out = True,
                        is_by_atbat = False
                    )
                ]
            )
        ]
