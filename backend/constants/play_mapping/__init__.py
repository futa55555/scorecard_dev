# backend/constants/play_mapping/__init__.py

from .infield_ground import play_mapping_infield_ground
from .outfield_ground import play_mapping_outfield_ground

# すべて統合
play_mapping = {}
play_mapping.update(play_mapping_infield_ground)
play_mapping.update(play_mapping_outfield_ground)

# 外部からは play_mapping だけ使えばOK
__all__ = ["play_mapping"]
