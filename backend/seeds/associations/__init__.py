# backend/seeds/associations/__init__.py

from .favorite_teams import seed_favorite_teams
from .favorite_people import seed_favorite_people
from .favorite_tournaments import seed_favorite_tournaments
from .leagues_admin_users import seed_leagues_admin_users
from .teams_admin_users import seed_teams_admin_users
from .categories_leagues import seed_categories_leagues
from .categories_teams import seed_categories_teams
from .teams_locations import seed_teams_locations
from .categories_tournaments import seed_categories_tournaments
from .leagues_tournaments import seed_leagues_tournaments
from .teams_tournaments import seed_teams_tournaments
from .locations_tournaments import seed_locations_tournaments

__all__ = [
    "seed_favorite_teams",
    "seed_favorite_people",
    "seed_favorite_tournaments",
    "seed_leagues_admin_users",
    "seed_teams_admin_users",
    "seed_categories_leagues",
    "seed_categories_teams",
    "seed_teams_locations",
    "seed_categories_tournaments",
    "seed_leagues_tournaments",
    "seed_teams_tournaments",
    "seed_locations_tournaments"
]
