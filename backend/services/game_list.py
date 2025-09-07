# backend/services/game_list.py

from sqlalchemy.orm import Session
from typing import List
from backend.schemas import game_list as schema
from backend.cruds import game_list as crud

def get_game_with_team_name_list(
    db: Session
) -> List[schema.GameWithTeamName]:
    """
    チーム名付きで試合のリストを取得
    """
    game_list = crud.get_game_list(db)
    
    res = []
    for game in game_list:
        res.append(
            schema.GameWithTeamName(
                id = game.id,
                top_team_short_name = game.top_team.short_name,
                bottom_team_short_name = game.bottom_team.short_name,
                date = game.date,
                start_time = game.start_time,
                end_time = game.end_time,
                tournament = game.tournament,
                location = game.location,
                status = game.status
            )
        )
        
    return res