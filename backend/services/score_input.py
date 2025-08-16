# backend/services/score_input.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend import models
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from typing import Optional, List, Dict, Tuple
from backend.constants import play_mapping
from copy import deepcopy
from backend.constants import pitch_group

# ------------------------
# 状態計算（表示用）
# ------------------------

def get_offense_and_defense_team_id(
    db: Session,
    game_id: int
) -> Tuple[int]:
    """
    現在の攻撃チームと守備チームのidを取得
    """
    game = crud.get_game(db, game_id)
    latest_inning = crud.get_latest_inning(db, game_id)
    
    top_bottom = latest_inning.top_bottom
    if top_bottom == "top":
        offense_team_id = game.top_team_id
        defense_team_id = game.bottom_team_id
    else:
        offense_team_id = game.bottom_team_id
        defense_team_id = game.top_team_id
        
    if not offense_team_id:
        raise HTTPException(status_code=404, detail="offense_team_id not found")
    if not defense_team_id:
        raise HTTPException(status_code=404, detail="defense_team_id not found")
    return offense_team_id, defense_team_id


def get_entry_state(
    db: Session,
    game_id: int
) -> Tuple[schema.TeamEntryState]:
    """
    出場登録された選手の現在の出場状態を取得
    """
    game = crud.get_game(db, game_id)
    game_members_with_member_profile = crud.get_game_members_with_member_profile(db, game_id)
    all_substitution_events = crud.get_all_substitution_events(db, game_id)
    
    tmp_game_members_entry_state = {}
    
    for game_member in game_members_with_member_profile:
        if game_member.team_id not in (game.top_team_id, game.bottom_team_id):
            raise ValueError(f"team_id is invalid")
        
        game_member_entry_state = schema.GameMemberEntryState(
            batting_order = game_member.starting_batting_order,
            position = game_member.starting_position,
            entry_number = game_member.entry_number
        )
        tmp_game_members_entry_state[game_member.id] = game_member_entry_state
        
    for substitution_event in all_substitution_events:
        out_member_id = substitution_event.out_member_id
        in_member_id = substitution_event.in_member_id
        if out_member_id not in tmp_game_members_entry_state:
            raise ValueError(f"out_member_id is invalid")
        if in_member_id not in tmp_game_members_entry_state:
            raise ValueError(f"in_member_id is invalid")
        
        if substitution_event.is_position_change:
            tmp = tmp_game_members_entry_state[out_member_id].position
            tmp_game_members_entry_state[out_member_id].position = tmp_game_members_entry_state[in_member_id].position
            tmp_game_members_entry_state[in_member_id].position = tmp
        else:
            tmp_out = deepcopy(tmp_game_members_entry_state[out_member_id])
            tmp_in = deepcopy(tmp_game_members_entry_state[in_member_id])
            tmp_game_members_entry_state[in_member_id] = tmp_out
            tmp_game_members_entry_state[out_member_id] = tmp_in
            crud.update_game_member_enrty_number(db, in_member_id)
    
    top_team_entry_state = schema.TeamEntryState(
        team_id = game.top_team_id,
        game_members_entry_state = {}
    )
    bottom_team_entry_state = schema.TeamEntryState(
        team_id = game.bottom_team_id,
        game_members_entry_state = {}
    )
    
    for game_member in game_members_with_member_profile:
        if game_member.team_id == game.top_team_id:
            top_team_entry_state.game_members_entry_state[game_member.id] = tmp_game_members_entry_state[game_member.id]
        else:
            bottom_team_entry_state.game_members_entry_state[game_member.id] = tmp_game_members_entry_state[game_member.id]
    
    return top_team_entry_state, bottom_team_entry_state


