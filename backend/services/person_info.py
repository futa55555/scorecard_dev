# backend/services/person_info.py

from sqlalchemy.orm import Session
from typing import List
from backend import models
from backend.schemas import person_info as schema
from backend.cruds import person_info as crud
from collections import defaultdict

def get_person(
    db: Session,
    person_id: int
) -> schema.ForPerson:
    person, profile, grade, position_type = crud.get_person(db, person_id)
    
    return schema.ForPerson(
        person_id = person_id,
        role = profile.role,
        uniform_number = profile.uniform_number,
        name = person.name,
        pitching_side = person.pitching_side,
        batting_side = person.batting_side,
        height_cm = person.height_cm,
        weight_kg = person.weight_kg,
        birthday = person.birthday,
        grade = grade.grade,
        position_type = position_type.position_type
    )
    

def get_batter_stats(
    db: Session,
    person_id: int
) -> schema.BatterStats:
    return schema.BatterStats(
        average = 1,
        atbat = 1,
        hit = 1,
        rbi = 1,
        homerun = 1,
        steal = 1
    )
    

def get_pitcher_stats(
    db: Session,
    person_id: int
) -> schema.PitcherStats:
    return schema.PitcherStats(
        era = 1,
        win = 1,
        lose = 1,
        hold = 1,
        save = 1,
        strikeout = 1
    )
