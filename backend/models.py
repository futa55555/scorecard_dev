# backend/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Table, Boolean
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


class TopBottomEnum(str, enum.Enum):
    top = "top"
    bottom = "bottom"


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
    NOT = "NOT"


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


class SubstitutionTypeEnum(str, enum.Enum):
    PH = "PH"
    PR = "PR"
    TR = "TR"
    PC = "PC"
    conti = "conti"
    bench = "bench"


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


class ResponsibilityTypeEnum(str, enum.Enum):
    win = "win"
    lose = "lose"
    hold = "hold"
    save = "save"


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
    none = "none"
    safe = "safe"
    force = "force"
    touch = "touch"


class AdvanceByPitchEnum(str, enum.Enum):
    steal = "steal"
    wild_pitch = "wild_pitch"
    passed_ball = "passed_ball"


class GameStatusEnum(str, enum.Enum):
    draft = "draft"
    ongoing = "ongoing"
    finished = "finished"
    confirmed = "confirmed"


# --------------------
# テーブル定義（本体テーブル）
# --------------------

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    birthday = Column(Date, nullable=True)

    admin_teams = relationship("Team", back_populates="admin")

    favorite_team_links = relationship("UserFavoriteTeam", back_populates="user")
    favorite_teams = relationship("Team", secondary="user_favorite_teams", viewonly=True)


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    teams = relationship("Team", back_populates="category")

    leagues = relationship("League", back_populates="category")

    tournament_links = relationship("TournamentCategory", back_populates="category")
    tournaments = relationship("Tournament", secondary="tournament_categories", viewonly=True)


class League(Base):
    __tablename__ = "leagues"

    league_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    name = Column(String(100), nullable=False)

    category = relationship("Category", foreign_keys=[category_id], back_populates="leagues")
    teams = relationship("Team", back_populates="league")


class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    short_name = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
    league_id = Column(Integer, ForeignKey("leagues.league_id"), nullable=True)
    prefecture = Column(Enum(PrefectureEnum), nullable=True)
    photo_url = Column(URLType, nullable=True)
    color = Column(String(100), nullable=True)
    admin_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    games_as_top_team = relationship("Game", foreign_keys="Game.top_team_id", back_populates="top_team")
    games_as_bottom_team = relationship("Game", foreign_keys="Game.bottom_team_id", back_populates="bottom_team")

    person_profiles = relationship("PersonProfile", back_populates="team")
    game_members = relationship("GameMember", back_populates="team")
    category = relationship("Category", back_populates="teams")
    league = relationship("League", back_populates="teams")
    admin = relationship("User", back_populates="admin_teams")

    favorited_by_links = relationship("UserFavoriteTeam", back_populates="team")
    favorited_by = relationship("User", secondary="user_favorite_teams", viewonly=True)

    tournament_links = relationship("TournamentTeam", back_populates="team")
    tournaments = relationship("Tournament", secondary="tournament_teams", viewonly=True)


class Person(Base):
    __tablename__ = "people"

    person_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    pitching_side = Column(Enum(DominantHandEnum), nullable=True)
    batting_side = Column(Enum(DominantHandEnum), nullable=True)
    photo_url = Column(URLType, nullable=True)
    height_cm = Column(Integer, nullable=True)
    weight_kg = Column(Integer, nullable=True)
    birthday = Column(Date, nullable=True)
    prefecture = Column(Enum(PrefectureEnum), nullable=True)

    person_profiles = relationship("PersonProfile", back_populates="person")
    game_members = relationship("GameMember", back_populates="person")


class PersonProfile(Base):
    __tablename__ = "person_profiles"

    person_profile_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("people.person_id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    since_date = Column(Date, nullable=True)
    until_date = Column(Date, nullable=True)
    uniform_number = Column(Integer, nullable=True)
    role = Column(Enum(RoleEnum), nullable=True)

    team = relationship("Team", foreign_keys=[team_id], back_populates="person_profiles")
    person = relationship("Person", foreign_keys=[person_id], back_populates="person_profiles")


class Tournament(Base):
    __tablename__ = "tournaments"

    tournament_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    since_date = Column(Date, nullable=True)
    until_date = Column(Date, nullable=True)

    games = relationship("Game", back_populates="tournament")

    team_links = relationship("TournamentTeam", back_populates="tournament")
    teams = relationship("Team", secondary="tournament_teams", viewonly=True)

    category_links = relationship("TournamentCategory", back_populates="tournament")
    categories = relationship("Category", secondary="tournament_categories", viewonly=True)


class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True)
    top_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=True)
    bottom_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=True)
    top_bottom_decided = Column(Boolean, default=False, nullable=False)
    date = Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.tournament_id"), nullable=True)
    location = Column(String(100), nullable=True)
    status = Column(Enum(GameStatusEnum), nullable=False)

    top_team = relationship("Team", foreign_keys=[top_team_id], back_populates="games_as_top_team")
    bottom_team = relationship("Team", foreign_keys=[bottom_team_id], back_populates="games_as_bottom_team")
    tournament = relationship("Tournament", foreign_keys=[tournament_id], back_populates="games")
    game_members = relationship("GameMember", back_populates="game")