def get_entering_members(
    db: Session,
    game_id: int,
) -> Dict[int, schema.TeamEnteringMembers]:
    top_team_entry_state, bottom_team_entry_state = get_entry_state(db, game_id)
    
    top_team_entering_members = {}
    bottom_team_entering_members = {}
    
    for top_team_game_member_id in top_team_entry_state.game_members_entry_state:
        top_team_game_member_entry_state = top_team_entry_state.game_members_entry_state[top_team_game_member_id]
        if top_team_game_member_entry_state.batting_order in range(1, 11):
            game_member = crud.get_game_member(db, top_team_game_member_id)
            top_team_entering_member = schema.EnteringMember(
                position = top_team_game_member_entry_state.position,
                game_member = schema.GameMember.model_validate(game_member, from_attributes=True)
            )
            top_team_entering_members[top_team_game_member_entry_state.batting_order] = top_team_entering_member
            
    for bottom_team_game_member_id in bottom_team_entry_state.game_members_entry_state:
        bottom_team_game_member_entry_state = bottom_team_entry_state.game_members_entry_state[bottom_team_game_member_id]
        if bottom_team_game_member_entry_state.batting_order in range(1, 11):
            game_member = crud.get_game_member(db, bottom_team_game_member_id)
            bottom_team_entering_member = schema.EnteringMember(
                position = bottom_team_game_member_entry_state.position,
                game_member = schema.GameMember.model_validate(game_member, from_attributes=True)
            )
            bottom_team_entering_members[bottom_team_game_member_entry_state.batting_order] = bottom_team_entering_member
    
    return {
        top_team_entry_state.team_id: top_team_entering_members,
        bottom_team_entry_state.team_id: bottom_team_entering_members
    }


def calc_bs_count(
    db: Session,
    game_id: int
) -> Tuple[int]:
    """
    現在のBSカウントを計算
    """
    pitch_events_of_latest_atbat = crud.get_pitch_events_of_latest_atbat(db, game_id)
    
    balls, strikes = 0, 0
    for pitch_event in pitch_events_of_latest_atbat:
        if pitch_event.pitch_type == models.PitchTypeEnum.ball:
            balls += 1
        elif pitch_event.pitch_type == models.PitchTypeEnum.others and pitch_event.pitch_type_detail == models.PitchTypeDetailEnum.illegal:
            balls += 1
        elif pitch_event.pitch_type in (models.PitchTypeEnum.swing_miss, models.PitchTypeEnum.looking):
            strikes += 1
        elif pitch_event.pitch_type == models.PitchTypeEnum.foul:
            if strikes < 2 or pitch_event.batting_form == models.BattingFormEnum.bunt:
                strikes += 1
    return balls, strikes


def aggregate_advance_events(
    db: Session,
    game_id: int
) -> Tuple[int]:
    """
    現在のinningのadvance_eventsからアウト、得点、ランナー計算
    """
    advance_events_of_latest_inning = crud.get_advance_events_of_latest_inning(db, game_id)
    
    outs, score = 0, 0
    runners_id = [0] * 4
    for advance_event in advance_events_of_latest_inning:
        runner_uniform_number = crud.get_uniform_number_by_game_member_id(db, advance_event.runner_id)
        
        if advance_event.from_base not in (0, 1, 2, 3):
            raise ValueError(f"from_base ({advance_event.from_base}) is invalid.")
        if advance_event.to_base not in (0, 1, 2, 3, 4):
            raise ValueError(f"to_base ({advance_event.to_base}) is invalid.")
        
        if advance_event.from_base == 0:
            batter_id = advance_event.pitch_event.atbat.batter_id
            batter_uniform_number = crud.get_uniform_number_by_game_member_id(db, batter_id)
            if advance_event.runner_id == batter_id:
                pass
            else:
                raise ValueError(f"mismatch in runner (#{runner_uniform_number}) and batter (#{batter_uniform_number})")
        else:
            if advance_event.runner_id == runners_id[advance_event.from_base]:
                pass
            else:
                raise ValueError(f"mismatch in runner (#{runner_uniform_number}) and previous runner (#{crud.get_uniform_number_by_game_member_id(db, runners_id[advance_event.from_base])})")
        
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
                    raise ValueError(f"runner (#{crud.get_uniform_number_by_game_member_id(db, runners_id[advance_event.to_base])}) is already on the base {advance_event.to_base}")
            elif advance_event.to_base == 4:
                score += 1
            else:
                raise ValueError(f"to_base (0) is invalid.")
        
    return outs, score, runners_id


