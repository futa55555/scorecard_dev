# backend/seeds/tournament_teams.py

import json

from backend import models


def seed_tournament_teams(db):
    with open("backend/seeds/data/tournament_teams.json", "r", encoding="utf-8") as f:
        tournament_team_data = json.load(f)

    tournament_teams = [
        models.TournamentTeam(
            tournament_team_id=tournament_team["tournament_team_id"],
            tournament_id=tournament_team["tournament_id"],
            team_id=tournament_team["team_id"]
        )
        for tournament_team in tournament_team_data
    ]

    db.add_all(tournament_teams)
    db.commit()
