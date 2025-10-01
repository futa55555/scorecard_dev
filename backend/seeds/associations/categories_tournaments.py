# backend/seeds/associations/categories_tournaments.py

import json
from backend import models


def seed_categories_tournaments(db):
    with open("backend/seeds/data/associations/categories_tournaments.json", "r", encoding="utf-8") as f:
        category_tournament_data = json.load(f)

    if category_tournament_data:
        db.execute(
            models.categories_tournaments_table.insert(),
            category_tournament_data
        )
        db.commit()
