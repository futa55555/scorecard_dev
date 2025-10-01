# backend/seeds/leagues.py

import json
from backend import models


def seed_leagues(db):
    with open("./data/leagues.json", "r", encoding="utf-8") as f:
        league_data = json.load(f)

    leagues = [
        models.League(
            league_id=league["league_id"],
            name=league["name"],
            chief_admin_user_id=league["chief_admin_user_id"]
        )
        for league in league_data
    ]

    db.add_all(leagues)
    db.commit()
