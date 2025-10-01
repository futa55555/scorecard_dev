# backend/seeds/associations/teams_locations.py

import json
from backend import models


def seed_teams_locations(db):
    with open("backend/seeds/data/associations/teams_locations.json", "r", encoding="utf-8") as f:
        team_location_data = json.load(f)

    if team_location_data:
        db.execute(
            models.teams_locations_table.insert(),
            team_location_data
        )
        db.commit()
