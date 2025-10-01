# backend/seeds/associations/leagues_tournaments.py

import json
from backend import models


def seed_leagues_tournaments(db):
    with open("../data/associations/leagues_tournaments.json", "r", encoding="utf-8") as f:
        league_tournament_data = json.load(f)

    leagues_tournaments = [
        models.leagues_tournaments_table(
            league_id=league_tournament["league_id"],
            tournament_id=league_tournament["tournament_id"]
        )
        for league_tournament in league_tournament_data
    ]

    db.add_all(leagues_tournaments)
    db.commit()
