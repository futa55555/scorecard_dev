# backend/routers/person_info.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import person_info as schema
from backend.services import person_info as service

router = APIRouter()

@router.get("/api/person_info/{person_id}", response_model=schema.PersonPage)
def get_person_page(
    person_id: int,
    db: Session = Depends(get_db)
) -> schema.PersonPage:
    person = service.get_person(db, person_id)
    
    batter_stats = service.get_batter_stats(db, person_id)
    
    pitcher_stats = service.get_pitcher_stats(db, person_id)
    
    return schema.PersonPage(
        person = person,
        batter_stats = batter_stats,
        pitcher_stats = pitcher_stats
    )