# backend/seeds/associations/favorite_tournaments.py

import json
from backend import models


def seed_favorite_tournaments(db):
    with open("../data/associations/favorite_tournaments.json", "r", encoding="utf-8") as f:
        favorite_tournament_data = json.load(f)

    favorite_tournaments = [
        models.favorite_tournaments_table(
            user_id=favorite_tournament["user_id"],
            tournament_id=favorite_tournament["tournament_id"]
        )
        for favorite_tournament in favorite_tournament_data
    ]

    db.add_all(favorite_tournaments)
    db.commit()
