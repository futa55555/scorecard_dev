# backend/services/game_info.py

from sqlalchemy.orm import Session
from typing import Dict
from backend import models
from backend.schemas import game_info as schema
from backend.cruds import game_info as crud

def get_game_base(
    db: Session,
    game_id: int
) -> schema.GameBase:
    """
    試合の基本情報を取得
    """
    game = crud.get_game_base(db, game_id)
    
    return schema.GameBase(
        top_team_id=game.top_team_id,
        bottom_team_id=game.bottom_team_id,
        top_team_short_name=game.top_team.short_name,
        bottom_team_short_name=game.bottom_team.short_name,
        date=game.date,
        start_time=game.start_time,
        end_time=game.end_time,
        tournament=game.tournament,
        location=game.location,
        status=game.status
    )
    

def calc_total_score(
    db: Session,
    game_id: int
) -> Dict[str, int]:
    """
    チームごとの総得点と総安打数を計算
    """
    all_innings_with_atbat = crud.get_all_innings_with_atbat(db, game_id)
    atbats = all_innings_with_atbat.atbats
    
    top_team_total_score = 0
    bottom_team_total_score = 0
    top_team_total_hit = 0
    bottom_team_total_hit = 0
    
    for inning_with_atbat in all_innings_with_atbat:
        if inning_with_atbat.top_bottom == models.TopBottomEnum.top:
            top_team_total_score += inning_with_atbat.score
            for atbat in atbats:
                if atbat.result == models.AtBatResultEnum.hit:
                    top_team_total_hit += 1
        else:
            bottom_team_total_score += inning_with_atbat.score
            for atbat in atbats:
                if atbat.result == models.AtBatResultEnum.hit:
                    bottom_team_total_hit += 1
    
    return {
        "top_team_total_score": top_team_total_score,
        "bottom_team_total_score": bottom_team_total_score,
        "top_team_total_hit": top_team_total_hit,
        "bottom_team_total_hit": bottom_team_total_hit
    }


def get_score_of_all_innings(
    db: Session,
    game_id: int
) -> schema.InningScore:
    """
    スコアボードに記録される得点、ヒットを取得
    """
    all_innings = crud.get_all_innings(db, game_id)