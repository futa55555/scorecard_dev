# backend/constants/position_group.py

from typing import FrozenSet, Dict
from backend import models

# --- グループ定義（重複可） ---
infield: FrozenSet[models.PositionEnum] = frozenset({
    models.PositionEnum.P,
    models.PositionEnum.C,
    models.PositionEnum.FB,
    models.PositionEnum.SB,
    models.PositionEnum.TB,
    models.PositionEnum.SS
})
outfield: FrozenSet[models.PositionEnum] = frozenset({
    models.PositionEnum.LF,
    models.PositionEnum.CF,
    models.PositionEnum.RF
})

GROUPS: Dict[str, FrozenSet[models.PositionEnum]] = {
    "infield": infield,
    "outfield": outfield
}

# 便利ヘルパ
def in_group(ps: models.PositionEnum, group: str) -> bool:
    return ps in GROUPS.get(group, frozenset())

def groups_of(ps: models.PositionEnum) -> list[str]:
    return [name for name, members in GROUPS.items() if ps in members]