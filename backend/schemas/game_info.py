# backend/schemas/game_info.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

#-----------------
# for top
#-----------------

class ForGameBase(BaseModel):
    team_id: int
    team_short_name: str


class GameBase(BaseModel):
    top_team: ForGameBase
    bottom_team: ForGameBase
    date: date
    start_time: time
    end_time: time
    tournament: str
    location: str
    status: models.GameStatusEnum


class ForInningScore(BaseModel):
    team_short_name: str
    team_inning_id: List[int]
    team_inning_score: List[int]
    team_total_score: int
    team_total_hit: int


class InningScore(BaseModel):
    top_team: ForGameBase
    bottom_team: ForGameBase


class MemberWithPosition(BaseModel):
    member_id: int
    member_name: str
    member_order: int
    member_postion: models.PositionEnum


class ForStartingOrder(BaseModel):
    team_short_name: str
    team_member_with_position: List[MemberWithPosition]


class StartingOrder(BaseModel):
    top_team: ForStartingOrder
    bottom_team: ForStartingOrder
    

class MemberWithPositionType(BaseModel):
    member_id: int
    member_name: str
    member_position_type: models.PositionTypeEnum


class ForBenchMember(BaseModel):
    team_short_name: str
    team_member_with_position_type: List[MemberWithPositionType]


class BenchMember(BaseModel):
    top_team: ForBenchMember
    bottom_team: ForBenchMember
    

class EntryState(BaseModel):
    substitution_type: models.SubstitutionTypeEnum
    batting_order: models.BattingOrderEnum
    position: models.PositionEnum
    game_member_id: int
    game_member_name: str
    pitch_event_id: int


class ForEntryHistory(BaseModel):
    team_short_name: str
    entry_state: List[EntryState]
    

class EntryHistory(BaseModel):
    top_team: ForEntryHistory
    bottom_team: ForEntryHistory
    

class MemberWithName(BaseModel):
    member_id: int
    member_name: str


class ForBattery(BaseModel):
    team_short_name: str
    team_pitcher: List[MemberWithName]
    team_catcher: List[MemberWithName]


class Battery(BaseModel):
    top_team: ForBattery
    bottom_team: ForBattery


class MemberWithExtrabaseHit(BaseModel):
    member_id: int
    member_name: str
    extrabase_hit_count: int


class ForExtrabaseHit(BaseModel):
    team_short_name: str
    two_base_hit: MemberWithExtrabaseHit
    three_base_hit: MemberWithExtrabaseHit
    homerun: MemberWithExtrabaseHit


class ExtrabaseHit(BaseModel):
    top_team: ForExtrabaseHit
    bottom_team: ForExtrabaseHit
    
    
class GameInfoTop(BaseModel):
    num: int

    
#-----------------
# for live
#-----------------

class GameInfoLive(BaseModel):
    num: int

#-----------------
# for progress
#-----------------

class BallCount(BaseModel):
    ball: int
    strike: int


class SubstitutionEventForInningProgress(BaseModel):
    substitution_type: models.SubstitutionTypeEnum
    out_member: MemberWithName
    in_member: MemberWithName
    

class AdvanceAggregated(BaseModel):
    outs: int
    score: int
    runners: List[int]


class PitchEventForInningProgress(BaseModel):
    pitch_event_index: int
    pitch_event_type: str
    count_after: BallCount
    pitch_event_result: str
    substitutions: List[SubstitutionEventForInningProgress]


class AtBatForInningProgress(BaseModel):
    atbat_index: int
    batter_order: int
    batter_id: int
    batter_name: str
    outs: int
    runners: str
    pitchevents: List[PitchEventForInningProgress]


class ForInningProgress(BaseModel):
    inning_id: int
    inning_number: int
    inning_top_bottom: models.TopBottomEnum
    offense_team_name: str
    atbats: List[AtBatForInningProgress]
    

class InningProgress(BaseModel):
    progress: List[ForInningProgress]


class GameInfoProgress(BaseModel):
    num: int


#-----------------
# for stats
#-----------------

class BatterStats(BaseModel):
    batter_id: int
    batter_name: str
    batter_position_history: List[models.PositionEnum]
    average: float
    atbat: int
    hit: int
    rbi: int
    homerun: int
    steal: int


class ForAllBatterStats(BaseModel):
    team_short_name: str
    batter: List[BatterStats]


class AllBatterStats(BaseModel):
    top_team: ForAllBatterStats
    bottom_team: ForAllBatterStats
    
    
class PitcherStats(BaseModel):
    pitcher_id: int
    pitcher_name: str
    responsibility_type: models.ResponsibilityTypeEnum
    inning: int
    pitch_count: int
    hit: int
    strikeout: int
    balls: int
    hbp: int
    run: int


class ForAllPitcherStats(BaseModel):
    team_short_name: str
    pitcher: List[PitcherStats]


class AllPitcherStats(BaseModel):
    top_team: ForAllPitcherStats
    bottom_team: ForAllPitcherStats


class GameInfoStats(BaseModel):
    num: int