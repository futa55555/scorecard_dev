# backend/seeds/associations/teams_tournaments.py

import json
from backend import models


def seed_teams_tournaments(db):
    with open("../data/associations/teams_tournaments.json", "r", encoding="utf-8") as f:
        team_tournament_data = json.load(f)

    teams_tournaments = [
        models.teams_tournaments_table(
            team_id=team_tournament["team_id"],
            tournament_id=team_tournament["tournament_id"]
        )
        for team_tournament in team_tournament_data
    ]

    db.add_all(teams_tournaments)
    db.commit()
