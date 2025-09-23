# backend/seeds/categories.py

from backend import models
from datetime import date, time

def seed_categories(db):
    categories = [
        models.Category(
            name = "大学男子"
        ),
        models.Category(
            name = "大学女子"
        )
    ]
    db.add_all(categories)
    db.commit()
