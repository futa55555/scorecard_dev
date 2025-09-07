# backend/services/game_info.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Dict, List
from datetime import date
from backend import models
from backend.schemas import game_info as schema
from backend.cruds import game_info as crud
from backend.constants import pitch_group

def get_game_base(
    db: Session,
    game_id: int
) -> schema.GameBase:
    """
    試合の基本情報を取得
    """
    game = crud.get_game_base(db, game_id)
    
    top_team = schema.ForGameBase(
        team_id = game.top_team_id,
        team_short_name = game.top_team.short_name
    )
    bottom_team = schema.ForGameBase(
        team_id = game.bottom_team_id,
        team_short_name = game.bottom_team.short_name
    )
    
    return schema.GameBase(
        top_team = top_team,
        bottom_team = bottom_team,
        date = game.date,
        start_time = game.start_time,
        end_time = game.end_time,
        tournament = game.tournament,
        location = game.location,
        status = game.status
    )
    
    
def calc_total_score(
    innings: List[models.Inning]
) -> Dict[str, int]:
    """
    チームの総得点と総安打数を計算
    """
    atbats = innings.atbats
    
    team_total_score = 0
    team_total_hit = 0
    
    for i in innings:
        team_total_score += i.score
        for atbat in atbats:
            if atbat.result == models.AtBatResultEnum.hit:
                team_total_hit += 1
    
    return {
        "team_total_score": team_total_score,
        "team_total_hit": team_total_hit,
    }


def get_inning_score(
    db: Session,
    game_id: int
) -> schema.InningScore:
    """
    チームごとの各イニングの得点と総得点、総安打数を取得
    """
    game = crud.get_game_base(db, game_id)
    innings = crud.get_all_innings(db, game_id)
    
    top_team_innings = [i for i in innings if i.top_bottom == models.TopBottomEnum.top]
    total_score = calc_total_score(top_team_innings)
    
    top_team = schema.ForInningScore(
        team_short_name = game.top_team.short_name,
        team_inning_id = [i.id for i in innings],
        team_inning_score = [i.score for i in innings],
        team_total_score = total_score["team_total_score"],
        team_total_hit = total_score["team_total_hit"]
    )
    
    bottom_team_innings = [i for i in innings if i.top_bottom == models.TopBottomEnum.bottom]
    total_score = calc_total_score(bottom_team_innings)
    
    bottom_team = schema.ForInningScore(
        team_short_name = game.bottom_team.short_name,
        team_inning_id = [i.id for i in innings],
        team_inning_score = [i.score for i in innings],
        team_total_score = total_score["team_total_score"],
        team_total_hit = total_score["team_total_hit"]
    )
    
    return schema.InningScore(
        top_team = top_team,
        bottom_team = bottom_team
    )


def get_starting_order(
    db: Session,
    game_id: int
) -> schema.StartingOrder:
    """
    スタメンをチームごとに分けて取得
    """
    game = crud.get_game_base(db, game_id)
    starting_members = crud.get_starting_member(db, game_id)
    
    top_team_member_with_position = [
        schema.MemberWithPosition(
            member_id = sm.id,
            member_name = sm.person.name,
            member_order = sm.starting_batting_order,
            member_position = sm.starting_position
        ) for sm in starting_members if sm.team_id == game.top_team_id
    ]
    
    top_team = schema.ForStartingOrder(
        team_short_name = game.top_team.short_name,
        team_member_with_position = top_team_member_with_position
    )
    
    bottom_team_member_with_position = [
        schema.MemberWithPosition(
            member_id = sm.id,
            member_name = sm.person.name,
            member_order = sm.starting_batting_order,
            member_position = sm.starting_position
        ) for sm in starting_members if sm.team_id == game.bottom_team_id
    ]
    
    bottom_team = schema.ForStartingOrder(
        team_short_name = game.bottom_team.short_name,
        team_member_with_position = bottom_team_member_with_position
    )
    
    return schema.StartingOrder(
        top_team = top_team,
        bottom_team = bottom_team
    )
    

def get_member_position_type(
    db: Session,
    person_id: int,
    date: date
) -> models.PositionTypeEnum:
    """
    その人物がその日にどの守備位置だったかを取得
    """
    position_type = crud.get_position_type(db, person_id)
    
    for pt in position_type:
        if pt.since_date >= date and pt.until_date <= date:
            return pt.position_type
    
    raise HTTPException(status_code=404, detail="player position type not found")


