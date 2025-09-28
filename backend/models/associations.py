# backend/models/associations.py

from sqlalchemy import Column, ForeignKey, Table, Integer
from backend.database import Base

favorite_teams_table = Table(
    "favorite_teams_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True)
)

favorite_people_table = Table(
    "favorite_people_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("person_id", Integer, ForeignKey("people.person_id"), primary_key=True)
)

favorite_tournaments_table = Table(
    "favorite_tournaments_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
)

organizations_admin_users_table = Table(
    "organizations_admin_users_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("organization_id", Integer, ForeignKey("organizations.organization_id"), primary_key=True)
)

leagues_admin_users_table = Table(
    "leagues_admin_users_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("league_id", Integer, ForeignKey("leagues.league_id"), primary_key=True)
)

teams_admin_users_table = Table(
    "teams_admin_users_table",
    Base.metabase,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True)
)

categories_leagues_table = Table(
    "categories_leagues_table",
    Base.metabase,
    Column("category_id", Integer, ForeignKey("categories.category_id"), primary_key=True),
    Column("league_id", Integer, ForeignKey("leagues.league_id"), primary_key=True)
)

categories_teams_table = Table(
    "categories_teams_table",
    Base.metabase,
    Column("category_id", Integer, ForeignKey("categories.category_id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True)
)

teams_locations_table = Table(
    "teams_locations_table",
    Base.metabase,
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True),
    Column("location_id", Integer, ForeignKey("locations.location_id"), primary_key=True)
)

categories_tournaments_table = Table(
    "categories_tournaments_table",
    Base.metabase,
    Column("category_id", Integer, ForeignKey("categories.category_id"), primary_key=True),
    Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
)

leagues_tournaments_table = Table(
    "leagues_tournaments_table",
    Base.metabase,
    Column("league_id", Integer, ForeignKey("leagues.league_id"), primary_key=True),
    Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
)

teams_tournaments_table = Table(
    "teams_tournaments_table",
    Base.metabase,
    Column("team_id", Integer, ForeignKey("teams.team_id"), primary_key=True),
    Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
)

locations_tournaments_table = Table(
    "locations_tournaments_table",
    Base.metabase,
    Column("location_id", Integer, ForeignKey("locations.location_id"), primary_key=True),
    Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), primary_key=True)
)

organizations_games_table = Table(
    "organizations_games_table",
    Base.metabase,
    Column("organization_id", Integer, ForeignKey("organizations.organization_id"), primary_key=True),
    Column("game_id", Integer, ForeignKey("games.game_id"), primary_key=True)
)
