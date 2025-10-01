# backend/seeds/associations/favorite_people.py

import json
from backend import models


def seed_favorite_people(db):
    with open("../data/associations/favorite_people.json", "r", encoding="utf-8") as f:
        favorite_person_data = json.load(f)

    favorite_people = [
        models.favorite_people_table(
            user_id=favorite_person["user_id"],
            person_id=favorite_person["person_id"]
        )
        for favorite_person in favorite_person_data
    ]

    db.add_all(favorite_people)
    db.commit()
