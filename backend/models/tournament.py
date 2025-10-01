# backend/models/tournament.py

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from backend.database import Base
from .associations import (
    favorite_tournaments_table,
    categories_tournaments_table,
    leagues_tournaments_table,
    teams_tournaments_table,
    locations_tournaments_table
)

class Tournament(Base):
    __tablename__ = "tournaments"

    # 1. Primary Key
    tournament_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)
    since_date = Column(Date, nullable=False)
    until_date = Column(Date, nullable=False)
    is_official = Column(Boolean, nullable=False)

    # 3. Foreign Keys
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_tournaments")

    # 5. Children Relationship
    games = relationship("Game", back_populates="tournament")

    # 6. Many-to-many Relationship
    fans = relationship("User", secondary=favorite_tournaments_table, back_populates="favorite_tournaments")
    categories = relationship("Category", secondary=categories_tournaments_table, back_populates="tournaments")
    leagues = relationship("League", secondary=leagues_tournaments_table, back_populates="tournaments")
    teams = relationship("Team", secondary=teams_tournaments_table, back_populates="tournaments")
    locations = relationship("Location", secondary=locations_tournaments_table, back_populates="tournaments")
