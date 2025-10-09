# backend/cruds/__init__.pyi

from .categories import get_category_summaries
from .leagues import get_league_summaries, get_league_list, get_league_detail
from .teams import get_team_list, get_team_detail
from .people import get_person_list, get_person_detail
from .games import get_game_list, get_game_detail

__all__ = [
    "get_category_summaries",
    "get_league_summaries", "get_league_list", "get_league_detail",
    "get_team_list", "get_team_detail",
    "get_person_list", "get_person_detail",
    "get_game_list", "get_game_detail"
]
