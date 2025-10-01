# backend/seeds/associations/favorite_tournaments.py

import json
from backend import models


def seed_favorite_tournaments(db):
    with open("backend/seeds/data/associations/favorite_tournaments.json", "r", encoding="utf-8") as f:
        favorite_tournament_data = json.load(f)

    if favorite_tournament_data:
        db.execute(
            models.favorite_tournaments_table.insert(),
            favorite_tournament_data
        )
        db.commit()
