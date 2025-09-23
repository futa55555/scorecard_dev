# backend/seeds/user_favorite_teams.py

from backend import models
from datetime import date, time

def seed_user_favorite_teams(db):
    user_favorite_teams = [
        models.UserFavoriteTeam(user_id=1, team_id=1),
        models.UserFavoriteTeam(user_id=1, team_id=3),
        models.UserFavoriteTeam(user_id=1, team_id=5),
        models.UserFavoriteTeam(user_id=2, team_id=2),
        models.UserFavoriteTeam(user_id=2, team_id=4),
        models.UserFavoriteTeam(user_id=2, team_id=6),
        models.UserFavoriteTeam(user_id=3, team_id=1),
        models.UserFavoriteTeam(user_id=3, team_id=2),
        models.UserFavoriteTeam(user_id=3, team_id=5),
        models.UserFavoriteTeam(user_id=3, team_id=6)
    ]
    db.add_all(user_favorite_teams)
    db.commit()
