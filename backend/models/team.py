# backend/models/game.py

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
from .associations import (
    favorite_teams_table,
    teams_admin_users_table,
    categories_teams_table,
    teams_locations_table,
    teams_tournaments_table
)
from .enums import PrefectureEnum

class Team(Base):
    __tablename__ = "teams"

    # 1. Primary Key
    team_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)
    short_name = Column(String(100), nullable=False)
    prefecture = Column(Enum(PrefectureEnum), nullable=True)

    # 3. Foreign Keys
    chief_admin_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    league_id = Column(Integer, ForeignKey("leagues.league_id"), nullable=True)

    # 4. Parent Relationship
    chief_admin_user = relationship("User", foreign_keys=[chief_admin_user_id], back_populates="chief_admin_teams")
    league = relationship("League", foreign_keys=[league_id], back_populates="teams")

    # 5. Children Relationship
    games_as_top_team = relationship("Game", foreign_keys="Game.top_team_id", back_populates="top_team")
    games_as_bottom_team = relationship("Game", foreign_keys="Game.bottom_team_id", back_populates="bottom_team")

    # 6. Many-to-many Relationship
    person_profiles = relationship("PersonProfile", back_populates="team")
    people = relationship("Person", secondary="person_profiles", viewonly=True)
    fans = relationship("User", secondary=favorite_teams_table, back_populates="favorite_teams")
    admin_users = relationship("User", secondary=teams_admin_users_table, back_populates="admin_teams")
    categories = relationship("Category", secondary=categories_teams_table, back_populates="teams")
    locations = relationship("Location", secondary=teams_locations_table, back_populates="teams")
    tournaments = relationship("Tournament", secondary=teams_tournaments_table, back_populates="teams")
