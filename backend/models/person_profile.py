# backend/models/person_profile.py

from sqlalchemy import Column, ForeignKey, Integer, Date, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class RoleEnum(str, enum.Enum):
    player = "player"
    head_coach = "head_coach"
    coach = "coach"
    manager = "manager"
    trainer = "trainer"
    analyst = "analyst"

class PersonProfile(Base):
    __tablename__ = "person_profiles"

    # 1. Primary Key
    person_profile_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    uniform_number = Column(Integer, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    since_date = Column(Date, nullable=False)
    until_date = Column(Date, nullable=True)

    # 3. Foreign Keys
    person_id = Column(Integer, ForeignKey("people.person_id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)

    # 4. Parent Relationship
    person = relationship("Person", foreign_keys=[person_id], back_populates="person_profiles")
    team = relationship("Team", foreign_keys=[team_id], back_populates="person_profiles")

    # 5. Children Relationship

    # 6. Many-to-many Relationship
