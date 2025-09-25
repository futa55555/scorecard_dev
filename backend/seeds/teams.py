# backend/seeds/teams.py

import json

from backend import models


def seed_teams(db):
    with open("backend/seeds/data/teams.json", "r", encoding="utf-8") as f:
        team_data = json.load(f)

    teams = [
        models.Team(
            team_id=team["team_id"],
            name=team["name"],
            short_name=team["short_name"],
            category_id=team["category_id"],
            league_id=team["league_id"],
            prefecture=models.PrefectureEnum[team["prefecture"]],
            photo_url=team["photo_url"],
            color=team["color"],
            admin_user_id=team["admin_user_id"]
        )
        for team in team_data
    ]

    db.add_all(teams)
    db.commit()
