# backend/cruds/score_input.py

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from backend import models
from typing import Optional, List, Dict
from backend.schemas import score_input as schema

# ------------------------
# 取得系
# ------------------------

def get_game(
    db: Session,
    game_id: int
) -> models.Game:
    """
    game_idからgameを取得
    """
    game = (
        db.query(models.Game)
        .filter(models.Game.id == game_id)
        .first()
    )
    if not game:
        raise HTTPException(status_code=404, detail="game not found")
    return game


def get_inning(
    db: Session,
    inning_id: int
) -> models.Inning:
    """
    inning_idからinningを取得
    """
    inning = (
        db.query(models.Inning)
        .filter(models.Inning.id == inning_id)
        .first()
    )
    if not inning:
        raise HTTPException(status_code=404, detail="inning not found")
    return inning


def get_team(
    db: Session,
    team_id: int
) -> models.Team:
    """
    team_idからteamを取得
    """
    team = (
        db.query(models.Team)
        .filter(models.Team.id == team_id)
        .first()
    )
    if not team:
        raise HTTPException(status_code=404, detail="team not found")
    return team
    

def get_game_member(
    db: Session,
    game_member_id: int
) -> Optional[models.GameMember]:
    """
    game_member_idからgame_memberを取得
    """
    return (
        db.query(models.GameMember)
        .filter(models.GameMember.id == game_member_id)
        .first()
    )


def get_game_members_with_member_profile(
    db: Session,
    game_id: int
) -> List[models.GameMember]:
    """
    出場登録選手のGameMemberをまとめて取得
    
    """
    game_members = (
        db.query(models.GameMember)
        .filter(models.GameMember.game_id == game_id)
        .options(
            joinedload(models.GameMember.member_profile)
        )
        .all()
    )
    if not game_members:
        raise HTTPException(status_code=404, detail="game_member not found")
    return game_members


def get_substitution_events_until_pitch(
    db: Session,
    pitch_event_id: int
) -> List[models.SubstitutionEvent]:
    """
    指定のpitch_event_idまでの選手交代情報を取得
    """
    substitution_events = (
        db.query(models.SubstitutionEvent)
        .filter(models.SubstitutionEvent.pitch_event_id <= pitch_event_id)
        .order_by(models.SubstitutionEvent.pitch_event_id)
        .all()
    )
    if not substitution_events:
        raise HTTPException(status_code=404, detail="substitution_event not found")
    return substitution_events


def get_all_substitution_events(
    db: Session,
    game_id: int
) -> List[models.SubstitutionEvent]:
    """
    現在までの選手交代情報を取得
    """
    return (
        db.query(models.SubstitutionEvent)
        .filter(models.SubstitutionEvent.game_id == game_id)
        .order_by(models.SubstitutionEvent.pitch_event_id)
        .all()
    )


