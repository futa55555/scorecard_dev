# backend/seeds/advance_events.py

import json
from backend import models


def seed_advance_events(db):
    with open("backend/seeds/data/advance_events.json", "r", encoding="utf-8") as f:
        advance_event_data = json.load(f)

    advance_events = [
        models.GameEvent(
            advance_event_id=advance_event["advance_event_id"],
            game_event_id=advance_event["game_event_id"],
            created_by_user_id=advance_event["created_by_user_id"]
        )
        for advance_event in advance_event_data
    ]

    db.add_all(advance_events)
    db.commit()
