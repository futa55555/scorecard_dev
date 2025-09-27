# backend/models/game_event.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class GameEvent(Base):
    __tablename__ = "game_events"

    # 1. Primary Key
    game_event_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns

    # 3. Foreign Keys
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    game_record_id = Column(Integer, ForeignKey("game_records.game_record_id"), nullable=False)

    # 4. Parent Relationship
    user = relationship("User", foreign_keys=[user_id], back_populates="game_events")
    game_record = relationship("GameRecord", foreign_keys=[game_record_id], back_populates="game_events")

    # 5. Children Relationship
    advance_events = relationship("AdvanceEvent", back_populates="game_event")
    pitch_event = relationship("PitchEvent", back_populates="game_event")
    substitution_events = relationship("SubstitutionEvent", back_populates="game_event")

    # 6. Many-to-many Relationship
