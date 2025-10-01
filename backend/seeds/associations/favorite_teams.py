# backend/seeds/associations/favorite_teams.py

import json
from backend import models


def seed_favorite_teams(db):
    with open("../data/associations/favorite_teams.json", "r", encoding="utf-8") as f:
        favorite_team_data = json.load(f)

    favorite_teams = [
        models.favorite_teams_table(
            user_id=favorite_team["user_id"],
            team_id=favorite_team["team_id"]
        )
        for favorite_team in favorite_team_data
    ]

    db.add_all(favorite_teams)
    db.commit()
