# backend/models/advance_event.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class AdvanceEvent(Base):
    __tablename__ = "advance_events"

    # 1. Primary Key
    advance_event_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns

    # 3. Foreign Keys
    game_event_id = Column(Integer, ForeignKey("game_events.game_event_id"), nullable=False)

    # 4. Parent Relationship
    game_event = relationship("GameEvent", foreign_keys=[game_event_id], back_populates="advance_events")

    # 5. Children Relationship

    # 6. Many-to-many Relationship
