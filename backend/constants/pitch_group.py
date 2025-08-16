# backend/constants/pitch_group.py

from typing import FrozenSet, Dict
from backend import models

# --- グループ定義（重複可） ---
strike: FrozenSet[models.PitchTypeEnum] = frozenset({models.PitchTypeEnum.swing_miss, models.PitchTypeEnum.looking})
count: FrozenSet[models.PitchTypeEnum] = frozenset({*strike, models.PitchTypeEnum.ball})  # strike ∪ {ball}
inplays: FrozenSet[models.PitchTypeEnum] = frozenset({models.PitchTypeEnum.inplay, models.PitchTypeEnum.hit, models.PitchTypeEnum.poor, models.PitchTypeEnum.sacrified})
ball_dead: FrozenSet[models.PitchTypeEnum] = frozenset({models.PitchTypeEnum.foul, models.PitchTypeEnum.others})

GROUPS: Dict[str, FrozenSet[models.PitchTypeEnum]] = {
    "strike": strike,
    "count": count,
    "inplays": inplays,
    "ball_dead": ball_dead
}

# 便利ヘルパ
def in_group(pt: models.PitchTypeEnum, group: str) -> bool:
    return pt in GROUPS[group]

def groups_of(pt: models.PitchTypeEnum) -> list[str]:
    return [name for name, members in GROUPS.items() if pt in members]