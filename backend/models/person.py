# backend/models/person.py

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
from .associations import favorite_people_table

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
    created_by_user_id = Column(Integer, ForeignKey("users.user_id", name="fk_created_by_user"), nullable=False)

    # 4. Parent Relationship
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_people")

    # 5. Children Relationship
    person_profiles = relationship("PersonProfile", back_populates="person")
    player_positions = relationship("PlayerPosition", back_populates="person")
    own_user = relationship("User", foreign_keys="User.own_person_id", back_populates="own_person")
    game_members = relationship("GameMember", back_populates="person")

    # 6. Many-to-many Relationship
    fans = relationship("User", secondary=favorite_people_table, back_populates="favorite_people")
