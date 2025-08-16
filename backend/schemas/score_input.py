# backend/schemas/score_input.py

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Tuple, Dict
from backend import models
from datetime import date, time

class RunnersSteal(BaseModel):
    first: bool = False
    second: bool = False
    third: bool = False

class ScoreInput(BaseModel):
    pitch_type: models.PitchTypeEnum  # swing_miss, looking, ball, foul, inplay, others
    position: Optional[models.PositionEnum] = None
    ball_direction: Optional[models.BattedBallDirectionEnum] = None
    ball_type: Optional[models.BattedBallTypeEnum] = None
    pitch_type_detail: Optional[models.PitchTypeDetailEnum] = None  # others用
    leaving_base: Optional[int]
    batting_form: models.BattingFormEnum  # hitting | bunt | slap
    batting_side: models.BattingSideEnum  # R | L | S
    is_runners_steal: RunnersSteal
    
class GameMemberEntryState(BaseModel):
    batting_order: models.BattingOrderEnum
    position: models.PositionEnum
    entry_number: int
    
class TeamEntryState(BaseModel):
    team_id: int
    game_members_entry_state: Dict[int, GameMemberEntryState]
    model_config = ConfigDict(from_attributes=True)

class Game(BaseModel):
    id: int
    top_team_id: int
    bottom_team_id: int
    date: Optional[date]
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    location: Optional[str]
    model_config = ConfigDict(from_attributes=True)

class Team(BaseModel):
    id: int
    name: str
    short_name: Optional[str]
    is_myteam: bool
    prefecture: models.PrefectureEnum
    league: Optional[str]
    photo_url: Optional[str]
    color: Optional[str]
    model_config = ConfigDict(from_attributes=True)

class GameMember(BaseModel):
    id: int
    game_id: int
    team_id: int
    member_profile_id: int
    starting_batting_order: models.BattingOrderEnum
    starting_position: models.PositionEnum
    entry_number: Optional[int]
    model_config = ConfigDict(from_attributes=True)
    
class BallCount(BaseModel):
    balls: int
    strikes: int
    outs: int
    
class GameStateResponse(BaseModel):
    game_id: int
    offense_team_id: int
    defense_team_id: int
    ball_count: BallCount
    score: int
    runners: List[Optional[GameMember]]
    top_team_score: List[int]
    bottom_team_score: List[int]
    top_team_entry_state: TeamEntryState
    bottom_team_entry_state: TeamEntryState

class EnteringMember(BaseModel):
    position: models.PositionEnum
    game_member: GameMember
    
class TeamEnteringMembers(BaseModel):
    entering_members: Dict[int, EnteringMember]
    
class AdvanceElement(BaseModel):
    runner_id: int
    from_base: int
    to_base: int
    is_out: bool
    is_by_atbat: bool
    out_type: Optional[models.OutTypeEnum] = None
    ball_flow: Optional[List[models.PositionEnum]] = []
    advance_by_pitch: Optional[models.AdvanceByPitchEnum] = None
    
class AdvanceCandidate(BaseModel):
    atbat_result: Optional[models.AtBatResultEnum]
    advance_elements: List[Optional[AdvanceElement]]

class MainAdvenceCandidates(BaseModel):
    num_of_candidates: int
    candidates: List[Optional[AdvanceCandidate]]

class AdvanceCandidateConfirm(BaseModel):
    change: bool
    selected_candidate: List[Optional[AdvanceElement]]
    
class ChangeInput(BaseModel):
    change: bool

class AdvanceEventSchema(BaseModel):
    id: int
    pitch_event_id: int
    runner_id: int
    from_base: int
    to_base: int
    is_out: bool
    is_by_atbat: bool
    out_type: Optional[models.OutTypeEnum]
    ball_flow: Optional[List[models.PositionEnum]]
    advance_by_pitch: Optional[models.AdvanceByPitchEnum]
    model_config = ConfigDict(from_attributes=True)

class PitchEventSchema(BaseModel):
    id: int
    atbat_id: int
    pitch_type: Optional[models.PitchTypeEnum]
    pitch_type_detail: Optional[models.PitchTypeDetailEnum]
    batting_form: Optional[models.BattingFormEnum]
    batting_side: Optional[models.BattingSideEnum]
    is_runner_first_steal: bool
    is_runner_second_steal: bool
    is_runner_third_steal: bool
    advance_events: List[AdvanceEventSchema]
    model_config = ConfigDict(from_attributes=True)

class AtBatSchema(BaseModel):
    id: int
    inning_id: int
    batter_id: Optional[int]
    result: Optional[str]  # 打席確定時のみ
    pitch_events: List[PitchEventSchema]
    model_config = ConfigDict(from_attributes=True)

class InningSchema(BaseModel):
    id: int
    game_id: int
    inning_number: int
    top_bottom: models.TopBottomEnum
    score: int
    atbats: List[AtBatSchema]
    model_config = ConfigDict(from_attributes=True)

class StateWithInnings(BaseModel):
    state: GameStateResponse
    all_innings_with_events: List[InningSchema]
