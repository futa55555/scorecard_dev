# backend/seeds/tournaments.py

from backend import models
from datetime import date, time

def seed_tournaments(db):
    tournaments = [
        models.Tournament(
            name = "練習試合",
            since_date = None,
            until_date = None
        ),
        models.Tournament(
            name = "2025年春季リーグ",
            since_date = date(2025, 4, 1),
            until_date = date(2025, 8, 31)
        )
    ]
    db.add_all(tournaments)
    db.commit()
