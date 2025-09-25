# backend/seeds/tournament_categories.py

import json

from backend import models


def seed_tournament_categories(db):
    with open("backend/seeds/data/tournament_categories.json", "r", encoding="utf-8") as f:
        tournament_category_data = json.load(f)

    tournament_categories = [
        models.TournamentCategory(
            tournament_category_id=tournament_category["tournament_category_id"],
            tournament_id=tournament_category["tournament_id"],
            category_id=tournament_category["category_id"]
        )
        for tournament_category in tournament_category_data
    ]

    db.add_all(tournament_categories)
    db.commit()
