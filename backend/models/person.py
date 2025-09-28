# backend/models/person.py

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.models import favorite_people_table

from .enums import PrefectureEnum

class Person(Base):
    __tablename__ = "people"

    # 1. Primary Key
    person_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), default=None)
    prefecture = Column(Enum(PrefectureEnum), nullable=True)
    is_official = Column(Boolean, nullable=False)

    # 3. Foreign Keys
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    created_by_organization_id = Column(Integer, ForeignKey("organizations.organization_id"), nullable=False)

    # 4. Parent Relationship
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_people")
    created_by_organization = relationship("Organization", foreign_keys=[created_by_organization_id], back_populates="created_people")

    # 5. Children Relationship
    player_positions = relationship("PlayerPosition", back_populates="person")
    own_user = relationship("User", back_populates="own_person")
    game_members = relationship("GameMember", back_populates="person")

    # 6. Many-to-many Relationship
    person_profiles = relationship("PersonProfile", back_populates="person")
    teams = relationship("Team", secondary="person_profiles", viewonly=True)
    fans = relationship("User", secondary=favorite_people_table, back_populates="favorite_people")
