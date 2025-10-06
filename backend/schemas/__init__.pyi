# backend/schemas/__init__.pyi

from .common import CommonResponse
from .category import CategorySummary, CategorySummaries, CategorySummariesResponse
from .league import LeagueSummary, LeagueSummaries, LeagueSummariesResponse, LeagueDetail, LeagueDetailResponse
from .location import LocationSummary
from .tournament import TournamentSummary
from .user import UserSummary
from .team import TeamSummary, TeamSummaries, TeamSummariesResponse, TeamItem, TeamList, TeamListResponse, TeamDetail, TeamDetailResponse
from .person import PersonSummary, PersonItem, PersonList, PersonListResponse, PersonDetail, PersonDetailResponse
from .game import GameItem, GameList, GameListResponse, GameDetail, GameDetailResponse

__all__ = [
    "CommonResponse",
    "CategorySummary", "CategorySummaries", "CategorySummariesResponse",
    "LeagueSummary", "LeagueSummaries", "LeagueSummariesResponse", "LeagueDetail", "LeagueDetailResponse",
    "LocationSummary",
    "TournamentSummary",
    "UserSummary",
    "TeamSummary", "TeamSummaries", "TeamSummariesResponse", "TeamItem", "TeamList", "TeamListResponse", "TeamListResponse", "TeamDetail", "TeamDetailResponse",
    "PersonSummary", "PersonItem", "PersonList", "PersonListResponse", "PersonDetail", "PersonDetailResponse",
    "GameItem", "GameList", "GameListResponse", "GameDetail", "GameDetailResponse"
]
