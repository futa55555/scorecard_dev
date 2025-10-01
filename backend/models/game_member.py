# backend/models/game_member.py

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from backend.database import Base

class GameMember(Base):
    __tablename__ = "game_members"

    # 1. Primary Key
    game_member_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    role = Column(Integer, nullable=False)

    # 3. Foreign Keys
    person_id = Column(Integer, ForeignKey("people.person_id"), nullable=False)
    game_record_id = Column(Integer, ForeignKey("game_records.game_record_id"), nullable=False)
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    person = relationship("Person", foreign_keys=[person_id], back_populates="game_members")
    game_record = relationship("GameRecord", foreign_keys=[game_record_id], back_populates="game_members")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_game_members")

    # 5. Children Relationship
    substitution_events_as_out_game_member = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.out_game_member_id", back_populates="out_game_member")
    substitution_events_as_in_game_member = relationship("SubstitutionEvent", foreign_keys="SubstitutionEvent.in_game_member_id", back_populates="in_game_member")

    # 6. Many-to-many Relationship
