# backend/seeds/game_members.py

from backend import models

def seed_game_members(db):
    game_members = [
        
    ]
    db.add_all(game_members)
    db.commit()