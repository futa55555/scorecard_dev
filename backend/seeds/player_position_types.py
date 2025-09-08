# backend/seeds/player_position_types.py

from backend import models
from datetime import date
import random

def seed_player_position_types(db):
    positions = []

    # ポジション分布（確率）
    weighted_positions = (
        ["P"] * 15 +   # 投手: 15%
        ["C"] * 10 +   # 捕手: 10%
        ["IF"] * 40 +  # 内野手: 40%
        ["OF"] * 35    # 外野手: 35%
    )

    for person_id in range(1, 101):
        pos = models.PositionTypeEnum(random.choice(weighted_positions))

        # 入学年をランダムに決める（2015〜2022）
        start_year = random.randint(2015, 2022)
        since_date = date(start_year, 4, 1)

        ppt = models.PlayerPositionType(
            person_id=person_id,
            position_type=pos,
            since_date=since_date,
            until_date=None   # 現役
        )
        positions.append(ppt)

    db.add_all(positions)
    db.commit()
