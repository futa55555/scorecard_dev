# backend/seeds/leagues.py

import json

from backend import models


def seed_leagues(db):
    with open("backend/seeds/data/leagues.json", "r", encoding="utf-8") as f:
        league_data = json.load(f)

    leagues = [
        models.League(
            league_id=league["league_id"],
            category_id=league["category_id"],
            name=league["name"]
        )
        for league in league_data
    ]

    db.add_all(leagues)
    db.commit()
