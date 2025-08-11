# backend/services/score_input.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend import models
from backend.schemas import score_input as schema
from backend.cruds import score_input as crud
from typing import Optional, List, Dict, Tuple
from backend.constants.play_mapping.utils import find_candidates
from copy import deepcopy

# # ------------------------
# # 状態計算
# # ------------------------

# def get_game_state(db: Session, game_id: int):
#     """
#     現在の試合状態を返す:
#       - アウト数
#       - ランナーID配列 [一塁,二塁,三塁]
#       - ランナー文字列 "101"
#       - ボール・ストライクカウント
#     打者が一塁に達しないアウトは AtBat.result で扱い、
#     ランナーの動きは AdvanceEvent で扱う。
#     """
#     atbat = crud.get_latest_atbat(db, game_id)
#     if not atbat:
#         return {
#             "outs": 0,
#             "runners": [None, None, None],
#             "runners_str": "000",
#             "balls": 0,
#             "strikes": 0
#         }

#     # --- ランナーとランナーアウトを集計 ---
#     advance_events = crud.get_all_advance_events(db, game_id)
#     bases = {1: None, 2: None, 3: None}
#     runner_outs = 0

#     for ev in advance_events:
#         if ev.from_base in bases:
#             bases[ev.from_base] = None

#         if ev.is_out:
#             runner_outs += 1
#         elif ev.to_base and ev.to_base <= 3:
#             bases[ev.to_base] = ev.runner_id

#     runners = [bases[1], bases[2], bases[3]]
#     runners_str = "".join(["1" if r else "0" for r in runners])

#     outs = runner_outs

#     # --- ボール・ストライクカウント ---
#     balls, strikes = 0, 0
#     for pitch in atbat.pitch_events:
#         if pitch.description in ("swing_miss", "looking"):
#             strikes += 1
#         elif pitch.description == "ball":
#             balls += 1
#         elif pitch.description == "foul" and strikes < 2:
#             strikes += 1
#         elif pitch.description == "inplay":
#             break  # 打席終了想定
        
    

#     return {
#         "outs": outs,
#         "runners": runners,         # [None, 12, None]
#         "runners_str": runners_str, # "010"
#         "balls": balls,
#         "strikes": strikes
#     }


# # ------------------------
# # 次打者・攻守管理
# # ------------------------

# def get_current_inning_and_half(db: Session, game_id: int):
#     """現在の回数と表裏を返す（3アウトで攻守交代）"""
#     last_atbat = crud.get_latest_atbat(db, game_id)
#     if not last_atbat:
#         return 1, models.TopBottomEnum.top

#     state = get_game_state(db, game_id)
#     outs = state["outs"]

#     inning = last_atbat.inning or 1
#     half = last_atbat.top_bottom or models.TopBottomEnum.top

#     if outs >= 3:
#         if half == models.TopBottomEnum.top:
#             return inning, models.TopBottomEnum.bottom
#         else:
#             return inning + 1, models.TopBottomEnum.top

#     return inning, half


# def get_offense_team_id(db: Session, game_id: int):
#     """現在攻撃中のチームIDを返す"""
#     game = db.query(models.Game).filter(models.Game.id == game_id).first()
#     if not game:
#         raise ValueError("Game not found")

#     inning, half = get_current_inning_and_half(db, game_id)
#     return (
#         game.first_attack_team_id
#         if half == models.TopBottomEnum.top
#         else game.team1_id
#         if game.team1_id != game.first_attack_team_id
#         else game.team2_id
#     )


# def get_next_batter(db: Session, game_id: int, offense_team_id: int) -> models.GameMember:
#     """現在の打者を基に次打者を返す"""
#     lineup = (
#         db.query(models.GameMember)
#         .filter(
#             models.GameMember.game_id == game_id,
#             models.GameMember.team_id == offense_team_id,
#             models.GameMember.batting_order.between(1, 9)
#         )
#         .order_by(models.GameMember.batting_order.asc())
#         .all()
#     )
    
#     if not lineup:
#         raise ValueError("打順が設定されていません")

#     last_order = crud.get_last_batting_order(db, game_id)
#     if not last_order or last_order == 9:
#         return lineup[0]

#     next_order = last_order + 1
#     if next_order > len(lineup):
#         next_order = 1

#     return next(g for g in lineup if g.batting_order == next_order)


# # (game_id, pitch_id) -> 候補リスト
# CANDIDATE_CACHE: Dict[tuple[int, int], List[dict]] = {}


