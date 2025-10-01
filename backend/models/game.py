# backend/models/game.py

from sqlalchemy import Column, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import relationship
from backend.database import Base

class Game(Base):
    __tablename__ = "games"

    # 1. Primary Key
    game_id = Column(Integer, primary_key=True, index=True)

    # 2. Local Columns
    date = Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    ent_time = Column(Time, nullable=True)

    # 3. Foreign Keys
    top_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    bottom_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.tournament_id"), nullable=False)
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # 4. Parent Relationship
    top_team = relationship("Team", foreign_keys=[top_team_id], back_populates="games_as_top_team")
    bottom_team = relationship("Team", foreign_keys=[bottom_team_id], back_populates="games_as_bottom_team")
    location = relationship("Location", foreign_keys=[location_id], back_populates="games")
    tournament = relationship("Tournament", foreign_keys=[tournament_id], back_populates="games")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id], back_populates="created_games")

    # 5. Children Relationship
    game_records = relationship("GameRecord", back_populates="game")

    # 6. Many-to-many Relationship
