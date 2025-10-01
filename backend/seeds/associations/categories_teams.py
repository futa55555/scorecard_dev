# backend/seeds/associations/categories_teams.py

import json
from backend import models


def seed_categories_teams(db):
    with open("../data/associations/categories_teams.json", "r", encoding="utf-8") as f:
        category_team_data = json.load(f)

    categories_teams = [
        models.categories_teams_table(
            category_id=category_team["category_id"],
            team_id=category_team["team_id"]
        )
        for category_team in category_team_data
    ]

    db.add_all(categories_teams)
    db.commit()
