# backend/models/player_position.py

from sqlalchemy import Column, ForeignKey, Integer, Boolean, Date, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class PositionTypeEnum(str, enum.Enum):
    P = "P"
    C = "C"
    IF = "IF"
    OF = "OF"

class PlayerPosition(Base):
    __tablename__ = "player_positions"

    # 1. Primary Key
    player_position_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    position_type = Column(Enum(PositionTypeEnum), nullable=False)
    since_date = Column(Date, nullable=False)
    until_date = Column(Date, nullable=True)
    is_official = Column(Boolean, nullable=True)

    # 3. Foreign Keys
    person_id = Column(Integer, ForeignKey("people.person_id"), nullable=False)
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    person = relationship("Person", foreign_keys=[person_id], back_populates="player_positions")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_player_positions")

    # 5. Children Relationship

    # 6. Many-to-many Relationship
