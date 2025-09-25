# backend/seeds/__init__.py

from backend.seeds.users import seed_users
from backend.seeds.categories import seed_categories
from backend.seeds.leagues import seed_leagues
from backend.seeds.teams import seed_teams
from backend.seeds.people import seed_people
from backend.seeds.person_profiles import seed_person_profiles
from backend.seeds.tournaments import seed_tournaments
from backend.seeds.games import seed_games
from backend.seeds.game_records import seed_game_records
from backend.seeds.game_members import seed_game_members

from backend.seeds.user_favorite_teams import seed_user_favorite_teams
from backend.seeds.tournament_teams import seed_tournament_teams
from backend.seeds.tournament_categories import seed_tournament_categories


def init_data(db):

    seed_users(db)
    seed_categories(db)
    seed_leagues(db)
    seed_teams(db)
    seed_people(db)
    seed_person_profiles(db)
    seed_tournaments(db)
    seed_games(db)
    seed_game_records(db)
    seed_game_members(db)

    seed_user_favorite_teams(db)
    seed_tournament_teams(db)
    seed_tournament_categories(db)