# def record_pitch_event(
#     db: Session,
#     game_id: int,
#     input_data: schema.ScoreInputSchema
# ) -> schema.ScoreInputResponse:
#     """
#     投球1球を記録し、進塁候補を返却するサービス関数
#       1. 打席がなければ作成
#       2. PitchEvent 作成（投球番号付き + カウント保存）
#       3. 入力に応じて進塁候補を生成（未確定）
#       4. ScoreInputResponse を返却
#     """
#     # --- イニングと表裏、攻撃チームを取得 ---
#     inning, half = get_current_inning_and_half(db, game_id)
#     offense_team_id = get_offense_team_id(db, game_id)

#     # --- 現在の打席を取得 or 作成 ---
#     atbat = crud.get_current_atbat_with_events(db, game_id)
#     if atbat is None or atbat.result != None:
#         batter = get_next_batter(db, game_id, offense_team_id)
#         atbat = crud.create_atbat(db, game_id, batter.id, inning, half)

#     # --- 現在のカウント取得 ---
#     state = get_game_state(db, game_id)
#     balls_before, strikes_before = state["balls"], state["strikes"]
#     outs = state["outs"]
#     bases = state["runners"]
#     bases_str = state["runners_str"]
#     batter_id = atbat.batter_id

#     # --- カウント進行 ---
#     balls_after = balls_before
#     strikes_after = strikes_before
    
#     description = input_data.description
#     if description == "ball":
#         balls_after += 1
#     elif description in ("swing_miss", "looking"):
#         strikes_after += 1
#     elif description == "foul":
#         if input_data.batting_form == "bunt" or strikes_before < 2:
#             strikes_after += 1
            
#     # --- PitchEvent 作成（投球番号 + カウント保存） ---
#     pitch_number = crud.get_next_pitch_number(db, game_id)
#     pitch_event = crud.create_pitch_event(
#         db=db,
#         game_id=game_id,
#         atbat_id=atbat.id,
#         description=description,
#         pitch_number=pitch_number,
#         balls_before=balls_before,
#         strikes_before=strikes_before,
#         outs_before=outs,
#         balls_after=balls_after,
#         strikes_after=strikes_after,
#         outs_after=outs,
#         runner_first_id=bases[0],
#         runner_second_id=bases[1],
#         runner_third_id=bases[2]
#     )
    
#     # --- 三振or四球 ---
#     if balls_after >= 4:
#         crud.update_atbat_result(db, atbat.id, "walk")
#     elif strikes_after >= 3:
#         crud.update_atbat_result(db, atbat.id, "strikeout")
        
#     # --- 打席終了かどうかを簡易判定 ---
#     requires_confirmation = False
#     end_results = ["walk", "strikeout", "hit"]  # 終了イベント
#     if atbat.result in end_results:
#         requires_confirmation = True
    
#     # --- 打席が確定したら新しく生成 ---
#     if atbat.result != None:
#         batter = get_next_batter(db, game_id, offense_team_id)
#         crud.create_atbat(db, game_id, batter.id, inning, half)

#     #-------------------------------------
#     # othersか否か、3バントか否かで分かれる
#     #-------------------------------------

#     # --- 進塁候補を生成 ---
#     raw_candidates = apply_play_result_and_generate_advances(
#         balls=balls_after,
#         strikes=strikes_after,
#         outs=outs,
#         batter_id=batter_id,
#         bases=bases,
#         bases_str=bases_str,
#         input_data=input_data
#     )

#     # candidate_idを付与
#     candidates = []
#     for idx, pattern in enumerate(raw_candidates):
#         candidates.append({
#             "candidate_id": idx,
#             "advances": pattern
#         })
    
#     # キャッシュに保存
#     CANDIDATE_CACHE[(game_id, pitch_event.id)] = candidates
    
#     # --- レスポンス生成 ---
#     return schema.ScoreInputResponse(
#         atbat_id=atbat.id,
#         pitch_event_id=pitch_event.id,
#         requires_confirmation=requires_confirmation,
#         advance_candidates=[
#             schema.AdvanceCandidate(candidate_id=c["candidate_id"],
#                                     advances=[schema.RunnerAdvance(**adv) for adv in c["advances"]])
#             for c in candidates
#         ],
#     )


# # ------------------------
# # 打席確定時のAdvanceEvent生成
# # ------------------------

# def apply_play_result_and_generate_advances(
#     balls: int,
#     strikes: int,
#     outs: int,
#     batter_id: int,
#     bases: List[int],
#     bases_str: str,
#     input_data: schema.ScoreInputSchema
# ) -> List[List[dict]]:
#     """
#     1球の入力内容から進塁候補を生成（複数パターン返却可）。
#     - まだAdvanceEventは作らない
#     - フロントが候補を選んだら confirm_advances() で確定
#     """
#     description = input_data.description
#     pitch_type_detail = getattr(input_data, "pitch_type_detail", None)
#     position = input_data.position
#     direction = input_data.direction
#     ball_type = input_data.ball_type
#     play_result = input_data.play_result

