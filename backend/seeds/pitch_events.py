# backend/seeds/pitch_events.py

import json
from backend import models


def seed_pitch_events(db):
    with open("./data/pitch_events.json", "r", encoding="utf-8") as f:
        pitch_event_data = json.load(f)

    pitch_events = [
        models.GameEvent(
            pitch_event_id=pitch_event["pitch_event_id"],
            game_event_id=pitch_event["game_event_id"],
            created_by_user_id=pitch_event["created_by_user_id"]
        )
        for pitch_event in pitch_event_data
    ]

    db.add_all(pitch_events)
    db.commit()
