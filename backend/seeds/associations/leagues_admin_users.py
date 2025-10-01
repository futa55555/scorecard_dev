# backend/seeds/associations/leagues_admin_users.py

import json
from backend import models


def seed_leagues_admin_users(db):
    with open("backend/seeds/data/associations/leagues_admin_users.json", "r", encoding="utf-8") as f:
        league_admin_user_data = json.load(f)

    if league_admin_user_data:
        db.execute(
            models.leagues_admin_users_table.insert(),
            league_admin_user_data
        )
        db.commit()
