# backend/models/__init__.py

from .person import Person
from .player_position import PlayerPosition
from .user import User
from .category import Category
from .league import League
from .team import Team
from .organization import Organization
from .location import Location
from tournament import Tournament
from game import Game
from game_record import GameRecord
from game_event import GameEvent
from game_member import GameMember
from advance_event import AdvanceEvent
from pitch_event import PitchEvent
from substitution_event import SubstitutionEvent
from .associations import (
    favorite_teams_table,
    favorite_people_table,
    favorite_tournaments_table,
    organizations_admin_users_table,
    leagues_admin_users_table,
    teams_admin_users_table,
    categories_leagues_table,
    categories_teams_table,
    teams_locations_table,
    categories_tournaments_table,
    leagues_tournaments_table,
    teams_tournaments_table,
    locations_tournaments_table,
    organizations_games_table
)

__all__ = [
    "Person",
    "PlayerPosition",
    "User",
    "Category",
    "League",
    "Team",
    "Organization",
    "Location",
    "Tournament",
    "Game",
    "GameRecord",
    "GameEvent",
    "GameMember",
    "AdvanceEvent",
    "PitchEvent",
    "SubstitutionEvent",
    "favorite_teams_table",
    "favorite_people_table",
    "favorite_tournaments_table",
    "organizations_admin_users_table",
    "leagues_admin_users_table",
    "teams_admin_users_table",
    "categories_leagues_table",
    "categories_teams_table",
    "teams_locations_table",
    "categories_tournaments_table",
    "leagues_tournaments_table",
    "teams_tournaments_table",
    "locations_tournaments_table",
    "organizations_games_table"
]
