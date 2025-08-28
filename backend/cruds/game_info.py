# backend/cruds/game_info.py

from sqlalchemy.orm import Session, joinedload
from typing import List
from backend import models

#-------------------
# 取得系
#-------------------

def get_game_base(
    db: Session,
    game_id: int
) -> models.Game:
    """
    試合の基本情報を取得
    """
    return (
        db.query(models.Game)
        .filter(models.Game.id == game_id)
        .options(
            joinedload(models.Game.top_team)
            .joinedload(models.Game.bottom_team)
        )
        .first()
    )


def get_all_innings(
    db: Session,
    game_id: int
) -> List[models.Inning]:
    """
    試合に紐づけられたイニングをすべて取得
    """
    return (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .all()
    )
    

def get_all_innings_with_atbat(
    db: Session,
    game_id: int
) -> List[models.Inning]:
    """
    すべての打席と投球を取得
    """
    return (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .options(
            joinedload(models.AtBat)
            .joinedload(models.PitchEvent)
            .joinedload(models.AdvanceEvent)
        )
        .order_by(models.AtBat.id.asc())
        .all()
    )
    

def get_starting_order(
    db: Session,
    game_id: int,
    team_id: int
) -> List[models.GameMember]:
    """
    チームの登録選手を取得
    """
    return (
        db.query(models.GameMember)
        .filter(
            (models.GameMember.game_id == game_id)
            & (models.GameMember.team_id == team_id)
        )
        .options(
            joinedload(models.GameMember.member_profile)
            .joinedload(models.MemberProfile.person)
        )
        .order_by(models.GameMember.starting_batting_order.asc())
        .all()
    )


def get_entry_member(
    db: Session,
    game_id: int,
    team_id: int
) -> List[models.GameMember]:
    """
    チームの出場選手を取得（順番を工夫しないといけない）
    """
    return (
        db.query(models.GameMember)
        .filter(
            (models.GameMember.game_id == game_id)
            & (models.GameMember.team_id == team_id)
            & (models.GameMember.entry_number > 0)
        )
        .options(
            joinedload(models.GameMember.member_profile)
            .joinedload(models.MemberProfile.person)
        )
        .all()
    )


def get_substitutions_by_pitch(
    db: Session,
    game_id: int,
    pitch_event_id: int
) -> List[models.SubstitutionEvent]:
    """
    投球時までの交代情報を取得
    """
    return (
        db.query(models.SubstitutionEvent)
        .filter(
            (models.SubstitutionEvent.game_id == game_id)
            & (models.SubstitutionEvent.pitch_event_id <= pitch_event_id)
        )
        .order_by(models.SubstitutionEvent.id.asc())
        .all()
    )


def get_game_member_by_id(
    db: Session,
    game_member_id: int
) -> models.GameMember:
    """
    game_member_idから、名前までの情報を取得
    """
    return (
        db.query(models.GameMember)
        .filter(models.GameMember.id == game_member_id)
        .options(
            joinedload(models.GameMember.member_profile)
            .joinedload(models.MemberProfile.person)
        )
        .first()
    )
    

