# backend/services/team_list.py

from sqlalchemy.orm import Session
from typing import List
from backend.schemas import team_list as schema
from backend.cruds import team_list as crud

def get_team_list(
    db: Session
) -> List[schema.TeamBase]:
    team_list = crud.get_team_list(db)
    
    res = []
    for team in team_list:
        res.append(
            schema.TeamBase(
                id = team.id,
                name = team.name,
                short_name = team.short_name,
                is_myteam = team.is_myteam,
                is_favorite = team.is_favorite,
                prefecture = team.prefecture,
                league = team.league,
                photo_url = team.photo_url,
                color = team.color
            )
        )
    
    return res