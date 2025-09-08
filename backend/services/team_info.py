# backend/services/team_info.py

from sqlalchemy.orm import Session
from typing import List
from backend import models
from backend.schemas import team_info as schema
from backend.cruds import team_info as crud
from collections import defaultdict

def get_team_base(
    db: Session,
    team_id: int
) -> schema.TeamBase:
    team = crud.get_team(db, team_id)
    
    return schema.TeamBase(
        name = team.name,
        short_name = team.short_name,
        is_myteam = team.is_myteam,
        is_favorite = team.is_favorite,
        prefecture = team.prefecture,
        league = team.league,
        photo_url = team.photo_url,
        color = team.color
    )
    

def get_team_member(
    db: Session,
    team_id: int
) -> List[schema.ForTeamMember]:
    count_by_grade_and_role = crud.get_count_by_grade_and_role(db, team_id)
    
    grouped = defaultdict(lambda: {
        "player_count": 0,
        "coach_count": 0,
        "manager_count": 0,
        "trainer_count": 0,
        "analyst_count": 0,
    })
    
    for row in count_by_grade_and_role:
        grade = row["grade"]
        role = row["role"]
        cnt = row["cnt"]
        
        if role == models.RoleEnum.player:
            grouped[grade]["player_count"] += cnt
        elif role == models.RoleEnum.coach:
            grouped[grade]["coach_count"] += cnt
        elif role == models.RoleEnum.manager:
            grouped[grade]["manager_count"] += cnt
        elif role == models.RoleEnum.trainer:
            grouped[grade]["trainer_count"] += cnt
        elif role == models.RoleEnum.analyst:
            grouped[grade]["analyst_count"] += cnt
    
    res = [
        schema.ForTeamMember(grade = grade, **counts) for grade, counts in grouped.items()
    ]
    
    return res


def get_game_score(
    team_id: int,
    game: models.Game
) -> schema.ForRecentGame:
    team_score = defaultdict(int)
    for inning in game.innings:
        if inning.score >= 0:
            team_score[inning.top_bottom] += inning.score
        
    if team_id == game.top_team_id:
        my_team_score = team_score[models.TopBottomEnum.top]
        opposite_team_score = team_score[models.TopBottomEnum.bottom]
        opposite_team_short_name = game.bottom_team.short_name
    else:
        my_team_score = team_score[models.TopBottomEnum.bottom]
        opposite_team_score = team_score[models.TopBottomEnum.top]
        opposite_team_short_name = game.top_team.short_name
        
    return schema.ForRecentGame(
        my_team_score = my_team_score,
        opposite_team_score = opposite_team_score,
        opposite_team_short_name = opposite_team_short_name,
        date = game.date,
        tournament = game.tournament
    )


def get_recent_game(
    db: Session,
    team_id: int
) -> List[schema.ForRecentGame]:
    recent_game = crud.get_recent_game(db, team_id)
    
    res = []
    for game in recent_game:
        res.append(
            get_game_score(team_id, game)
        )
    
    return res


def get_team_name(
    db: Session,
    team_id: int
) -> str:
    team = crud.get_team(db, team_id)
    return team.name


def get_all_member(
    db: Session,
    team_id: int
) -> List[schema.ForAllMembers]:
    res = []
    
    people_with_all_info = crud.get_all_member(db, team_id)
    
    for person, profile, grade, position_type in people_with_all_info:
        res.append(
            schema.ForAllMembers(
                person_id = person.id,
                role = profile.role,
                uniform_number = profile.uniform_number,
                name = person.name,
                pitching_side = person.pitching_side,
                batting_side = person.batting_side,
                height_cm = person.height_cm,
                weight_kg = person.weight_kg,
                birtyday = person.birthday,
                grade = grade.grade,
                position_type = position_type.position_type
            )
        )
    
    return res
