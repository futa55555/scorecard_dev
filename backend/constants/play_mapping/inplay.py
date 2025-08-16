# backend/constants/play_mapping/inplay.py

from backend import models
from typing import Optional, List
from backend.schemas import score_input as schema
from backend.constants import position_group
from .infield_poor import make_infield_poor
from .infield_hit import make_infield_hit
from .outfield_poor import make_outfield_poor
from .outfield_hit import make_outfield_hit

# ------------------------
# 打撃を伴う進塁
# ------------------------

def make_inplay(
    advance_ingredient: schema.AdvanceIngredient
) -> List[Optional[schema.AdvanceCandidate]]:
    res = []
    
    if position_group.in_group(advance_ingredient.position, "infield"):
        res += make_infield_poor(advance_ingredient)
        res += make_infield_hit(advance_ingredient)
    elif position_group.in_group(advance_ingredient.position, "outfield"):
        res += make_outfield_poor(advance_ingredient)
        res += make_outfield_hit(advance_ingredient)
    
    return res
