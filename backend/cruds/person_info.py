# backend/cruds/person_info.py

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from typing import List, Dict, Tuple
from backend import models
from backend.schemas import person_info as schema


def get_person(
    db: Session,
    person_id: int
) -> Tuple[models.Person, models.MemberProfile, models.MemberGrade, models.PlayerPositionType]:
    return (
        db.query(
            models.Person,
            models.MemberProfile,
            models.MemberGrade,
            models.PlayerPositionType
        )
        .join(models.MemberProfile)
        .join(models.MemberGrade)
        .join(models.PlayerPositionType)
        .filter(
            (models.Person.id == person_id)
            & (models.MemberProfile.until_date.is_(None))
            & (models.MemberGrade.until_date.is_(None))
            & (models.PlayerPositionType.until_date.is_(None))
        )
        .first()
    )
