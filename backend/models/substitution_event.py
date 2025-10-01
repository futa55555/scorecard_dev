# backend/models/substitution_event.py

from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from backend.database import Base
import enum

class SubstitutionTypeEnum(str, enum.Enum):
    PH = "PH"
    PR = "PR"
    TR = "TR"
    PC = "PC"
    conti = "conti"
    bench = "bench"

class SubstitutionEvent(Base):
    __tablename__ = "substitution_events"

    # 1. Primary Key
    substitution_event_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    substitution_type = Column(Enum(SubstitutionTypeEnum), nullable=False)

    # 3. Foreign Keys
    game_event_id = Column(Integer, ForeignKey("game_events.game_event_id"), nullable=False)
    out_game_member_id = Column(Integer, ForeignKey("game_members.game_member_id"), nullable=True)
    in_game_member_id = Column(Integer, ForeignKey("game_members.game_member_id"), nullable=True)
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    game_event = relationship("GameEvent", foreign_keys=[game_event_id], back_populates="substitution_events")
    out_game_member = relationship("GameMember", foreign_keys=[out_game_member_id], back_populates="substitution_events_as_out_game_member")
    in_game_member = relationship("GameMember", foreign_keys=[in_game_member_id], back_populates="substitution_events_as_in_game_member")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_substitution_events")

    # 5. Children Relationship

    # 6. Many-to-many Relationship
