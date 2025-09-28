# backend/models/user.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import (
    favorite_teams_table,
    favorite_people_table,
    favorite_tournaments_table,
    organizations_admin_users_table,
    leagues_admin_users_table,
    teams_admin_users_table
)

class User(Base):
    __tablename__ = "users"

    # 1. Primary Key
    user_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    # 3. Foreign Keys
    own_person_id = Column(Integer, ForeignKey("people.person_id"), nullable=True, unique=True)

    # 4. Parent Relationship
    own_person = relationship("Person", foreign_keys=[own_person_id], back_populates="own_user")

    # 5. Children Relationship
    chief_admin_leagues = relationship("League", back_populates="chief_admin_user")
    chief_admin_teams = relationship("Team", back_populates="chief_admin_user")
    chief_admin_organizations = relationship("Organization", back_populates="chief_admin_user")
    created_people = relationship("Person", back_populates="created_by_user")
    created_person_profiles = relationship("PersonProfile", back_populates="created_by_user")
    game_events = relationship("GameEvent", back_populates="user")

    # 6. Many-to-many Relationship
    favorite_teams = relationship("Team", secondary=favorite_teams_table, back_populates="fans")
    favorite_people = relationship("Person", secondary=favorite_people_table, back_populates="fans")
    favorite_tournaments = relationship("Tournament", secondary=favorite_tournaments_table, back_populates="fans")
    admin_organizations = relationship("Organization", secondary=organizations_admin_users_table, back_populates="admin_users")
    admin_leagues = relationship("League", secondary=leagues_admin_users_table, back_populates="admin_users")
    admin_teams = relationship("Team", secondary=teams_admin_users_table, back_populates="admin_users")
