# backend/seeds/games.py

import json
from datetime import date, time
from backend import models


def seed_games(db):
    with open("backend/seeds/data/games.json", "r", encoding="utf-8") as f:
        game_data = json.load(f)

    games = [
        models.Game(
            game_id=game["game_id"],
            date=date.fromisoformat(game["date"]) if game["date"] else None,
            start_time=time.fromisoformat(game["start_time"]) if game["start_time"] else None,
            end_time=time.fromisoformat(game["end_time"]) if game["end_time"] else None,
            top_team_id=game["top_team_id"] if game["top_team_id"] else None,
            bottom_team_id=game["bottom_team_id"] if game["bottom_team_id"] else None,
            tournament_id=game["tournament_id"],
            location_id=game["location_id"],
            created_by_user_id=game["created_by_user_id"]
        )
        for game in game_data
    ]

    db.add_all(games)
    db.commit()
