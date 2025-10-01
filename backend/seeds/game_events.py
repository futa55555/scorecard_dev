# backend/seeds/game_events.py

import json
from backend import models


def seed_game_events(db):
    with open("backend/seeds/data/game_events.json", "r", encoding="utf-8") as f:
        game_event_data = json.load(f)

    game_events = [
        models.GameEvent(
            game_event_id=game_event["game_event_id"],
            game_record_id=game_event["game_record_id"],
            created_by_user_id=game_event["created_by_user_id"]
        )
        for game_event in game_event_data
    ]

    db.add_all(game_events)
    db.commit()
