# backend/seeds/associations/categories_tournaments.py

import json
from backend import models


def seed_categories_tournaments(db):
    with open("../data/associations/categories_tournaments.json", "r", encoding="utf-8") as f:
        category_tournament_data = json.load(f)

    categories_tournaments = [
        models.categories_tournaments_table(
            category_id=category_tournament["category_id"],
            tournament_id=category_tournament["tournament_id"]
        )
        for category_tournament in category_tournament_data
    ]

    db.add_all(categories_tournaments)
    db.commit()
