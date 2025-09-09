# backend/seeds/game_members.py

from backend import models
import random

def seed_game_members(db):
    game_members = []

    # 全ゲームを取得
    games = db.query(models.Game).all()

    for game in games:
        # 各ゲームの2チーム
        for team_id in [game.top_team_id, game.bottom_team_id]:
            if team_id is None:
                continue

            # 現役メンバーを取得
            members = (
                db.query(models.MemberProfile)
                .filter(
                    models.MemberProfile.team_id == team_id,
                    models.MemberProfile.until_date.is_(None)
                )
                .all()
            )
            person_ids = [m.person_id for m in members]

            # シャッフルしてランダムな先発メンバーを作る
            random.shuffle(person_ids)

            # 打順: No1〜No9
            batting_orders = [
                models.BattingOrderEnum.No1,
                models.BattingOrderEnum.No2,
                models.BattingOrderEnum.No3,
                models.BattingOrderEnum.No4,
                models.BattingOrderEnum.No5,
                models.BattingOrderEnum.No6,
                models.BattingOrderEnum.No7,
                models.BattingOrderEnum.No8,
                models.BattingOrderEnum.No9,
            ]

            # 守備位置: P〜RF
            positions = [
                models.PositionEnum.P,
                models.PositionEnum.C,
                models.PositionEnum.FB,
                models.PositionEnum.SB,
                models.PositionEnum.TB,
                models.PositionEnum.SS,
                models.PositionEnum.LF,
                models.PositionEnum.CF,
                models.PositionEnum.RF,
            ]

            # 先発9人まで
            starters = person_ids[:9]
            for idx, person_id in enumerate(starters):
                gm = models.GameMember(
                    game_id=game.id,
                    team_id=team_id,
                    person_id=person_id,
                    starting_batting_order=batting_orders[idx],
                    starting_position=positions[idx]
                )
                game_members.append(gm)

            # それ以降はベンチ
            for idx, person_id in enumerate(person_ids[9:], start=10):
                gm = models.GameMember(
                    game_id=game.id,
                    team_id=team_id,
                    person_id=person_id,
                    starting_batting_order=models.BattingOrderEnum.NOT,
                    starting_position=models.PositionEnum.NOT
                )
                game_members.append(gm)

    db.add_all(game_members)
    db.commit()
