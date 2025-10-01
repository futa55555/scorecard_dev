# backend/seeds/player_positions.py

import json
from datetime import date
from backend import models


def seed_player_positions(db):
    with open("backend/seeds/data/player_positions.json", "r", encoding="utf-8") as f:
        player_position_data = json.load(f)

    player_positions = [
        models.PlayerPosition(
            player_position_id=player_position["player_position_id"],
            position_type=models.PositionTypeEnum[player_position["position_type"]],
            since_date=date.fromisoformat(player_position["since_date"]),
            until_date=date.fromisoformat(player_position["until_date"]) if player_position["until_date"] else None,
            is_official=player_position["is_official"],
            person_id=player_position["person_id"],
            created_by_user_id=player_position["created_by_user_id"]
        )
        for player_position in player_position_data
    ]

    db.add_all(player_positions)
    db.commit()
