# backend/seeds/associations/leagues_tournaments.py

import json
from backend import models


def seed_leagues_tournaments(db):
    with open("backend/seeds/data/associations/leagues_tournaments.json", "r", encoding="utf-8") as f:
        league_tournament_data = json.load(f)

    if league_tournament_data:
        db.execute(
            models.leagues_tournaments_table.insert(),
            league_tournament_data
        )
        db.commit()
