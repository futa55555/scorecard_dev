# backend/models/location.py

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import (
    teams_locations_table,
    locations_tournaments_table
)
from .enums import PrefectureEnum

class Location(Base):
    __tablename__ = "locations"

    # 1. Primary Key
    location_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)
    prefecture = Column(Enum(PrefectureEnum), nullable=False)

    # 3. Foreign Keys

    # 4. Parent Relationship

    # 5. Children Relationship
    games = relationship("Game", back_populates="location")

    # 6. Many-to-many Relationship
    teams = relationship("Team", secondary=teams_locations_table, back_populates="locations")
    tournaments = relationship("Tournament", secondary=locations_tournaments_table, back_populates="locations")
