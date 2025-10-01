# backend/seeds/associations/teams_tournaments.py

import json
from backend import models


def seed_teams_tournaments(db):
    with open("backend/seeds/data/associations/teams_tournaments.json", "r", encoding="utf-8") as f:
        team_tournament_data = json.load(f)

    if team_tournament_data:
        db.execute(
            models.teams_tournaments_table.insert(),
            team_tournament_data
        )
        db.commit()
