# backend/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Boolean, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON, Time
from backend.database import Base
import enum

# --------------------
# Enum 定義
# --------------------

class PrefectureEnum(str, enum.Enum):
    Hokkaido = "北海道"
    Aomori = "青森"
    Iwate = "岩手"
    Akita = "秋田"
    Miyagi = "宮城"
    Yamagata = "山形"
    Fukushima = "福島"
    Ibaraki = "茨城"
    Tochigi = "栃木"
    Gunma = "群馬"
    Saitama = "埼玉"
    Chiba = "千葉"
    Tokyo = "東京"
    Kanagawa = "神奈川"
    Niigata = "新潟"
    Nagano = "長野"
    Yamanashi = "山梨"
    Shizuoka = "静岡"
    Gifu = "岐阜"
    Aichi = "愛知"
    Toyama = "富山"
    Ishikawa = "石川"
    Fukui = "福井"
    Shiga = "滋賀"
    Mie = "三重"
    Nara = "奈良"
    Wakayama = "和歌山"
    Kyoto = "京都"
    Osaka = "大阪"
    Hyogo = "兵庫"
    Kagawa = "香川"
    Tokushima = "徳島"
    Ehime = "愛媛"
    Kochi = "高知"
    Okayama = "岡山"
    Hiroshima = "広島"
    Tottori = "鳥取"
    Shimane = "島根"
    Yamaguchi = "山口"
    Fukuoka = "福岡"
    Saga = "佐賀"
    Nagasaki = "長崎"
    Oita = "大分"
    Kumamoto = "熊本"
    Miyazaki = "宮崎"
    Kagoshima = "鹿児島"
    Okinawa = "沖縄"
    
