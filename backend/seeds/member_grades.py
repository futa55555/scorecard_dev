# backend/seeds/member_grades.py

from backend import models
from datetime import date, timedelta
import random

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

    for person_id in range(1, 101):  # 100人
        # 入学年をランダムに決定
        start_year = random.randint(2015, 2022)
        current_year = start_year

        for grade_enum in all_grades:
            # その学年を最低1年は必ずやる
            repeat = 1

            # 留年の確率（例: 15%）
            if random.random() < 0.15:
                repeat += 1

            for _ in range(repeat):
                since_date = date(current_year, 4, 1)
                until_date = date(current_year + 1, 3, 31)

                # 最後の学年の最後のレコードは until_date=None（現役）
                if grade_enum == models.GradeEnum.M2 and _ == repeat - 1:
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
