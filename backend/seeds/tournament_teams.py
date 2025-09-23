# backend/seeds/tournament_teams.py

from backend import models
from datetime import date, time

def seed_tournament_teams(db):
    tournament_teams = [
        models.TournamentTeam(tournament_id=1, team_id=1),
        models.TournamentTeam(tournament_id=1, team_id=2),
        models.TournamentTeam(tournament_id=1, team_id=3),
        models.TournamentTeam(tournament_id=1, team_id=4),
        models.TournamentTeam(tournament_id=1, team_id=5),
        models.TournamentTeam(tournament_id=1, team_id=6),
        models.TournamentTeam(tournament_id=2, team_id=1),
        models.TournamentTeam(tournament_id=2, team_id=2),
        models.TournamentTeam(tournament_id=2, team_id=3),
        models.TournamentTeam(tournament_id=2, team_id=4),
        models.TournamentTeam(tournament_id=2, team_id=5),
        models.TournamentTeam(tournament_id=2, team_id=6),
    ]
    db.add_all(tournament_teams)
    db.commit()