def get_latest_pitch_event(
    db: Session,
    game_id: int
) -> Optional[models.PitchEvent]:
    """
    現在のpitch_eventを取得
    投球がなければ（試合開始直後なら）Noneを返す
    """
    return (
        db.query(models.PitchEvent.id)
        .join(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .order_by(models.PitchEvent.id.desc())
        .first()
    )


def get_inning_by_pitch(
    db: Session,
    pitch_event_id: int
) -> models.Inning:
    """
    pitch_event.idからinningを取得
    """
    inning = (
        db.query(models.Inning)
        .join(models.AtBat)
        .join(models.PitchEvent)
        .filter(models.PitchEvent.id == pitch_event_id)
        .first()
    )
    if not inning:
        raise HTTPException(status_code=404, detail="inning not found")
    return inning


def get_latest_inning(
    db: Session,
    game_id: int
) -> models.Inning:
    """
    現在のinningを取得
    """
    latest_inning = (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .order_by(models.Inning.id.desc())
        .first()
    )
    if not latest_inning:
        raise HTTPException(status_code=404, detail="latest_inning not found")
    return latest_inning


def get_atbat_by_pitch(
    db: Session,
    pitch_event_id: int
) -> models.AtBat:
    """
    pitch_event.idからatbatを取得
    """
    atbat = (
        db.query(models.AtBat)
        .join(models.PitchEvent)
        .filter(models.PitchEvent.id == pitch_event_id)
        .first()
    )
    if not atbat:
        raise HTTPException(status_code=404, detail="atbat not found")
    return atbat


def get_latest_atbat(
    db: Session,
    game_id: int
) -> Optional[models.AtBat]:
    """
    最新のatbatを取得
    """
    return (
        db.query(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .options(
            joinedload(models.AtBat.batter)
            .joinedload(models.GameMember.member_profile)
        )
        .order_by(models.AtBat.id.desc())
        .first()
    )
    
    
def get_previous_inning(
    db: Session,
    inning: models.Inning
) -> Optional[models.Inning]:
    """
    inning_idから1つ前のinningを取得
    """
    previous_inning = get_inning(db, inning)
    if not inning:
        raise HTTPException(status_code=404, detail="inning not found")
    
    return (
        db.query(models.Inning)
        .filter(
            (models.Inning.game_id == inning.game_id)
            & (models.Inning.inning_number == inning.inning_number - 1)
            & (models.Inning.top_bottom == inning.top_bottom)
        )
        .first()
    )


def get_innings_with_events_until_pitch(
    db: Session,
    pitch_event_id: int
) -> List[models.Inning]:
    """
    指定のpitch_eventまでのイニング->打席->投球->進塁を取得（一覧表示用）
    """
    subquery = (
        db.query(models.PitchEvent.atbat_id)
        .filter(models.PitchEvent.id <= pitch_event_id)
        .subquery()
    )
    if not subquery:
        raise HTTPException(status_code=404, detail="atbat not found")
    
    innings_with_events = (
        db.query(models.Inning)
        .join(models.Inning.atbats)
        .filter(models.AtBat.id.in_(subquery))
        .options(
            joinedload(models.Inning.atbats)
            .joinedload(models.AtBat.pitch_events)
            .joinedload(models.PitchEvent.advance_events)
        )
        .distinct()
        .order_by(models.Inning.inning_number, models.Inning.top_bottom)
        .all()
    )
    if not innings_with_events:
        raise HTTPException(status_code=404, detail="innings_with_events not found")
    return innings_with_events
    
    
def get_all_innings_with_events(
    db: Session,
    game_id: int
) -> List[models.Inning]:
    """
    現在までのイニング->打席->投球->進塁を取得（一覧表示用）
    """
    all_innings_with_events = (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .options(
            joinedload(models.Inning.atbats)
            .joinedload(models.AtBat.pitch_events)
            .joinedload(models.PitchEvent.advance_events)
        )
        .order_by(models.Inning.id)
        .all()
    )
    if not all_innings_with_events:
        raise HTTPException(status_code=404, detail="innings_with_events not found")
    return all_innings_with_events


def get_top_bottom_innings_with_events(
    db: Session,
    game_id: int,
    top_bottom: models.TopBottomEnum
) -> List[models.Inning]:
    """
    現在までのイニング->打席->投球->進塁を取得（一覧表示用）
    """
    all_innings_with_events = (
        db.query(models.Inning)
        .filter(models.Inning.game_id == game_id, models.Inning.top_bottom == top_bottom)
        .options(
            joinedload(models.Inning.atbats)
            .joinedload(models.AtBat.pitch_events)
            .joinedload(models.PitchEvent.advance_events)
        )
        .order_by(models.Inning.id)
        .all()
    )
    if not all_innings_with_events:
        raise HTTPException(status_code=404, detail="innings_with_events not found")
    return all_innings_with_events
    

def get_inning_with_events_by_pitch(
    db: Session,
    pitch_event_id: int
) -> models.Inning:
    """
    指定のpitch_eventが含まれるinningを取得
    """
    inning_id = get_inning_by_pitch(db, pitch_event_id).id
    inning_with_events = (
        db.query(models.Inning)
        .filter(models.Inning.id == inning_id)
        .options(
            joinedload(models.Inning.atbats)
            .joinedload(models.AtBat.pitch_events.and_(
                models.PitchEvent.id <= pitch_event_id
            ))
            .joinedload(models.PitchEvent.advance_events)
        )
        .first()
    )
    if not inning_with_events:
        raise HTTPException(status_code=404, detail="inning_with_events not found")
    return inning_with_events
    

def get_atbat_with_events_by_pitch(
    db: Session,
    pitch_event_id: int
) -> models.AtBat:
    """
    指定のpitch_eventが含まれるatbatを取得
    """
    atbat_id = get_atbat_by_pitch(db, pitch_event_id)
    atbat_with_events = (
        db.query(models.AtBat)
        .filter(models.AtBat.id == atbat_id)
        .options(
            joinedload(models.AtBat.pitch_events.and_(
                models.PitchEvent.id <= pitch_event_id
            ))
            .joinedload(models.PitchEvent.advance_events)
        )
        .first()
    )
    if not atbat_with_events:
        raise HTTPException(status_code=404, detail="atbat_with_events not found")
    return atbat_with_events


def get_pitch_events_of_latest_atbat(
    db: Session,
    game_id: int
) -> List[models.PitchEvent]:
    """
    現在のatbat中のpitch_eventsを取得
    投球がなければ（試合開始直後なら）[]を返す
    """
    latest_atbat = (
        db.query(models.AtBat)
        .join(models.Inning)
        .filter(models.Inning.game_id == game_id)
        .order_by(models.AtBat.id.desc())
        .first()
    )
    if not latest_atbat:
        raise HTTPException(status_code=404, detail="latest_atbat not found")
    
    pitch_events_of_latest_atbat = (
        db.query(models.PitchEvent)
        .filter(models.PitchEvent.atbat_id == latest_atbat.id)
        .order_by(models.PitchEvent.id)
        .all()
    )
    if not pitch_events_of_latest_atbat:
        return []
    return pitch_events_of_latest_atbat


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


def get_uniform_number_by_game_member_id(
    db: Session,
    game_member_id: int
) -> Optional[int]:
    """
    出場選手のidから背番号を取得
    """
    game_member = (
        db.query(models.GameMember)
        .options(joinedload(models.GameMember.member_profile))
        .filter(models.GameMember.id == game_member_id)
        .one_or_none()
    )

    if game_member is None:
        raise HTTPException(status_code=404, detail=f"game_member ID {game_member_id} not found")
    if game_member.member_profile is None:
        return None

    return game_member.member_profile.uniform_number


def get_starting_batter(
    db: Session,
    game_id: int
) -> models.GameMember:
    """
    試合の最初のバッターを取得
    """
    


# ------------------------
# 作成系
# ------------------------

def create_inning(
    db: Session,
    game_id: int,
    inning_number: int,
    top_bottom: models.TopBottomEnum
) -> models.Inning:
    """
    新しいinningを作成する
    """
    new_inning = models.Inning(
        game_id = game_id,
        inning_number = inning_number,
        top_bottom = top_bottom,
    )
    
    db.add(new_inning)
    db.commit()
    db.refresh(new_inning)
    
    return new_inning


def create_atbat(
    db: Session,
    inning_id: int,
    batter_id: int
) -> models.AtBat:
    """
    新しい打席を作成する
    """
    new_atbat = models.AtBat(
        inning_id = inning_id,
        batter_id = batter_id
    )
    
    db.add(new_atbat)
    db.commit()
    db.refresh(new_atbat)
    
    return new_atbat


def create_pitch_event(
    db: Session,
    atbat_id: int,
    input_data: schema.ScoreInput
) -> models.PitchEvent:
    """
    pitch_eventを作成する
    """
    new_pitch_event = models.PitchEvent(
        atbat_id = atbat_id,
        pitch_type = input_data.pitch_type,
        pitch_type_detail = input_data.pitch_type_detail,
        batting_form = input_data.batting_form,
        batting_side = input_data.batting_side,
        is_runner_first_steal = input_data.is_runners_steal.first,
        is_runner_second_steal = input_data.is_runners_steal.second,
        is_runner_third_steal = input_data.is_runners_steal.third,
    )
    
    db.add(new_pitch_event)
    db.commit()
    db.refresh(new_pitch_event)
    
    return new_pitch_event


def create_advance_event(
    db: Session,
    pitch_event_id: int,
    advs: List[schema.AdvanceElement]
) -> List[models.AdvanceEvent]:
    """
    advance_eventを作成する
    """
    new_advance_events = [
        models.AdvanceEvent(
            pitch_event_id = pitch_event_id,
            runner_id = adv.runner_id,
            from_base = adv.from_base,
            to_base = adv.to_base,
            is_out = adv.is_out,
            reason = adv.reason
        ) for adv in advs
    ]
    
    db.add_all(new_advance_events)
    db.commit()
    for event in new_advance_events:
        db.refresh(event)
    
    return new_advance_events


# ------------------------
# 更新系
# ------------------------

def update_atbat_result(
    db: Session,
    atbat_id: int,
    result: models.AtBatResultEnum
) -> models.AtBat:
    """
    atbat.resultを更新する
    """
    atbat = db.query(models.AtBat).filter(models.AtBat.id == atbat_id).first()
    if atbat:
        atbat.result = result
        db.commit()
        db.refresh(atbat)
    else:
        raise HTTPException(status_code=404, detail="atbat not found")
        
    return atbat


def update_game_member_enrty_number(
    db: Session,
    game_member_id: int
) -> models.GameMember:
    """
    game_member.entry_numberを更新する
    """
    game_member = db.query(models.GameMember).filter(models.GameMember.id == game_member_id).first()
    if game_member:
        game_member.entry_number += 1
        db.commit()
        db.refresh(game_member)
    else:
        raise HTTPException(status_code=404, detail="game_member not found")

    return game_member


def update_inning_score(
    db: Session,
    inning_id: int,
    score: int
) -> models.Inning:
    inning = db.query(models.Inning).filter(models.Inning.id == inning_id).first()
    if inning:
        inning.score = score
        db.commit()
        db.refresh(inning)
    else:
        raise HTTPException(status_code=404, detail="inning not found")
    
    return inning
