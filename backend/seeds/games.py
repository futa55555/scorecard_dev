# backend/seeds/games.py

import json
from datetime import date, time

from backend import models


def seed_games(db):
    with open("backend/seeds/data/games.json", "r", encoding="utf-8") as f:
        game_data = json.load(f)

    games = [
        models.Game(
            top_team_id=game["top_team_id"] if game["top_team_id"] else None,
            bottom_team_id=game["bottom_team_id"] if game["bottom_team_id"] else None,
            top_bottom_decided=game["top_bottom_decided"],
            date=date.fromisoformat(game["date"]) if game["date"] else None,
            start_time=time.fromisoformat(game["start_time"]) if game["start_time"] else None,
            end_time=time.fromisoformat(game["end_time"]) if game["end_time"] else None,
            tournament_id=game["tournament_id"],
            location=game["location"],
            status=models.GameStatusEnum[game["status"]]
        )
        for game in game_data
    ]

    db.add_all(games)
    db.commit()
