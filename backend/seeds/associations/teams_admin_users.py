# backend/seeds/associations/teams_admin_users.py

import json
from backend import models


def seed_teams_admin_users(db):
    with open("backend/seeds/data/associations/teams_admin_users.json", "r", encoding="utf-8") as f:
        team_admin_user_data = json.load(f)

    if team_admin_user_data:
        db.execute(
            models.teams_admin_users_table.insert(),
            team_admin_user_data
        )
        db.commit()
