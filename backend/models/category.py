# backend/models/category.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from .associations import (
    categories_leagues_table,
    categories_teams_table,
    categories_tournaments_table
)

class Category(Base):
    __tablename__ = "categories"

    # 1. Primary Key
    category_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)

    # 3. Foreign Keys

    # 4. Parent Relationship

    # 5. Children Relationship

    # 6. Many-to-many Relationship
    leagues = relationship("League", secondary=categories_leagues_table, back_populates="categories")
    teams = relationship("Team", secondary=categories_teams_table, back_populates="categories")
    tournaments = relationship("Tournament", secondary=categories_tournaments_table, back_populates="categories")
