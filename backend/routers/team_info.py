# backend/routers/team_info.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import team_info as schema
from backend.services import team_info as service

router = APIRouter()

@router.get("/api/team_info/{team_id}/top", response_model=schema.TeamInfoTop)
def get_team_info_top(
    team_id: int,
    db: Session = Depends(get_db)
) -> schema.TeamInfoTop:
    team_base = service.get_team_base(db, team_id)
    
    team_member = service.get_team_member(db, team_id)
    
    recent_game = service.get_recent_game(db, team_id)
    
    return schema.TeamInfoTop(
        team_base = team_base,
        team_member = team_member,
        recent_game = recent_game
    )
    

@router.get("/api/team_info/{team_id}/members", response_model=schema.AllMembers)
def get_all_members(
    team_id: int,
    db: Session = Depends(get_db)
) -> schema.AllMembers:
    team_name = service.get_team_name(db, team_id)
    
    member = service.get_all_member(db, team_id)
    
    return schema.AllMembers(
        team_name = team_name,
        member = member
    )
    

@router.get("/api/team_info/{team_id}/members/{person_id}", response_model=schema.MemberPage)
def get_member_page(
    team_id: int,
    person_id: int,
    db: Session = Depends(get_db)
) -> schema.MemberPage:
    member = service.get_member(db, person_id)
    
    batter_stats = service.get_batter_stats(db, person_id)
    
    return schema.MemberPage(
        member = member,
        batter_stats = batter_stats,
        pitcher_stats = pitcher_stats
    )