#     # --- 1) 打球系（inplay） ---
#     if description == "inplay":
#         key = (position, direction, ball_type, play_result)
#         candidates = find_candidates(key, bases_str, outs)

#         all_candidates: List[List[dict]] = []
#         for candidate in candidates:
#             pattern = []
#             for frm, to, reason, safe in candidate:
#                 runner_id = batter_id if frm is None else bases[frm-1]
#                 pattern.append({
#                     "runner_id": runner_id,
#                     "from_base": frm,
#                     "to_base": to,
#                     "is_out": not safe,
#                     "reason": reason
#                 })
#             all_candidates.append(pattern)

#         return all_candidates

#     # --- 2) 特殊系（others） ---
#     elif description == "others":
#         if pitch_type_detail == "hit_by_pitch":
#             # 死球 → 打者1塁＋押し出し
#             advances = []
#             for base in [3, 2, 1]:
#                 runner_id = bases[base-1]
#                 if runner_id:
#                     advances.append({
#                         "runner_id": runner_id,
#                         "from_base": base,
#                         "to_base": base+1,
#                         "is_out": False,
#                         "reason": "押し出し"
#                     })
#             advances.append({
#                 "runner_id": batter_id,
#                 "from_base": 0,
#                 "to_base": 1,
#                 "is_out": False,
#                 "reason": "死球"
#             })
#             return [advances]

#         elif pitch_type_detail == "illegal_pitch":
#             # ボーク扱い → 進塁は1ベースずつ
#             advances = []
#             for base in [3, 2, 1]:
#                 runner_id = bases[base-1]
#                 if runner_id:
#                     advances.append({
#                         "runner_id": runner_id,
#                         "from_base": base,
#                         "to_base": base+1,
#                         "is_out": False,
#                         "reason": "ボーク"
#                     })
#             return [advances]

#         elif pitch_type_detail == "interference":
#             # 守備妨害など → アウト扱い（打者 or 走者）
#             return [[{
#                 "runner_id": batter_id,
#                 "from_base": 0,
#                 "to_base": None,
#                 "is_out": True,
#                 "reason": "打撃妨害"
#             }]]

#         return [[]]

#     # --- 3) 通常球（ボール/ストライク） ---
#     else:
#         # --- 四球判定 ---
#         # 四球による進塁は確定。+alphaの進塁もセットでサジェスト
#         if balls >= 4:
#             advances = []
#             # 押し出し処理（後ろのランナーから順に）
#             for base in [3, 2, 1]:
#                 runner_id = bases[base-1]
#                 if runner_id:
#                     advances.append({
#                         "runner_id": runner_id,
#                         "from_base": base,
#                         "to_base": base+1,
#                         "is_out": False,
#                         "reason": "四球押し出し"
#                     })
#             advances.append({
#                 "runner_id": batter_id,
#                 "from_base": 0,
#                 "to_base": 1,
#                 "is_out": False,
#                 "reason": "四球"
#             })
#             return [advances]

#         # --- 三振判定（振り逃げ考慮） ---
#         if strikes >= 3:
#             # 通常三振
#             advances = []
#             advances.append([{
#                 "runner_id": batter_id,
#                 "from_base": 0,
#                 "to_base": 0,
#                 "is_out": True,
#                 "reason": "三振"
#             }])
            
#             # 1塁空き or 2アウトなら振り逃げ可能
#             if bases[0] is None or outs == 2:
#                 advances.append([{
#                     "runner_id": batter_id,
#                     "from_base": 0,
#                     "to_base": 1,
#                     "is_out": False,
#                     "reason": "振り逃げ"
#                 }])
            
#             return advances

#         # --- まだ進塁なし ---
#         return [[]]


# def confirm_score_input(db: Session, game_id: int, input_data: schema.ConfirmScoreInput):
#     pitch = db.query(models.PitchEvent).filter(
#         models.PitchEvent.id == input_data.pitch_event_id,
#         models.PitchEvent.game_id == game_id
#     ).first()
#     if not pitch:
#         raise HTTPException(status_code=404, detail="Pitch not found")

#     # 一時保存していた進塁候補リストを取得（メモリ or DBに仮保存しておく前提）
#     candidates = CANDIDATE_CACHE.get((game_id, input_data.pitch_event_id), [])
#     selected_candidate = next(
#         (c for c in candidates if c["candidate_id"] == input_data.candidate_id),
#         None
#     )
#     if not selected_candidate:
#         raise HTTPException(status_code=400, detail="Candidate not found")

