# backend/cruds/members.py

from sqlalchemy.orm import Session
from backend import models


def set_myteam(team_id: int, db: Session):
    """
    全チームの is_myteam を False にしてから、 
    指定チームの is_myteam を True に設定
    """
    # 全チームを False にする
    db.query(models.Team).update({models.Team.is_myteam: False})
    
    # 指定チームを True にする
    team = db.get(models.Team, team_id)
    if team:
        team.is_myteam = True
        db.commit()
    return team
        

def unset_myteam(team_id: int, db: Session):
    """
    指定チームの is_myteam を False に設定
    """
    team = db.get(models.Team, team_id)
    if team:
        team.is_myteam = False
        db.commit()
    return team