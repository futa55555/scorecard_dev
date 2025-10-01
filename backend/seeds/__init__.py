# backend/seeds/__init__.py

from .users import seed_users
from .categories import seed_categories
from .leagues import seed_leagues
from .teams import seed_teams
from .people import seed_people
from .person_profiles import seed_person_profiles
from .player_positions import seed_player_positions
from .locations import seed_locations
from .tournaments import seed_tournaments
from .games import seed_games
from .game_records import seed_game_records
from .game_events import seed_game_events
from .game_members import seed_game_members
from .advance_events import seed_advance_events
from .pitch_events import seed_pitch_events
from .substitution_events import seed_substitution_events

from .associations import (
    seed_favorite_teams,
    seed_favorite_people,
    seed_favorite_tournaments,
    seed_leagues_admin_users,
    seed_teams_admin_users,
    seed_categories_leagues,
    seed_categories_teams,
    seed_teams_locations,
    seed_categories_tournaments,
    seed_leagues_tournaments,
    seed_teams_tournaments,
    seed_locations_tournaments
)


def init_data(db):

    seed_users(db)
    seed_categories(db)
    seed_leagues(db)
    seed_teams(db)
    seed_people(db)
    seed_person_profiles(db)
    seed_player_positions(db)
    seed_locations(db)
    seed_tournaments(db)
    seed_games(db)
    seed_game_records(db)
    seed_game_events(db)
    seed_game_members(db)
    seed_advance_events(db)
    seed_pitch_events(db)
    seed_substitution_events(db)

    seed_favorite_teams(db)
    seed_favorite_people(db)
    seed_favorite_tournaments(db)
    seed_leagues_admin_users(db)
    seed_teams_admin_users(db)
    seed_categories_leagues(db)
    seed_categories_teams(db)
    seed_teams_locations(db)
    seed_categories_tournaments(db)
    seed_leagues_tournaments(db)
    seed_teams_tournaments(db)
    seed_locations_tournaments(db)
