# backend/models/league.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import (
    categories_leagues_table,
    leagues_tournaments_table
)

class League(Base):
    __tablename__ = "leagues"

    # 1. Primary Key
    league_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)

    # 3. Foreign Keys

    # 4. Parent Relationship

    # 5. Children Relationship
    teams = relationship("Team", back_populates="league")

    # 6. Many-to-many Relationship
    categories = relationship("Category", secondary=categories_leagues_table, back_populates="leagues")
    tournaments = relationship("Tournament", secondary=leagues_tournaments_table, back_populates="leagues")
