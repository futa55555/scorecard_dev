# backend/seeds/associations/categories_leagues.py

import json
from backend import models


def seed_categories_leagues(db):
    with open("backend/seeds/data/associations/categories_leagues.json", "r", encoding="utf-8") as f:
        category_league_data = json.load(f)

    if category_league_data:
        db.execute(
            models.categories_leagues_table.insert(),
            category_league_data
        )
        db.commit()
