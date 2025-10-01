# backend/seeds/associations/categories_teams.py

import json
from backend import models


def seed_categories_teams(db):
    with open("backend/seeds/data/associations/categories_teams.json", "r", encoding="utf-8") as f:
        category_team_data = json.load(f)

    if category_team_data:
        db.execute(
            models.categories_teams_table.insert(),
            category_team_data
        )
        db.commit()
