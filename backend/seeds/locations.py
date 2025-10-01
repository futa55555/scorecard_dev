# backend/seeds/locations.py

import json
from backend import models


def seed_locations(db):
    with open("backend/seeds/data/locations.json", "r", encoding="utf-8") as f:
        location_data = json.load(f)

    locations = [
        models.Location(
            location_id=location["location_id"],
            name=location["name"],
            prefecture=location["prefecture"],
            created_by_user_id=location["created_by_user_id"]
        )
        for location in location_data
    ]

    db.add_all(locations)
    db.commit()
