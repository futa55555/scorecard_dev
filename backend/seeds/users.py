# backend/seeds/users.py

from backend import models
from datetime import date, time

def seed_users(db):
    users = [
        models.User(
            name = "reira_okamura",
            password = "reira",
            birthday = date(2006, 4, 1)
        ),
        models.User(
            name = "asami_kawana",
            password = "asami",
            birthday = date(2006, 5, 1)
        ),
        models.User(
            name = "rio_kobayashi",
            password = "rio",
            birthday = date(2006, 6, 1)
        )
    ]
    db.add_all(users)
    db.commit()
