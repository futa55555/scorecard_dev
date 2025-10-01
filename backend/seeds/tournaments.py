# backend/seeds/tournaments.py

import json
from datetime import date
from backend import models


def seed_tournaments(db):
    with open("backend/seeds/data/tournaments.json", "r", encoding="utf-8") as f:
        tournament_data = json.load(f)

    tournaments = [
        models.Tournament(
            tournament_id=tournament["tournament_id"],
            name=tournament["name"],
            since_date=date.fromisoformat(tournament["since_date"]) if tournament["since_date"] else None,
            until_date=date.fromisoformat(tournament["until_date"]) if tournament["until_date"] else None,
            is_official=tournament["is_official"],
            created_by_user_id=tournament["created_by_user_id"]
        )
        for tournament in tournament_data
    ]

    db.add_all(tournaments)
    db.commit()
