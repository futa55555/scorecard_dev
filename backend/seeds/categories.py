# backend/seeds/categories.py

import json

from backend import models


def seed_categories(db):
    with open("backend/seeds/data/categories.json", "r", encoding="utf-8") as f:
        category_data = json.load(f)

    categories = [
        models.Category(
            category_id=category["category_id"],
            name=category["name"]
        )
        for category in category_data
    ]

    db.add_all(categories)
    db.commit()