class GameMember(Base):
    __tablename__ = "game_members"

    game_member_id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    person_id = Column(Integer, ForeignKey("people.person_id"), nullable=False)
    starting_batting_order = Column(Enum(BattingOrderEnum), nullable=True)
    starting_position = Column(Enum(PositionEnum), nullable=True)

    person = relationship("Person", foreign_keys=[person_id], back_populates="game_members")
    game = relationship("Game", foreign_keys=[game_id], back_populates="game_members")
    team = relationship("Team", foreign_keys=[team_id], back_populates="game_members")
    advance_events = relationship("AdvanceEvent", foreign_keys="AdvanceEvent.runner_id", back_populates="runner")
    substitution_events_as_out = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.out_member_id", back_populates="out_member")
    substitution_events_as_in = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.in_member_id", back_populates="in_member")


class SubstitutionEvent(Base):
    __tablename__ = "substitution_events"

    substitution_event_id = Column(Integer, primary_key=True)
    pitch_event_id = Column(Integer, ForeignKey("pitch_events.pitch_event_id"), nullable=False)
    out_member_id = Column(Integer, ForeignKey("game_members.game_member_id"), nullable=False)
    in_member_id = Column(Integer, ForeignKey("game_members.game_member_id"), nullable=False)
    substitution_type = Column(Enum(SubstitutionTypeEnum), nullable=False)

    pitch_event = relationship("PitchEvent", back_populates="substitution_events")
    out_member = relationship("GameMember", foreign_keys=[out_member_id], back_populates="substitution_events_as_out")
    in_member = relationship("GameMember", foreign_keys=[in_member_id], back_populates="substitution_events_as_in")


class PitchEvent(Base):
    __tablename__ = "pitch_events"

    pitch_event_id = Column(Integer, primary_key=True, index=True)
    pitch_type = Column(Enum(PitchTypeEnum), nullable=False)
    pitch_type_detail = Column(String(50), nullable=True)
    batting_form = Column(Enum(BattingFormEnum), nullable=True)
    batting_side = Column(Enum(BattingSideEnum), nullable=True)

    advance_events = relationship("AdvanceEvent", back_populates="pitch_event")
    substitution_events = relationship("SubstitutionEvent", back_populates="pitch_event")


class AdvanceEvent(Base):
    __tablename__ = "advance_events"

    advance_event_id = Column(Integer, primary_key=True, index=True)
    pitch_event_id = Column(Integer, ForeignKey("pitch_events.pitch_event_id"), nullable=False)
    runner_id = Column(Integer, ForeignKey("game_members.game_member_id"), nullable=False)
    to_base = Column(Integer, nullable=False)
    out_type = Column(Enum(OutTypeEnum), nullable=True)
    parent_advance_event_id = Column(Integer, nullable=True)
    fielding_sequence = Column(JSON, nullable=True)

    pitch_event = relationship("PitchEvent", foreign_keys=[pitch_event_id], back_populates="advance_events")
    runner = relationship("GameMember", foreign_keys=[runner_id], back_populates="advance_events")


# --------------------
# テーブル定義（中間テーブル）
# --------------------

class UserFavoriteTeam(Base):
    __tablename__ = "user_favorite_teams"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"), primary_key=True)

    user = relationship("User", back_populates="favorite_team_links")
    team = relationship("Team", back_populates="favorited_by_links")


class TournamentTeam(Base):
    __tablename__ = "tournament_teams"

    tournament_id = Column(Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"), primary_key=True)

    tournament = relationship("Tournament", back_populates="team_links")
    team = relationship("Team", back_populates="tournament_links")


class TournamentCategory(Base):
    __tablename__ = "tournament_categories"

    tournament_id = Column(Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), primary_key=True)

    tournament = relationship("Tournament", back_populates="category_links")
    category = relationship("Category", back_populates="tournament_links")
