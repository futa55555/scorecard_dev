# backend/seeds/game_members.py

import json
from backend import models


def seed_game_members(db):
    with open("./data/game_members.json", "r", encoding="utf-8") as f:
        game_member_data = json.load(f)

    game_members = [
        models.GameMember(
            game_member_id=game_member["game_member_id"],
            role=models.RoleEnum[game_member["role"]],
            person_id=game_member["person_id"],
            game_record_id=game_member["game_record_id"],
            created_by_user_id=game_member["created_by_user_id"]
        )
        for game_member in game_member_data
    ]

    db.add_all(game_members)
    db.commit()
