# backend/seeds/tournament_categories.py

from backend import models
from datetime import date, time

def seed_tournament_categories(db):
    tournament_categories = [
        models.TournamentCategory(tournament_id=1, category_id=1),
        models.TournamentCategory(tournament_id=1, category_id=2),
        models.TournamentCategory(tournament_id=2, category_id=1),
        models.TournamentCategory(tournament_id=2, category_id=2)
    ]
    db.add_all(tournament_categories)
    db.commit()