def get_bench_member(
    db: Session,
    game_id: int
) -> schema.BenchMember:
    """
    控えをチームごとに分けて取得
    """
    game = crud.get_game_base(db, game_id)
    bench_members = crud.get_bench_member(db, game_id)
    
    top_team_member_with_position_type = [
        schema.MemberWithPositionType(
            member_id = sm.id,
            member_name = sm.person.name,
            member_position_type = get_member_position_type(db, sm.person_id, game.date)
        ) for sm in bench_members if sm.team_id == game.top_team_id
    ]
    
    top_team = schema.ForBenchMember(
        team_short_name = game.top_team.short_name,
        team_member_with_position_type = top_team_member_with_position_type
    )
    
    bottom_team_member_with_position_type = [
        schema.MemberWithPositionType(
            member_id = sm.id,
            member_name = sm.person.name,
            member_position_type = get_member_position_type(db, sm.person_id, game.date)
        ) for sm in bench_members if sm.team_id == game.bottom_team_id
    ]
    
    bottom_team = schema.ForBenchMember(
        team_short_name = game.bottom_team.short_name,
        team_member_with_position_type = bottom_team_member_with_position_type
    )
    
    return schema.BenchMember(
        top_team = top_team,
        bottom_team = bottom_team
    )
    

def get_entry_history(
    db: Session,
    game_id: int
) -> schema.EntryHistory:
    """
    出場選手たちの出場履歴を取得
    """
    game = crud.get_game_base(db, game_id)
    starting_member = crud.get_starting_member(db, game_id)
    
    top_team_entry_state = [
        schema.EntryState(
            batting_order = sm.starting_batting_order,
            position = sm.starting_position,
            game_member_id = sm.id,
            game_member_name = sm.person.name,
            pitch_event_id = 1
        ) for sm in starting_member if sm.team_id == game.top_team_id
    ]
    
    bottom_team_entry_state = [
        schema.EntryState(
            batting_order = sm.starting_batting_order,
            position = sm.starting_position,
            game_member_id = sm.id,
            game_member_name = sm.person.name,
            pitch_event_id = 1
        ) for sm in starting_member if sm.team_id == game.bottom_team_id
    ]
    
    all_substitution_events = crud.get_all_substitution_events(db, game_id)
    
    for se in all_substitution_events:
        if se.sub_member.team_id == game.top_team_id:
            top_team_entry_state.append(
                schema.EntryState(
                    substitution_type = se.substitution_type,
                    batting_order = se.after_batting_order,
                    position = se.after_position,
                    game_member_id = se.sub_member_id,
                    game_member_name = se.sub_member.person.name,
                    pitch_event_id = se.pitch_event_id
                )
            )
        else:
            bottom_team_entry_state.append(
                schema.EntryState(
                    substitution_type = se.substitution_type,
                    batting_order = se.after_batting_order,
                    position = se.after_position,
                    game_member_id = se.sub_member_id,
                    game_member_name = se.sub_member.person.name,
                    pitch_event_id = se.pitch_event_id
                )
            )
    
    top_team = schema.ForEntryHistory(
        team_short_name = game.top_team.short_name,
        entry_state = top_team_entry_state
    )
    
    bottom_team = schema.ForEntryHistory(
        team_short_name = game.bottom_team.short_name,
        entry_state = bottom_team_entry_state
    )
    
    return schema.EntryHistory(
        top_team = top_team,
        bottom_team = bottom_team
    )


def get_battery(
    db: Session,
    game_id: int
) -> schema.Battery:
    """
    バッテリーをチームごとに取得
    """
    game = crud.get_game_base(db, game_id)
    entry_history = get_entry_history(db, game_id)
    
    top_team_pitcher = [
        schema.MemberWithName(
            member_id = es.game_member_id,
            member_name = es.game_member_name
        )
        for es in entry_history.top_team.entry_state
        if es.substitution_type in {
            models.SubstituionTypeEnum.PC,
            models.SubstitutionTypeEnum.conti
        } and es.position == models.PositionEnum.P
    ]
    
    top_team_catcher = [
        schema.MemberWithName(
            member_id = es.game_member_id,
            member_name = es.game_member_name
        )
        for es in entry_history.top_team.entry_state
        if es.substitution_type in {
            models.SubstituionTypeEnum.PC,
            models.SubstitutionTypeEnum.conti
        } and es.position == models.PositionEnum.C
    ]
    
    top_team = schema.ForBattery(
        team_short_name = game.top_team.short_name,
        team_pitcher = top_team_pitcher,
        team_catcher = top_team_catcher
    )
    
    bottom_team_pitcher = [
        schema.MemberWithName(
            member_id = es.game_member_id,
            member_name = es.game_member_name
        )
        for es in entry_history.bottom_team.entry_state
        if es.substitution_type in {
            models.SubstitutionTypeEnum.PC,
            models.SubstitutionTypeEnum.conti
        } and es.position == models.PositionEnum.P
    ]
    
    bottom_team_catcher = [
        schema.MemberWithName(
            member_id = es.game_member_id,
            member_name = es.game_member_name
        )
        for es in entry_history.bottom_team.entry_state
        if es.substitution_type in {
            models.SubstitutionTypeEnum.PC,
            models.SubstitutionTypeEnum.conti
        } and es.position == models.PositionEnum.C
    ]
    
    bottom_team = schema.ForBattery(
        team_short_name = game.bottom_team.short_name,
        team_pitcher = bottom_team_pitcher,
        team_catcher = bottom_team_catcher
    )
    
    return schema.Battery(
        top_team = top_team,
        bottom_team = bottom_team
    )


