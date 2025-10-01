# backend/seeds/associations/locations_tournaments.py

import json
from backend import models


def seed_locations_tournaments(db):
    with open("../data/associations/locations_tournaments.json", "r", encoding="utf-8") as f:
        locations_tournament_data = json.load(f)

    locations_tournaments = [
        models.locations_tournaments_table(
            locations_id=locations_tournament["locations_id"],
            tournament_id=locations_tournament["tournament_id"]
        )
        for locations_tournament in locations_tournament_data
    ]

    db.add_all(locations_tournaments)
    db.commit()
