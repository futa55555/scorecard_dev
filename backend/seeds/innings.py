# backend/seeds/innings.py

from backend import models
import random
random.seed(42)


def seed_innings(db):
    """
    5試合分 (game_id=1..5)、各7イニング (1..7)、表裏 (top, bottom)
    を必ず作成する。
    score は 0〜5 のランダム整数。
    """
    innings = []
    current_id = 1

    for game_id in range(1, 6):  # 1〜5試合
        for inning_number in range(1, 8):  # 1〜7イニング
            for tb in [models.TopBottomEnum.top, models.TopBottomEnum.bottom]:
                innings.append(
                    models.Inning(
                        inning_id=current_id,
                        game_id=game_id,
                        inning_number=inning_number,
                        top_bottom=tb,
                        score=random.randint(0, 5),
                    )
                )
                current_id += 1

    db.add_all(innings)
    db.commit()
