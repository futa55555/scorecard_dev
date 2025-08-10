# backend/routes/teams.py

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import teams as teams_schema
from backend.cruds import teams as teams_crud


# このルーターはチーム管理に関するAPI（JSON形式）を提供する
# GET: 一覧取得
# POST: 追加 / マイチーム設定
# DELETE: 削除


router = APIRouter()


@router.get("/api/teams", response_model=list[teams_schema.TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    """
    チーム一覧を取得してJSONで返す
    """
    stmt = select(models.Team)
    teams = db.scalars(stmt).all()
    return teams  # ORM → 自動でJSONに変換（from_attributes=True）





@router.post("/api/teams/add", response_model=teams_schema.TeamResponse)
def add_team(team_data: teams_schema.TeamCreate, db: Session = Depends(get_db)):
    """
    フォームデータからチームを追加し、追加されたチーム情報を返す
    """
    team = models.Team(**team_data.model_dump())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


@router.delete("/api/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    """
    指定されたIDのチームを削除する
    """
    team = db.get(models.Team, team_id)
    if team:
        db.delete(team)
        db.commit()
    return {"success": True}


@router.post("/api/teams/{team_id}/mark_myteam")
def mark_team_as_myteam(team_id: int, db: Session = Depends(get_db)):
    """
    指定チームを「マイチーム」に設定する（他は自動でFalseに）
    """
    if teams_crud.set_myteam(team_id, db):
        return {"success": True}
    else:
        return {"success": False}


@router.post("/api/teams/{team_id}/unmark_myteam")
def unmark_team_as_myteam(team_id: int, db: Session = Depends(get_db)):
    """
    指定チームの「マイチーム」設定を解除する
    """
    if teams_crud.unset_myteam(team_id, db):
        return {"success": True}
    else:
        return {"success": False}
