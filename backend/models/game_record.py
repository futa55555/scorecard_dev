# backend/models/game_record.py

from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class GameStateEnum(str, enum.Enum):
    draft = "draft"
    ongoing = "ongoing"
    finished = "finished"
    confirmed = "confirmed"

class GameRecord(Base):
    __tablename__ = "game_records"

    # 1. Primary Key
    game_record_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    state = Column(Enum(GameStateEnum), nullable=False)

    # 3. Foreign Keys
    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.organization_id"), nullable=True)

    # 4. Parent Relationship
    game = relationship("Game", foreign_keys=[game_id], back_populates="game_records")
    organization = relationship("Organization", foreign_keys=[organization_id], back_populates="game_records")

    # 5. Children Relationship
    game_events = relationship("GameEvent", back_populates="game_record")
    game_members = relationship("GameMember", back_populates="game_record")

    # 6. Many-to-many Relationship
