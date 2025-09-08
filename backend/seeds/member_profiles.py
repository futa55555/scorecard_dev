# backend/seeds/member_profiles.py

from backend import models
from datetime import date, timedelta
import random

def seed_member_profiles(db):
    profiles = []

    roles = (
        ["player"] * 90 +
        ["manager"] * 7 +
        ["coach"] * 1 +
        ["trainer"] * 1 +
        ["analyst"] * 1
    )

    for person_id in range(1, 101):  # 100人
        # 開始基準年をランダムに決める
        start_year = random.randint(2015, 2022)
        current_date = date(start_year, random.randint(1, 12), random.randint(1, 28))

        for j in range(5):
            # role を確率分布に基づいて選択
            role = models.RoleEnum(random.choice(roles))

            # チームIDをランダム
            team_id = random.randint(1, 6)

            # 背番号をランダム
            uniform_number = random.randint(1, 99)

            # 期間を決める
            if j < 4:  # 最初の4つは終了日あり
                duration = timedelta(days=random.randint(200, 500))  # ざっくり半年〜1年半
                until_date = current_date + duration
                since_date = current_date
                # 次の開始日 = 終了日 + ギャップ（0〜180日）
                current_date = until_date + timedelta(days=random.randint(0, 180))
            else:
                # 最後の1レコードは現役
                since_date = current_date
                until_date = None

            profile = models.MemberProfile(
                person_id=person_id,
                team_id=team_id,
                since_date=since_date,
                until_date=until_date,
                uniform_number=uniform_number,
                role=role
            )
            profiles.append(profile)

    db.add_all(profiles)
    db.commit()
