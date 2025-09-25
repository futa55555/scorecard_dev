# backend/seeds/game_records.py

import json
from datetime import date, time

from backend import models


def seed_game_records(db):
    with open("backend/seeds/data/game_records.json", "r", encoding="utf-8") as f:
        game_record_data = json.load(f)

    game_records = [
        models.GameRecord(
            game_record_id=game_record["game_record_id"],
            game_id=game_record["game_id"],
            team_id=game_record["team_id"]
        )
        for game_record in game_record_data
    ]

    db.add_all(game_records)
    db.commit()
