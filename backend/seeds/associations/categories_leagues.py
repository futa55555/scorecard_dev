# backend/seeds/associations/categories_leagues.py

import json
from backend import models


def seed_categories_leagues(db):
    with open("../data/associations/categories_leagues.json", "r", encoding="utf-8") as f:
        category_league_data = json.load(f)

    categories_leagues = [
        models.categories_leagues_table(
            category_id=category_league["category_id"],
            league_id=category_league["league_id"]
        )
        for category_league in category_league_data
    ]

    db.add_all(categories_leagues)
    db.commit()
