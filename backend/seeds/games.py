# backend/seeds/games.py

from backend import models
from datetime import date, time

def seed_games(db):
    games = [
        models.Game(
            top_team_id = 1,
            bottom_team_id = 2,
            date = date(2025, 7, 1),
            start_time = time(9, 0, 5),
            end_time = time(10, 35, 12),
            tournament = "練習試合",
            location = "東京大学駒場キャンパス野球場",
            status = models.GameStatusEnum.confirmed
        ),
        models.Game(
            top_team_id = 3,
            bottom_team_id = 1,
            date = date(2025, 7, 4),
            start_time = time(10, 4, 37),
            end_time = time(11, 53, 21),
            tournament = "東京都大学リーグ春季リーグ戦2025",
            location = "大類ソフトボールパーク",
            status = models.GameStatusEnum.finished
        ),
        models.Game(
            top_team_id = 2,
            bottom_team_id = 3,
            date = date(2025, 7, 10),
            start_time = time(13, 0, 0),
            end_time = time(15, 12, 45),
            tournament = "東京都大学リーグ春季リーグ戦2025",
            location = "早稲田大学東伏見キャンパスグラウンド",
            status = models.GameStatusEnum.finished
        ),
        models.Game(
            top_team_id = 4,
            bottom_team_id = 1,
            date = date(2025, 7, 18),
            start_time = time(9, 30, 0),
            end_time = time(11, 45, 30),
            tournament = "練習試合",
            location = "立教大学新座キャンパス",
            status = models.GameStatusEnum.confirmed
        ),
        models.Game(
            top_team_id = 1,
            bottom_team_id = 5,
            date = date(2025, 8, 2),
            start_time = time(14, 0, 0),
            end_time = time(16, 20, 0),
            tournament = "東京都大学リーグ夏季リーグ戦2025",
            location = "明治大学和泉キャンパス",
            status = models.GameStatusEnum.ongoing
        ),
        models.Game(
            top_team_id = 6,
            bottom_team_id = 1,
            date = date(2025, 8, 15),
            start_time = time(10, 0, 0),
            end_time = time(12, 40, 0),
            tournament = "東京都大学リーグ夏季リーグ戦2025",
            location = "国士舘大学多摩キャンパス",
            status = models.GameStatusEnum.draft
        )
    ]
    db.add_all(games)
    db.commit()
