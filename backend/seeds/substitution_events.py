# backend/seeds/substitution_events.py

import json
from backend import models


def seed_substitution_events(db):
    with open("./data/substitution_events.json", "r", encoding="utf-8") as f:
        substitution_event_data = json.load(f)

    substitution_events = [
        models.GameEvent(
            substitution_event_id=substitution_event["substitution_event_id"],
            game_event_id=substitution_event["game_event_id"],
            created_by_user_id=substitution_event["created_by_user_id"]
        )
        for substitution_event in substitution_event_data
    ]

    db.add_all(substitution_events)
    db.commit()
