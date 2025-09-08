# backend/seeds/__init__.py

from backend.seeds.teams import seed_teams
from backend.seeds.people import seed_people
from backend.seeds.member_profiles import seed_member_profiles
from backend.seeds.member_grades import seed_member_grades
from backend.seeds.player_position_types import seed_player_position_types
from backend.seeds.games import seed_games
from backend.seeds.game_members import seed_game_members

def init_data(db):
    seed_teams(db)
    seed_people(db)
    seed_member_profiles(db)
    seed_member_grades(db)
    seed_player_position_types(db)
    seed_games(db)
    seed_game_members(db)
