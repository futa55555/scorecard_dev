# backend/seeds/game_members.py

import json

from backend import models


def seed_game_members(db):
    with open("backend/seeds/data/game_members.json", "r", encoding="utf-8") as f:
        game_member_data = json.load(f)

    game_members = [
        models.GameMember(
            game_member_id=game_member["game_member_id"],
            game_record_id=game_member["game_record_id"],
            team_id=game_member["team_id"],
            person_id=game_member["person_id"],
            is_eligible=game_member["is_eligible"]
        )
        for game_member in game_member_data
    ]

    db.add_all(game_members)
    db.commit()