class GradeEnum(str, enum.Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    B4 = "B4"
    M1 = "M1"
    M2 = "M2"
    
class DominantHandEnum(str, enum.Enum):
    right = "R"
    left = "L"
    switch = "S"

class RoleEnum(str, enum.Enum):
    player = "player"
    coach = "coach"
    manager = "manager"
    trainer = "trainer"
    analyst = "analyst"

class PositionTypeEnum(str, enum.Enum):
    P = "P"
    C = "C"
    IF = "IF"
    OF = "OF"

class PositionEnum(int, enum.Enum):
    P = 1
    C = 2
    FB = 3
    SB = 4
    TB = 5
    SS = 6
    LF = 7
    CF = 8
    RF = 9
    DP = 10
    NOT = 0

class BattingOrderEnum(int, enum.Enum):
    No1 = 1
    No2 = 2
    No3 = 3
    No4 = 4
    No5 = 5
    No6 = 6
    No7 = 7
    No8 = 8
    No9 = 9
    FP = 10
    NOT = 0

class TopBottomEnum(str, enum.Enum):
    top = "top"
    bottom = "bottom"

class BattingFormEnum(str, enum.Enum):
    hitting = "hitting"  # 通常打撃
    bunt = "bunt"        # バント
    slap = "slap"        # スラップ

class BattingSideEnum(str, enum.Enum):
    R = "R"  # 右打席
    L = "L"  # 左打席
    S = "S"  # スイッチ

class PitchTypeEnum(str, enum.Enum):
    swing_miss = "swing_miss"
    looking = "looking"
    ball = "ball"
    foul = "foul"
    inplay = "inplay"
    others = "others"

class PitchTypeDetailEnum(str, enum.Enum):
    hit_by_pitch = "hit_by_pitch"
    illegal = "illegal"
    interfere = "interfere"
    leaving_base = "leaving_base"

class AtBatResultEnum(str, enum.Enum):
    strikeout = "strikeout"
    walk = "walk"
    hit = "hit"
    poor = "poor"
    sacrified = "sacrified"
    hit_by_pitch = "hit_by_pitch"
    illegal = "illegal"
    interfere = "interfere"

class BattedBallDirectionEnum(str, enum.Enum):
    center = "center"
    front = "front"
    back = "back"
    left = "left"
    right = "right"
    
class BattedBallTypeEnum(str, enum.Enum):
    none = "none"
    ground = "ground"
    fly = "fly"
    liner = "liner"

class OutTypeEnum(str, enum.Enum):
    force = "force"
    touch = "touch"

class AdvanceByPitchEnum(str, enum.Enum):
    steal = "steal"
    wild_pitch = "wild_pitch"
    passed_ball = "passed_ball"

# --------------------
# テーブル定義
# --------------------

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    short_name = Column(String(100), nullable=True) # 略称
    is_myteam = Column(Boolean, default=False)
    prefecture = Column(Enum(PrefectureEnum), nullable=True)
    league = Column(String(100), nullable=True) # 所属リーグ
    photo_url = Column(URLType, nullable=True) # 画像
    color = Column(String(100), nullable=True) # テーマカラー
    
    member_profiles = relationship("MemberProfile", back_populates="team")
    games_as_top_team = relationship("Game", foreign_keys="Game.top_team_id", back_populates="top_team")
    games_as_bottom_team = relationship("Game", foreign_keys="Game.bottom_team_id", back_populates="bottom_team")
    game_members = relationship("GameMember", back_populates="team")
    substitutions = relationship("SubstitutionEvent", back_populates="team")
    

class Person(Base):
    __tablename__ = "people"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    pitching_side = Column(Enum(DominantHandEnum), nullable=True)
    batting_side = Column(Enum(DominantHandEnum), nullable=True)
    photo_url = Column(URLType, nullable=True)
    height_cm = Column(Integer, nullable=True)
    weight_kg = Column(Integer, nullable=True)
    birthday = Column(Date, nullable=True)

    member_profiles = relationship("MemberProfile", back_populates="person")
    member_grades = relationship("MemberGrade", back_populates="person")
    player_position_types = relationship("PlayerPositionType", back_populates="person")

    
class MemberProfile(Base):
    __tablename__ = "member_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    since_date = Column(Date, nullable=True)
    until_date = Column(Date, nullable=True)
    uniform_number = Column(Integer, nullable=True)
    role = Column(Enum(RoleEnum), nullable=True)
    
    team = relationship("Team", foreign_keys=[team_id], back_populates="member_profiles")
    person = relationship("Person", foreign_keys=[person_id], back_populates="member_profiles")
    game_members = relationship("GameMember", back_populates="member_profile")
    

class MemberGrade(Base):
    __tablename__ = "member_grades"
    
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    grade = Column(Enum(GradeEnum), nullable=True)
    since_date = Column(Date, nullable=True)
    until_date = Column(Date, nullable=True)
    
    person = relationship("Person", foreign_keys=[person_id], back_populates="member_grades")
    

class PlayerPositionType(Base):
    __tablename__ = "player_position_types"
    
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    position_type = Column(Enum(PositionTypeEnum), nullable=False)
    since_date = Column(Date, nullable=True)
    until_date = Column(Date, nullable=True)
    
    person = relationship("Person", foreign_keys=[person_id], back_populates="player_position_types")
    

class GameMember(Base):
    __tablename__ = "game_members"
    
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    member_profile_id = Column(Integer, ForeignKey("member_profiles.id"), nullable=False)
    starting_batting_order = Column(Enum(BattingOrderEnum), nullable=True)
    starting_position = Column(Enum(PositionEnum), nullable=True)
    entry_number = Column(Integer, default=0)
    
    member_profile = relationship("MemberProfile", foreign_keys=[member_profile_id], back_populates="game_members")
    game = relationship("Game", foreign_keys=[game_id], back_populates="game_members")
    team = relationship("Team", foreign_keys=[team_id], back_populates="game_members")
    atbats = relationship("AtBat", back_populates="batter")
    runners = relationship("AdvanceEvent", foreign_keys="AdvanceEvent.runner_id", back_populates="runner")
    sub_out_events = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.out_member_id", back_populates="out_member")
    sub_in_events = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.in_member_id", back_populates="in_member")
    

class SubstitutionEvent(Base):
    __tablename__ = "substitution_events"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    pitch_event_id = Column(Integer, ForeignKey("pitch_events.id"), nullable=True) # 交代のタイミング
    out_member_id = Column(Integer, ForeignKey("game_members.id"), nullable=True)  # 交代で出る選手
    in_member_id = Column(Integer, ForeignKey("game_members.id"), nullable=False)  # 入る選手
    is_position_change = Column(Boolean, nullable=False)
    is_tmp = Column(Boolean, default=False)

    game = relationship("Game", back_populates="substitutions")
    team = relationship("Team", back_populates="substitutions")
    pitch_event = relationship("PitchEvent", back_populates="substitutions")
    out_member = relationship("GameMember", foreign_keys=[out_member_id], back_populates="sub_out_events")
    in_member = relationship("GameMember", foreign_keys=[in_member_id], back_populates="sub_in_events")
    

class Game(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    top_team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    bottom_team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    date = Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    location = Column(String(100), nullable=True)
    
    top_team = relationship("Team", foreign_keys=[top_team_id], back_populates="games_as_top_team")
    bottom_team = relationship("Team", foreign_keys=[bottom_team_id], back_populates="games_as_bottom_team")
    game_members = relationship("GameMember", back_populates="game")
    substitutions = relationship("SubstitutionEvent", back_populates="game")
    innings = relationship("Inning", back_populates="game")


class Inning(Base):
    __tablename__ = "innings"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    inning_number = Column(Integer, nullable=False)
    top_bottom = Column(Enum(TopBottomEnum), nullable=False)
    score = Column(Integer, default=-1)  # -1はnot finished. 得点を代入してfinished.
    
    game = relationship("Game", back_populates="innings")
    atbats = relationship("AtBat", back_populates="inning")
    

class AtBat(Base):
    __tablename__ = "atbats"

    id = Column(Integer, primary_key=True, index=True)
    inning_id = Column(Integer, ForeignKey("innings.id"), nullable=False)
    batter_id = Column(Integer, ForeignKey("game_members.id"), nullable=True)
    # result = Column(Enum(AtBatResultEnum), nullable=True)
    result = Column(String(50), nullable=True)

    inning = relationship("Inning", foreign_keys=[inning_id], back_populates="atbats")
    batter = relationship("GameMember", back_populates="atbats")
    pitch_events = relationship("PitchEvent", back_populates="atbat")


class PitchEvent(Base):
    __tablename__ = "pitch_events"

    id = Column(Integer, primary_key=True, index=True)
    atbat_id = Column(Integer, ForeignKey("atbats.id"), nullable=False)
    pitch_type = Column(Enum(PitchTypeEnum), nullable=False)
    pitch_type_detail = Column(String(50), nullable=True)
    batting_form = Column(Enum(BattingFormEnum), nullable=True)
    batting_side = Column(Enum(BattingSideEnum), nullable=True)
    is_runner_first_steal = Column(Boolean, default=False)
    is_runner_second_steal = Column(Boolean, default=False)
    is_runner_third_steal = Column(Boolean, default=False)
    
    atbat = relationship("AtBat", foreign_keys=[atbat_id], back_populates="pitch_events")
    advance_events = relationship("AdvanceEvent", back_populates="pitch_event")
    substitutions = relationship("SubstitutionEvent", back_populates="pitch_event")
    

class AdvanceEvent(Base):
    __tablename__ = "advance_events"

    id = Column(Integer, primary_key=True, index=True)
    pitch_event_id = Column(Integer, ForeignKey("pitch_events.id"), nullable=False)
    runner_id = Column(Integer, ForeignKey("game_members.id"), nullable=False)
    from_base = Column(Integer, nullable=False)
    to_base = Column(Integer, nullable=False)
    is_out = Column(Boolean, nullable=False)
    is_by_atbat = Column(Boolean, nullable=False)
    out_type = Column(Enum(OutTypeEnum), nullable=True)
    ball_flow = Column(JSON, nullable=True)
    advance_by_pitch = Column(Enum(AdvanceByPitchEnum), nullable=True)

    pitch_event = relationship("PitchEvent", foreign_keys=[pitch_event_id], back_populates="advance_events")
    runner = relationship("GameMember", foreign_keys=[runner_id], back_populates="runners")
