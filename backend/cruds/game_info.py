# backend/cruds/game_info.py

from fastapi import HTTPException
from sqlalchemy import func
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
        .options(
            joinedload(models.Inning.game)
            .joinedload(models.Inning.atbats)
        )
        .all()
    )
    

def get_starting_member(
    db: Session,
    game_id: int
) -> List[models.GameMember]:
    """
    試合のスタメンをチーム関係なく取得
    """
    return (
        db.query(models.GameMember)
        .filter(
            (models.GameMember.game_id == game_id)
            & (models.GameMember.starting_batting_order > 0)
        )
        .options(
            joinedload(models.GameMember.person)
        )
        .order_by(models.GameMember.starting_batting_order.asc())
        .all()
    )


def get_position_type(
    db: Session,
    person_id: int
) -> List[models.PlayerPositionType]:
    """
    人の守備位置の履歴を取得
    """
    return (
        db.query(models.PlayerPositionType)
        .filter(models.PlayerPositionType.person_id == person_id)
        .order_by(models.PlayerPositionType.since_date.asc())
        .all()
    )


def get_bench_member(
    db: Session,
    game_id: int
) -> List[models.GameMember]:
    """
    試合の控えをチーム関係なく取得
    """
    return (
        db.query(models.GameMember)
        .filter(
            (models.GameMember.game_id == game_id)
            & (models.GameMember.starting_batting_order is None)
        )
        .options(
            joinedload(models.GameMember.person)
        )
        .all()
    )


def get_all_substitution_events(
    db: Session,
    game_id: int
) -> List[models.SubstitutionEvent]:
    """
    交代イベントをすべて取得
    """
    return (
        db.query(models.SubstitutionEvent)
        .filter(models.SubstitutionEvent.game_id == game_id)
        .options(
            joinedload(models.SubstitutionEvent.sub_member)
            .joinedload(models.GameMember.person)
        )
        .order_by(models.SubstitutionEvent.id.asc())
        .all()
    )


def get_all_atbats(
    db: Session,
    game_id: int
) -> List[models.AtBat]:
    """
    すべての打席を取得
    """
    return (
        db.query(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .options(
            joinedload(models.AtBat.responsible_batter)
        )
        .all()
    )


def get_latest_atbat_with_pitch_events(
    db: Session,
    game_id: int
) -> models.AtBat:
    """
    最新の打席を取得
    """
    return (
        db.query(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .options(
            joinedload(models.AtBat.pitch_events)
        )
        .order_by(models.AtBat.id.desc())
        .first()
    )


def get_advance_events_of_latest_inning(
    db: Session,
    game_id: int
) -> List[models.AdvanceEvent]:
    """
    現在のイニングのadvance_eventsを取得
    進塁がなければ（試合開始直後なら）[]を返す
    """
    latest_inning = (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .order_by(models.Inning.id.desc())
        .first()
    )
    if not latest_inning:
        raise HTTPException(status_code=404, detail="latest_inning not found")
    
    advance_events_of_latest_inning = (
        db.query(models.AdvanceEvent)
        .join(models.PitchEvent)
        .join(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.id == latest_inning.id)
        .order_by(
            models.PitchEvent.id.asc(),      # pitch_event.id 昇順
            models.AdvanceEvent.runner_id.asc(),  # runnerごとにまとめる
            func.min(models.AdvanceEvent.from_base).over(
                partition_by=models.AdvanceEvent.runner_id
            ).desc(),                       # runnerの初期位置（最大のfrom_base）降順
            models.AdvanceEvent.from_base.asc()   # runner内でfrom_base 昇順
        )
        .options(
            joinedload(models.AdvanceEvent.pitch_event)
            .joinedload(models.PitchEvent.atbat)
        )
        .all()
    )
    if not advance_events_of_latest_inning:
        return []
    return advance_events_of_latest_inning









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
            joinedload(models.Inning.game)
            .joinedload(models.Inning.atbats)
            .joinedload(models.AtBat.pitch_events)
            .joinedload(models.PitchEvent.advance_events)
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
            joinedload(models.MemberProfile.person)
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
            joinedload(models.GameMember.person)
        )
        .first()
    )
    