def calc_past_inning_score(
    db: Session,
    game_id: int
) -> Tuple[List[int]]:
    """
    過去のイニングの得点を取得
    """
    all_innings_with_events = crud.get_all_innings_with_events(db, game_id)
    
    top_team_past_inning_score = []
    bottom_team_past_inning_score = []
    
    for inning in all_innings_with_events:
        if inning.score >= 0:
            if inning.top_bottom == models.TopBottomEnum.top:
                top_team_past_inning_score.append(inning.score)
            else:
                bottom_team_past_inning_score.append(inning.score)
    
    return top_team_past_inning_score, bottom_team_past_inning_score


def get_latest_state(
    db: Session,
    game_id: int
) -> schema.GameStateResponse:
    """
    現在の試合状況をまとめて取得
    """
    game = crud.get_game(db, game_id)
    latest_atbat = crud.get_latest_atbat(db, game_id)
    
    # 攻撃チーム、守備チーム
    offense_team_id, defense_team_id = get_offense_and_defense_team_id(db, game_id)
    offense_team = crud.get_team(db, offense_team_id)
    defense_team = crud.get_team(db, defense_team_id)
    # バッター
    batter = schema.GameMember.model_validate(latest_atbat.batter, from_attributes=True)
    # ボール、ストライク
    balls, strikes = calc_bs_count(db, game_id)
    # アウト、得点、ランナー(id)
    outs, score, runners_id = aggregate_advance_events(db, game_id)
    ball_count = schema.BallCount(
        balls = balls,
        strikes = strikes,
        outs = outs
    )
    runners = []
    for runner_id in runners_id:
        if runner_id > 0:
            runner = crud.get_game_member(db, runner_id)
            runners.append(schema.GameMember.model_validate(runner, from_attributes=True))
        else:
            runners.append(None)
    runners[0] = batter
    # 選手の出場状態
    top_team_entry_state, bottom_team_entry_state = get_entry_state(db, game_id)
    # 過去イニングの得点状況
    top_team_score, bottom_team_score = calc_past_inning_score(db, game_id)
    
    return schema.GameStateResponse(
        game_id = game_id,
        offense_team_id = offense_team_id,
        defense_team_id = defense_team_id,
        ball_count = ball_count,
        score = score,
        runners = runners,
        top_team_score = top_team_score,
        bottom_team_score = bottom_team_score,
        top_team_entry_state = schema.TeamEntryState.model_validate(top_team_entry_state, from_attributes=True),
        bottom_team_entry_state = schema.TeamEntryState.model_validate(bottom_team_entry_state, from_attributes=True),
    )
    

def get_all_innings_with_events_to_schema(
    db: Session,
    game_id: int
) -> List[schema.InningSchema]:
    """
    crud.get_all_innings_with_eventsで取得したデータをschema.Inningに合わせる
    """
    all_innings_with_events = crud.get_all_innings_with_events(db, game_id)
    return [schema.InningSchema.model_validate(inning_with_events, from_attributes=True) for inning_with_events in all_innings_with_events]
    

# ------------------------
# 試合進行
# ------------------------
# team_idからそのチームの完了した打席数->次の打順を計算
# 次の打順と打順表から次のbatter_idを取得
# advance_eventの候補作成

def game_start(
    db: Session,
    game_id: int
) -> models.AtBat:
    """
    試合情報に基づき、最初のイニング、打席を作成。
    試合開始時に1回だけ実行される
    """
    atbat = crud.get_latest_atbat(db, game_id)
    if atbat:
        raise HTTPException(status_code=400, detail="game had already started")
    
    inning = crud.create_inning(db, game_id, 1, "top")
    
    game = crud.get_game(db, game_id)
    entering_members = get_entering_members(db, game_id)[game.top_team_id]
    batter = entering_members[1].game_member
    
    atbat = crud.create_atbat(db, inning.id, batter.id)
    
    return atbat


