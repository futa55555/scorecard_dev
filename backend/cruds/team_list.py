# backend/cruds/team_list.py

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from backend import models

def get_team_list(
    db: Session,
    limit: int
) -> List[models.Team]:
    """
    すべてのチームを取得
    """
    return (
        db.query(models.Team)
        .limit(limit)
        .all()
    )