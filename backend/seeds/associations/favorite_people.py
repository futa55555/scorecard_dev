# backend/seeds/associations/favorite_people.py

import json
from backend import models


def seed_favorite_people(db):
    with open("backend/seeds/data/associations/favorite_people.json", "r", encoding="utf-8") as f:
        favorite_person_data = json.load(f)

    if favorite_person_data:
        db.execute(
            models.favorite_people_table.insert(),
            favorite_person_data
        )
        db.commit()
