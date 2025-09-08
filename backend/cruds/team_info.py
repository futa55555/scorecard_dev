# backend/cruds/team_info.py

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from typing import List, Dict, Tuple
from backend import models
from backend.schemas import team_info as schema


def get_team(
    db: Session,
    team_id: int
) -> models.Team:
    return (
        db.query(models.Team)
        .filter(models.Team.id == team_id)
        .first()
    )


def get_count_by_grade_and_role(
    db: Session,
    team_id: int
) -> List[Dict[str, any]]:
    return (
        db.query(
            func.count(models.Person.id).label("cnt"),
            models.MemberGrade.grade,
            models.MemberProfile.role
        )
        .join(models.MemberProfile)
        .join(models.MemberGrade)
        .filter(
            (models.MemberProfile.team_id == team_id)
            & (models.MemberProfile.until_date.is_(None))
            & (models.MemberGrade.until_date.is_(None))
        )
        .group_by(
            models.MemberGrade.grade,
            models.MemberProfile.role
        )
        .all()
    )
    

def get_recent_game(
    db: Session,
    team_id: int
) -> List[models.Game]:
    return (
        db.query(models.Game)
        .filter(
            (models.Game.top_team_id == team_id)
            | (models.Game.bottom_team_id == team_id)    
        )
        .options(
            joinedload(models.Game.innings),
            joinedload(models.Game.top_team),
            joinedload(models.Game.bottom_team)
        )
        .order_by(
            models.Game.date.desc(),
            models.Game.start_time.desc()
        )
        .limit(5)
        .all()
    )
    

def get_all_member(
    db: Session,
    team_id: int
) -> List[Tuple[models.Person, models.MemberProfile, models.MemberGrade, models.PlayerPositionType]]:
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
            (models.MemberProfile.team_id == team_id)
            & (models.MemberProfile.until_date.is_(None))
            & (models.MemberGrade.until_date.is_(None))
            & (models.PlayerPositionType.until_date.is_(None))
        )
        .all()
    )


def get_member(
    db: Session,
    team_id: int,
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
            & (models.MemberProfile.team_id == team_id)
            & (models.MemberProfile.until_date.is_(None))
            & (models.MemberGrade.until_date.is_(None))
            & (models.PlayerPositionType.until_date.is_(None))
        )
        .first()
    )