#     # 実際にAdvanceEventを作成
#     applied_advances = []
#     for adv in selected_candidate["advances"]:
#         new_adv = models.AdvanceEvent(
#             game_id=game_id,
#             pitch_event_id=pitch.id,
#             runner_id=adv["runner_id"],
#             from_base=adv["from_base"],
#             to_base=adv["to_base"],
#             is_out=adv.get("is_out", False),
#         )
#         db.add(new_adv)
#         applied_advances.append(new_adv)

#     db.commit()
#     for adv in applied_advances:
#         db.refresh(adv)

#     return {"success": True, "message": "進塁イベントを登録しました"}















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
            crud.upload_game_member_enrty_number(db, in_member_id)
    
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


def get_following_batter(
    db: Session,
    game_id: int,
    skip: int = 1
) -> models.GameMember:
    """
    次の打者のgame_memberを取得
    """
    game = crud.get_game(db, game_id)
    latest_inning_with_events = crud.get_latest_inning_with_events(db, game_id)
    
    if len(latest_inning_with_events.atbats) == 0:
        last_batting_order = crud.get_last_batting_order_by_inning(db, latest_inning_with_events.id)
    else:
        last_batting_order = crud.get_latest_atbat(db, game_id).batting_order
    
    if latest_inning_with_events.top_bottom == models.TopBottomEnum.top:
        entering_members = get_entering_members(db, game_id)[game.top_team_id]
    else:
        entering_members = get_entering_members(db, game_id)[game.bottom_team_id]
    
    return entering_members[last_batting_order + skip].game_member


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
        if pitch_event.pitch_type in (models.PitchTypeEnum.swing_miss, models.PitchTypeEnum.looking):
            strikes += 1
        if pitch_event.pitch_type == models.PitchTypeEnum.foul and strikes < 2:
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
    batter = latest_atbat.batter
    # ボール、ストライク
    balls, strikes = calc_bs_count(db, game_id)
    # アウト、得点、ランナー(id)
    outs, score, runners_id = aggregate_advance_events(db, game_id)
    runners = []
    for runner_id in runners_id:
        if runner_id > 0:
            runner = crud.get_game_member(db, runner_id)
            runners.append(schema.GameMember.model_validate(runner, from_attributes=True))
        else:
            runners.append(None)
    # 選手の出場状態
    top_team_entry_state, bottom_team_entry_state = get_entry_state(db, game_id)
    # 過去イニングの得点状況
    top_team_score, bottom_team_score = calc_past_inning_score(db, game_id)
    
    return schema.GameStateResponse(
        game = schema.Game.model_validate(game, from_attributes=True),
        top_team_entry_state = schema.TeamEntryState.model_validate(top_team_entry_state, from_attributes=True),
        bottom_team_entry_state = schema.TeamEntryState.model_validate(bottom_team_entry_state, from_attributes=True),
        offense_team = schema.Team.model_validate(offense_team, from_attributes=True),
        defense_team = schema.Team.model_validate(defense_team, from_attributes=True),
        batter = schema.GameMember.model_validate(batter, from_attributes=True),
        balls = balls,
        strikes = strikes,
        outs = outs,
        score = score,
        runners = runners,
        top_team_score = top_team_score,
        bottom_team_score = bottom_team_score
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
    batter = get_following_batter(db, game_id)
    atbat = crud.create_atbat(db, inning.id, batter.id)
    
    return atbat


def suggest_main_advance_events(
    db: Session,
    game_id: int,
    input_data: schema.ScoreInput
):
    """
    想定されるエラーまで含めた進塁イベントをサジェスト
    """
    
    
    
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
    pitch_event = crud.create_pitch_event
    
    balls, strikes = calc_bs_count(db, game_id)
    outs, score, runners_id = aggregate_advance_events(db, game_id)
    
    
    
    



def _is_walk_after_this_pitch(pitch_events: list[models.PitchEvent]) -> bool:
    balls, strikes = calc_bs_count(pitch_events)
    return balls >= 4

def _is_strikeout_after_this_pitch(pitch_events: list[models.PitchEvent]) -> bool:
    balls, strikes = calc_bs_count(pitch_events)
    return strikes >= 3

def _build_forced_walk_advances(
    db: Session,
    game_id: int,
) -> list[schema.AdvanceDetail]:
    """
    現在の走者配置を見て、四球による強制進塁の AdvanceDetail を列挙する。
    - batter: 0 -> 1
    - occupied(1B): 1 -> 2
    - occupied(2B): 2 -> 3
    - occupied(3B): 3 -> 4 (得点)
    """
    advances: list[schema.AdvanceDetail] = []

    latest_atbat = crud.get_latest_atbat(db, game_id)
    batter_id = latest_atbat.batter_id

    # 現在イニングの進塁イベントから盤面を集計（あなたの既存関数）
    advance_events = crud.get_advance_events_of_latest_inning(db, game_id)
    outs, _score, runners = aggregate_advance_events(db, advance_events)  # runners: [0..3]

    # 3塁→本塁、2塁→3塁、1塁→2塁 の順に押し出し
    if runners[3]:
        advances.append(schema.AdvanceDetail(runner_id=runners[3], from_base=3, to_base=4, is_out=False))
    if runners[2]:
        advances.append(schema.AdvanceDetail(runner_id=runners[2], from_base=2, to_base=3, is_out=False))
    if runners[1]:
        advances.append(schema.AdvanceDetail(runner_id=runners[1], from_base=1, to_base=2, is_out=False))

    # 打者 → 一塁
    advances.append(schema.AdvanceDetail(runner_id=batter_id, from_base=0, to_base=1, is_out=False))
    return advances

def _build_strikeout_advance(db: Session, game_id: int) -> list[schema.AdvanceDetail]:
    batter_id = crud.get_latest_atbat(db, game_id).batter_id
    # is_out=True のときは to_base=0 でOK（あなたの検証ロジックと整合）
    return [schema.AdvanceDetail(runner_id=batter_id, from_base=0, to_base=0, is_out=True)]

def register_pitch_event_and_auto_finish(
    db: Session,
    game_id: int,
    input_data: schema.ScoreInput,
) -> schema.GameStateResponse:
    """
    1球登録→四球 or 三振なら AtBat を確定し Advance を記録→3アウトならチェンジ。
    それ以外は何も確定せず次の投球を待つ。
    """
    # 1) 最新打席を取得し PitchEvent を作成
    latest_atbat = crud.get_latest_atbat(db, game_id)
    pitch = crud.create_pitch_event(db, latest_atbat.id, input_data)

    # 2) 現在打席の全PitchEventからカウントを再計算
    pitch_events = crud.get_pitch_events_of_latest_atbat(db, game_id)

    # 3) 四球判定
    if _is_walk_after_this_pitch(pitch_events):
        advances = _build_forced_walk_advances(db, game_id)
        crud.create_advance_event(db, pitch_event_id=pitch.id, advs=advances)
        crud.upload_atbat_result(db, latest_atbat.id, models.AtBatResultEnum.walk)  # ←適宜あなたのEnum名

    # 4) 三振判定（四球と両立しない想定）
    elif _is_strikeout_after_this_pitch(pitch_events):
        advances = _build_strikeout_advance(db, game_id)
        crud.create_advance_event(db, pitch_event_id=pitch.id, advs=advances)
        crud.upload_atbat_result(db, latest_atbat.id, models.AtBatResultEnum.strikeout)

    # 5) 3アウトになっていたらチェンジ
    advance_events_of_latest_inning = crud.get_advance_events_of_latest_inning(db, game_id)
    outs, _score, _runners = aggregate_advance_events(db, advance_events_of_latest_inning)
    if outs >= 3:
        _do_change_inning(db, game_id)

    # 6) 最新状態を返してフロントは次の投球へ
    return get_latest_state(db, game_id)

def _do_change_inning(db: Session, game_id: int) -> None:
    latest_inning = crud.get_latest_inning(db, game_id)

    # 次のイニングを決める
    if latest_inning.top_bottom == models.TopBottomEnum.top:
        # 表→裏
        new_inning = models.Inning(
            game_id=game_id,
            inning_number=latest_inning.inning_number,
            top_bottom=models.TopBottomEnum.bottom,
        )
    else:
        # 裏→次回の表
        new_inning = models.Inning(
            game_id=game_id,
            inning_number=latest_inning.inning_number + 1,
            top_bottom=models.TopBottomEnum.top,
        )

    db.add(new_inning)
    db.commit()
    db.refresh(new_inning)

    # 次の先頭打者（最低限：今は単純に打順を1つ進める。あなたの get_entry_state を使ってもOK）
    game = crud.get_game(db, game_id)
    offense_team_id, _ = get_offense_and_defense_team_id(game, new_inning)
    # ここは暫定：打順管理の正式実装があるなら差し替え
    next_batter_id = get_following_batter(db, game_id).id

    crud.create_atbat(db, inning_id=new_inning.id, batter_id=next_batter_id)
