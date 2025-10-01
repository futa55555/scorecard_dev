# backend/models/league.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import (
    leagues_admin_users_table,
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
    chief_admin_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    # 4. Parent Relationship
    chief_admin_user = relationship("User", foreign_keys=[chief_admin_user_id], back_populates="chief_admin_leagues")

    # 5. Children Relationship
    teams = relationship("Team", back_populates="league")

    # 6. Many-to-many Relationship
    admin_users = relationship("User", secondary=leagues_admin_users_table, back_populates="admin_leagues")
    categories = relationship("Category", secondary=categories_leagues_table, back_populates="leagues")
    tournaments = relationship("Tournament", secondary=leagues_tournaments_table, back_populates="leagues")