def get_extrabase_hit(
    db: Session,
    game_id: int
) -> schema.ExtrabaseHit:
    """
    長打を打った打者をチームごとに取得
    """
    game = crud.get_game_base(db, game_id)
    all_atbats = crud.get_all_atbats(db, game_id)
    
    top_team_two_base_hit = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    top_team_three_base_hit = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    top_team_homerun = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    
    top_team = schema.ForExtrabaseHit(
        team_short_name = game.top_team.short_name,
        two_base_hit = top_team_two_base_hit,
        three_base_hit = top_team_three_base_hit,
        homerun = top_team_homerun,
    )

    bottom_team_two_base_hit = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    bottom_team_three_base_hit = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    bottom_team_homerun = [
        schema.MemberWithName(
            member_id = a.responsible_batter.id,
            member_name = a.responsible_batter.person.name
        )
        for a in all_atbats
        if a.responsible_batter.team_id == game.top_team_id
        and a.result == models.AtBatResultEnum.hit
    ]
    
    bottom_team = schema.ForExtrabaseHit(
        team_short_name = game.bottom_team.short_name,
        two_base_hit = bottom_team_two_base_hit,
        three_base_hit = bottom_team_three_base_hit,
        homerun = bottom_team_homerun,
    )
    
    return schema.ExtrabaseHit(
        top_team = top_team,
        bottom_team = bottom_team
    )


def get_ball_count(
    db: Session,
    game_id: int
) -> schema.BallCount:
    """
    ボールカウントを取得
    """
    latest_atbat = crud.get_latest_atbat_with_pitch_events(db, game_id)
    pitch_events = latest_atbat.pitch_events
    
    balls, strikes = 0, 0
    for pitch_event in pitch_events:
        if pitch_event.pitch_type == models.PitchTypeEnum.ball:
            balls += 1
        elif pitch_event.pitch_type == models.PitchTypeEnum.others and pitch_event.pitch_type_detail == models.PitchTypeDetailEnum.illegal:
            balls += 1
        elif pitch_group.in_group(pitch_event.pitch_type, "strike"):
            strikes += 1
        elif pitch_event.pitch_type == models.PitchTypeEnum.foul:
            if strikes < 2 or pitch_event.batting_form == models.BattingFormEnum.bunt:
                strikes += 1
    return schema.BallCount(
        ball = balls,
        strike = strikes
    )


def aggregate_advance_events(
    db: Session,
    game_id: int
) -> schema.AdvanceAggregated:
    """
    現在のinningのadvance_eventsからアウト、得点、ランナー計算
    """
    advance_events_of_latest_inning = crud.get_advance_events_of_latest_inning(db, game_id)
    
    outs, score = 0, 0
    runners_id = [0] * 4
    for advance_event in advance_events_of_latest_inning:
        runner = crud.get_game_member_by_id(db, advance_event.runner_id)
        
        if advance_event.from_base not in (0, 1, 2, 3):
            raise ValueError(f"from_base ({advance_event.from_base}) is invalid.")
        if advance_event.to_base not in (0, 1, 2, 3, 4):
            raise ValueError(f"to_base ({advance_event.to_base}) is invalid.")
        
        if advance_event.from_base == 0:
            batter_id = advance_event.pitch_event.atbat.responsible_batter_id
            batter = crud.get_game_member_by_id(db, batter_id)
            if advance_event.runner_id == batter_id:
                pass
            else:
                raise ValueError(f"mismatch in runner (#{runner.person.name}) and batter (#{batter.person.name})")
        else:
            if advance_event.runner_id == runners_id[advance_event.from_base]:
                pass
            else:
                raise ValueError(f"mismatch in runner (#{runner.person.name}) and previous runner (#{crud.get_game_member_by_id(db, runners_id[advance_event.from_base])})")
        
        if advance_event.is_out:
            runners_id[advance_event.from_base] = 0
            outs += 1
        else:
            if not any(runners_id[advance_event.from_base + 1: advance_event.to_base]):
                pass
            else:
                raise ValueError("runner cannot pass another runner")
            
            runners_id[advance_event.from_base] = 0
            if advance_event.to_base in (1, 2, 3):
                if runners_id[advance_event.to_base] == 0:
                    runners_id[advance_event.to_base] = advance_event.runner_id
                else:
                    raise ValueError(f"runner (#{crud.get_game_member_by_id(db, runners_id[advance_event.to_base])}) is already on the base {advance_event.to_base}")
            elif advance_event.to_base == 4:
                score += 1
            else:
                raise ValueError(f"to_base (0) is invalid.")
        
    return schema.AdvanceAggregated(
        outs = outs,
        score = score,
        runners = runners_id
    )



