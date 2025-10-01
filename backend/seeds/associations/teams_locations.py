# backend/seeds/associations/teams_locations.py

import json
from backend import models


def seed_teams_locations(db):
    with open("../data/associations/teams_locations.json", "r", encoding="utf-8") as f:
        team_location_data = json.load(f)

    teams_locations = [
        models.teams_locations_table(
            team_id=team_location["team_id"],
            location_id=team_location["location_id"]
        )
        for team_location in team_location_data
    ]

    db.add_all(teams_locations)
    db.commit()
