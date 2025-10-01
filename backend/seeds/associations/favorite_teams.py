# backend/seeds/associations/favorite_teams.py

import json
from backend import models


def seed_favorite_teams(db):
    with open("backend/seeds/data/associations/favorite_teams.json", "r", encoding="utf-8") as f:
        favorite_team_data = json.load(f)

    if favorite_team_data:
        db.execute(
            models.favorite_teams_table.insert(),
            favorite_team_data
        )
        db.commit()
