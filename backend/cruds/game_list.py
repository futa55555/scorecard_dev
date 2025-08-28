# backend/cruds/game_list.py

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from backend import models

# ------------------------
# 取得系
# ------------------------

def get_game_list(
    db: Session
) -> List[models.Game]:
    """
    すべての試合を取得
    """
    return (
        db.query(models.Game)
        .options(
            joinedload(models.Game.top_team)
            .joinedload(models.Game.bottom_team)
        )
        .all()
    )
