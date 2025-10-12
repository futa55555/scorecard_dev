# backend/schemas/__init__.pyi

from .common import CommonResponse
from .category import CategoryBase, CategorySummary, CategorySummariesResponse
from .league import LeagueBase, LeagueSummary, LeagueSummariesResponse, LeagueListItem, LeagueListResponse, LeagueDetail, LeagueDetailResponse
from .location import LocationBase
from .tournament import TournamentBase
from .user import UserBase
from .team import TeamBase, TeamListItem, TeamListResponse, TeamListWithPage, TeamListWithPageResponse, TeamDetail, TeamDetailResponse
from .person import PersonBase, PersonListItem, PersonListResponse, PersonListWithPage, PersonListWithPageResponse, PersonDetail, PersonDetailResponse
from .person_profile import PersonProfileBase, PersonProfileListItem
from .player_position import PlayerPositionBase, PlayerPositionListItem
from .game import GameBase, GameListItem, GameListResponse, GameDetail, GameDetailResponse

__all__ = [
    "CommonResponse",
    "CategoryBase", "CategorySummary", "CategorySummariesResponse",
    "LeagueBase", "LeagueSummary", "LeagueSummariesResponse", "LeagueListItem", "LeagueListResponse", "LeagueDetail", "LeagueDetailResponse",
    "LocationBase",
    "TournamentBase",
    "UserBase",
    "TeamBase", "TeamListItem", "TeamListResponse", "TeamListWithPage", "TeamListWithPageResponse", "TeamDetail", "TeamDetailResponse",
    "PersonBase", "PersonListItem", "PersonListResponse", "PersonListWithPage", "PersonListWithPageResponse", "PersonDetail", "PersonDetailResponse",
    "PersonProfileBase", "PersonProfileListItem",
    "PlayerPositionBase", "PlayerPositionListItem",
    "GameBase", "GameListItem", "GameListResponse", "GameDetail", "GameDetailResponse"
]
