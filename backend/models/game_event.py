# backend/models/game_event.py

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from backend.database import Base

class GameEvent(Base):
    __tablename__ = "game_events"

    # 1. Primary Key
    game_event_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns

    # 3. Foreign Keys
    game_record_id = Column(Integer, ForeignKey("game_records.game_record_id"), nullable=False)
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    game_record = relationship("GameRecord", foreign_keys=[game_record_id], back_populates="game_events")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_game_events")

    # 5. Children Relationship
    advance_events = relationship("AdvanceEvent", back_populates="game_event")
    pitch_event = relationship("PitchEvent", back_populates="game_event")
    substitution_events = relationship("SubstitutionEvent", back_populates="game_event")

    # 6. Many-to-many Relationship
