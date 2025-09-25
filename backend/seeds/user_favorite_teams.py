# backend/seeds/user_favorite_teams.py

import json

from backend import models


def seed_user_favorite_teams(db):
    with open("backend/seeds/data/user_favorite_teams.json", "r", encoding="utf-8") as f:
        user_favorite_team_data = json.load(f)

    user_favorite_teams = [
        models.UserFavoriteTeam(
            user_favorite_team_id=user_favorite_team["user_favorite_team_id"],
            user_id=user_favorite_team["user_id"],
            team_id=user_favorite_team["team_id"]
        )
        for user_favorite_team in user_favorite_team_data
    ]

    db.add_all(user_favorite_teams)
    db.commit()
