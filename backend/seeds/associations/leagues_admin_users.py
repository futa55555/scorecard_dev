# backend/seeds/associations/leagues_admin_users.py

import json
from backend import models


def seed_leagues_admin_users(db):
    with open("../data/associations/leagues_admin_users.json", "r", encoding="utf-8") as f:
        league_admin_user_data = json.load(f)

    league_admin_users = [
        models.leagues_admin_users_table(
            user_id=league_admin_user["user_id"],
            team_id=league_admin_user["team_id"]
        )
        for league_admin_user in league_admin_user_data
    ]

    db.add_all(league_admin_users)
    db.commit()
