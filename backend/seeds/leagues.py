# backend/seeds/leagues.py

from backend import models
from datetime import date, time

def seed_leagues(db):
    leagues = [
        models.League(
            category_id = 1,
            name = "東京都大学ソフトボール連盟"
        ),
        models.League(
            category_id = 2,
            name = "東京都大学ソフトボール連盟"
        )
    ]
    db.add_all(leagues)
    db.commit()
