# backend/models/pitch_event.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class PitchEvent(Base):
    __tablename__ = "pitch_events"

    # 1. Primary Key
    pitch_event_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns

    # 3. Foreign Keys
    game_event_id = Column(Integer, ForeignKey("game_events.game_event_id"), nullable=False, unique=True)

    # 4. Parent Relationship
    game_event = relationship("GameEvent", foreign_keys=[game_event_id], back_populates="pitch_event")

    # 5. Children Relationship

    # 6. Many-to-many Relationship