def suggest_main_advance_events(
    db: Session,
    game_id: int,
    input_data: schema.ScoreInput
) -> List[Optional[schema.AdvanceCandidate]]:
    """
    想定されるエラーまで含めた進塁イベントをサジェスト
    """    
    game_state = get_latest_state(db, game_id)
    
    if pitch_group.in_group(input_data.pitch_type, "ball_dead"):
        ### 確定的進塁
        return play_mapping.make_others(
            runners = game_state.runners,
            ball_count = game_state.ball_count,
            pitch_type = input_data.pitch_type,
            pitch_type_detail = input_data.pitch_type_detail,
            leaving_base = input_data.leaving_base
        )

    elif pitch_group.in_group(input_data.pitch_type, "count"):
        ### ボール、ストライク
        return play_mapping.make_pitch_only(
            runners = game_state.runners,
            ball_count = game_state.ball_count,
            is_runners_steal = input_data.is_runners_steal
        )

    elif pitch_group.in_group(input_data.pitch_type, "inplays"):
        ### 打球あり
        # atbat,
        # runners,
        # is_runners_steal,
        # position,
        # batted_ball_type,
        # outs
        pass

    # if input_data.pitch_type == models.PitchTypeEnum.foul:
    #     # nothing
    #     return [[]]

    # elif pitch_group.in_group(input_data.pitch_type, "count"):
    #     # pitch_type, balls, strikes, outs, runners, is_runner_steal
    #     return play_mapping.make_pitch_only(
    #         pitch_type = input_data.pitch_type,
    #         ball_count = game_state.ball_count,
    #         runners = game_state.runners,
    #         is_runners_steal = input_data.is_runners_steal
    #     )

    # elif input_data.pitch_type == models.PitchTypeEnum.inplay:
    #     # position, direction, type, ball_count, runners, is_runner_steal
    #     return play_mapping.make_inplay(
    #         position = input_data.position,
    #         ball_direction = input_data.ball_direction,
    #         ball_type = input_data.ball_type,
    #         outs = game_state.ball_count.outs,
    #         runners = game_state.runners,
    #         is_runners_steal = input_data.is_runners_steal
    #     )
    
    # elif input_data.pitch_type == models.PitchTypeEnum.others:
    #     # pitch_type_detail, (leaving_runner), runners, 
    #     return play_mapping.make_others(
    #         pitch_type_detail = input_data.pitch_type_detail,
    #         runners = game_state.runners,
    #         leaving_base = input_data.leaving_base
    #     )


def get_following_batter(
    db: Session,
    game_id: int,
    skip: int = 1
) -> models.GameMember:
    """
    先攻・後攻のチームの次の打者を取得
    """
    last_inning = crud.get_latest_inning(db, game_id)
    innings_with_events = crud.get_top_bottom_innings_with_events(db, game_id, last_inning.top_bottom)
    
    cnt = 0
    for inning_with_events in innings_with_events:
        for atbat in inning_with_events.atbats:
            if atbat.result:
                cnt += 1
    order = (cnt + skip) % 9
    
    game = crud.get_game(db, game_id)
    if last_inning.top_bottom == models.TopBottomEnum.top:
        team_id = game.top_team_id
    else:
        team_id = game.bottom_team_id
    
    entering_members = get_entering_members(db, game_id)[team_id]
    
    return entering_members[order].game_member


def create_next_inning(
    db: Session,
    game_id: int,
    inning: models.Inning
) -> models.Inning:
    """
    次のイニングを作成する
    """
    if inning.top_bottom == models.TopBottomEnum.top:
        return crud.create_inning(db, game_id, inning.inning_number, models.TopBottomEnum.bottom)
    else:
        return crud.create_inning(db, game_id, inning.inning_number + 1, models.TopBottomEnum.top)

    
def suggest_additional_advance_events():
    """
    想定されないエラーによる進塁を追加でサジェスト
    """
    

def apply_advance_events():
    """
    フロントで選択した進塁を登録
    """
    

def change_inning():
    """
    3アウトでチェンジして次のイニング、打席を作成
    """


def register_pitch_event(
    db: Session,
    game_id: int,
    input_data: schema.ScoreInput
):
    """
    投球内容を受けて、チェンジの判定・反映まで一連を行う
    """
    balls, strikes = calc_bs_count(db, game_id)
    outs, score, runners_id = aggregate_advance_events(db, game_id)
    
