# backend/seeds/associations/teams_admin_users.py

import json
from backend import models


def seed_teams_admin_users(db):
    with open("../data/associations/teams_admin_users.json", "r", encoding="utf-8") as f:
        team_admin_user_data = json.load(f)

    team_admin_users = [
        models.teams_admin_users_table(
            user_id=team_admin_user["user_id"],
            team_id=team_admin_user["team_id"]
        )
        for team_admin_user in team_admin_user_data
    ]

    db.add_all(team_admin_users)
    db.commit()
