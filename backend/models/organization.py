# backend/models/organization.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import (
    organizations_admin_users_table,
    organizations_games_table
)

class Organization(Base):
    __tablename__ = "organizations"

    # 1. Primary Key
    organization_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)

    # 3. Foreign Keys
    chief_admin_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    chief_admin_user = relationship("User", foreign_keys=[chief_admin_user_id], back_populates="chief_admin_organizations")

    # 5. Children Relationship
    created_people = relationship("Person", back_populates="created_by_organization")
    created_person_profiles = relationship("PersonProfile", back_populates="created_by_organization")
    tournaments = relationship("Tournament", back_populates="organization")
    game_records = relationship("GameRecord", back_populates="organization")

    # 6. Many-to-many Relationship
    admin_users = relationship("User", secondary=organizations_admin_users_table, back_populates="admin_organizations")
    games = relationship("Game", secondary=organizations_games_table, back_populates="organizations")
