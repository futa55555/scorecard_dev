# backend/seeds/users.py

import json
from backend import models


def seed_users(db):
    with open("backend/seeds/data/users.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)

    users = [
        models.User(
            user_id=user["user_id"],
            name=user["name"],
            password=user["password"],
            own_person_id=user["own_person_id"]
        )
        for user in user_data
    ]

    db.add_all(users)
    db.commit()
