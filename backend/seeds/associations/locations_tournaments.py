# backend/seeds/associations/locations_tournaments.py

import json
from backend import models


def seed_locations_tournaments(db):
    with open("backend/seeds/data/associations/locations_tournaments.json", "r", encoding="utf-8") as f:
        locations_tournament_data = json.load(f)

    if locations_tournament_data:
        db.execute(
            models.locations_tournaments_table.insert(),
            locations_tournament_data
        )
        db.commit()
