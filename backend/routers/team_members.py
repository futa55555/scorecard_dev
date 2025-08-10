# backend/routers/team_members.py

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from backend.database import get_db
from backend import models
from backend.schemas import team_members as team_members_schema
from backend.cruds import team_members as team_members_crud

# GET: 一覧取得
# POST: 追加 / 更新 / 移籍
# DELETE: 削除

router = APIRouter()

@router.get("/api/team_members/{team_id}", response_model=team_members_schema.TeamMembersResponse)
def get_team_members(team_id: int, db: Session = Depends(get_db)):
    """
    そのチームの選手一覧を取得してJSONで返す
    """
    # チームを取得
    team = db.get(models.Team, team_id)
    if not team:
        return None
    
    # チームに所属経験のある選手（MemberProfile + Person）をすべて取得
    profiles = (
        db.query(models.MemberProfile)
        .options(joinedload(models.MemberProfile.person))
        .filter(models.MemberProfile.team_id == team_id)
        .all()
    )
    
    # person.id ごとにまとめて、member_with_profiles を作る
    member_dict = {}
    for profile in profiles:
        person = profile.person
        if person.id not in member_dict:
            member_dict[person.id] = team_members_schema.MemberWithProfiles(
                name=person.name,
                pitching_side=person.pitching_side,
                batting_side=person.batting_side,
                photo_url=person.photo_url,
                height_cm=person.height_cm,
                weight_kg=person.weight_kg,
                birthday=person.birthday,
                member_profiles=[]
            )
        member_dict[person.id].member_profiles.append(
            team_members_schema.MemberProfileBase(
                since_date=profile.since_date,
                until_date=profile.until_date,
                uniform_number=profile.uniform_number,
                role=profile.role,
            )
        )

    return team_members_schema.TeamMembersResponse(
        id=team.id,
        name=team.name,
        is_myteam=team.is_myteam,
        short_name=team.short_name,
        prefecture=team.prefecture,
        league=team.league,
        color=team.color,
        member_with_profiles=list(member_dict.values())
    )


# @router.post("/api/team_members/{team_id}")
# def add_team_members(team_id: int, members_data: team_members_schema.TeamMembersCreate, db: Session = Depends(get_db)):
#     """
#     フォームデータから選手を追加し、選手情報を返す
#     """
#     for member in members_data.members:
#         # Person作成
#         person = models.Person(
#             name=member.name,
#             pitching_side=member.pitching_side,
#             batting_side=member.batting_side,
#             photo_url=str(member.photo_url) if member.photo_url else None,
#             height_cm=member.height_cm,
#             weight_kg=member.weight_kg,
#             birthday=member.birthday,
#         )
#         db.add(person)
#         db.commit()
#         db.refresh(person)

#         # MemberProfile作成
#         profile = models.MemberProfile(
#             person_id=person.id,
#             team_id=team_id,
#             since_date=member.since_date,
#             until_date=member.until_date,
#             uniform_number=member.uniform_number,
#             role=member.role
#         )
#         db.add(profile)
#     db.commit()
    
#     return {"success": True}
