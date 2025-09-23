# backend/seeds/member_grades.py

from backend import models
from datetime import date
import random
random.seed(42)

# 上限日付
CUTOFF_DATE = date(2025, 9, 21)


def seed_member_grades(db):
    grades = []

    all_grades = [
        models.GradeEnum.B1,
        models.GradeEnum.B2,
        models.GradeEnum.B3,
        models.GradeEnum.B4,
        models.GradeEnum.M1,
        models.GradeEnum.M2,
    ]

    for person_id in range(1, 201):  # 200人分
        start_year = random.randint(2020, 2025)
        current_year = start_year

        for grade_enum in all_grades:
            repeat = 1
            if random.random() < 0.15:
                repeat += 1

            for rep in range(repeat):
                since_date = date(current_year, 4, 1)
                until_date = date(current_year + 1, 3, 31)

                # 未来すぎる学年はスキップ
                if since_date > CUTOFF_DATE:
                    break  # これ以降の学年も未来なのでループ終了

                # 最後の学年で現役なら until_date = None
                if grade_enum == models.GradeEnum.M2 and rep == repeat - 1:
                    until_date = None
                else:
                    # CUTOFF_DATE を超えていたら調整
                    if until_date > CUTOFF_DATE:
                        until_date = None

                grade = models.MemberGrade(
                    person_id=person_id,
                    grade=grade_enum,
                    since_date=since_date,
                    until_date=until_date,
                )
                grades.append(grade)

                current_year += 1

    db.add_all(grades)
    db.commit()
