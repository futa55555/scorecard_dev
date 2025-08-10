# backend/schemas/score_input.py

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Tuple, Dict
from backend import models
from datetime import date, time


class ScoreInput(BaseModel):
    pitch_type: models.PitchTypeEnum  # swing_miss, looking, ball, foul, inplay, others
    pitch_type_detail: Optional[models.PitchTypeDetailType] = None  # others用
    batting_form: models.BattingFormEnum  # hitting | bunt | slap
    batting_side: models.BattingSideEnum  # R | L | S

    is_runner_first_steal: bool = False
    is_runner_second_steal: bool = False
    is_runner_third_steal: bool = False
    
class GameMemberEntryState(BaseModel):
    batting_order: models.BattingOrderEnum
    position: models.PositionEnum
    entry_number: int
    
class TeamEntryState(BaseModel):
    team_id: int
    game_members_entry_state: Dict[int, GameMemberEntryState]
    model_config = ConfigDict(from_attributes=True)
    
class AdvanceDetail(BaseModel):
    """
    進塁候補の1つ
    """
    runner_id: int
    from_base: Optional[int]
    to_base: Optional[int]
    is_out: bool
    reason: Optional[str] = None
    
class ConfirmScoreInput(BaseModel):
    pitch_event_id: int
    candidate_id: int
    
class Game(BaseModel):
    id: int
    top_team_id: int
    bottom_team_id: int
    date: Optional[date]
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    location: str

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
    
class GameStateResponse(BaseModel):
    game: Game
    top_team_entry_state: TeamEntryState
    bottom_team_entry_state: TeamEntryState
    offense_team: Team
    defense_team: Team
    batter: GameMember
    balls: int
    strikes: int
    outs: int
    score: int
    runners_by_uniform_number: List[GameMember]
    top_team_score: List[int]
    bottom_team_score: List[int]

    class Config:
        from_attributes = True

class EnteringMember(BaseModel):
    position: models.PositionEnum
    game_member: GameMember
    
class TeamEnteringMembers(BaseModel):
    entering_members: Dict[int, EnteringMember]
    
class AdvanceEventSchema(BaseModel):
    id: int
    from_base: Optional[int]
    to_base: Optional[int]
    runner_id: Optional[int]
    reason: Optional[str]
    is_out: Optional[bool]


class PitchEventSchema(BaseModel):
    id: int
    description: Optional[str]    # 例: 見逃し/空振り/ゴロなど
    pitch_type_detail: Optional[str] = None # 表示用
    advance_events: List[AdvanceEventSchema] = []


class AtBatWithEvents(BaseModel):
    id: int
    game_id: int
    batter_id: Optional[int]
    result: Optional[str]  # 打席確定時のみ
    inning: Optional[int]
    top_bottom: Optional[models.TopBottomEnum]
    pitch_events: List[PitchEventSchema] = []

    class Config:
        from_attributes = True
        
class GameState(BaseModel):
    outs: int
    runners: List[Optional[int]]
    runners_str: str
    balls: int
    strikes: int

class StateWithAtBats(BaseModel):
    state: GameState
    atbats: List[AtBatWithEvents]
    
    class Config:
        from_attributes = True



# class AdvanceCandidate(BaseModel):
#     candidate_id: int  # 選択用のID
#     advances: List[AdvanceDetail]

# class ScoreInputResponse(BaseModel):
#     atbat_id: int
#     pitch_event_id: int
#     requires_confirmation: bool = False
#     advance_candidates: List[AdvanceCandidate] = []
    
#     class Config:
#         from_attributes = True

# class ConfirmAdvance(BaseModel):
#     runner_id: int
#     from_base: Optional[int]
#     to_base: Optional[int]
#     is_out: bool

# class ConfirmScoreInput(BaseModel):
#     pitch_event_id: int
#     candidate_id: int

# class AdvanceEventResponse(BaseModel):
#     id: int
#     pitch_event_id: int
#     runner_id: int
#     from_base: Optional[int]
#     to_base: Optional[int]
#     is_out: bool
#     via_error: bool
#     reason: Optional[str]

#     class Config:
#         from_attributes = True

# class ConfirmScoreInputResponse(BaseModel):
#     pitch_event_id: int
#     confirmed_advances: List[AdvanceEventResponse]
#     outs: int
#     runners: List[Optional[int]]  # [一塁, 二塁, 三塁] の runner_id
#     runners_str: str              # "101" 形式
#     change_sides: bool

#     class Config:
#         from_attributes = True
