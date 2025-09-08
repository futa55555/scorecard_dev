# backend/seeds/people.py

from backend import models
from datetime import date
import random

def seed_people(db):
    people = []

    surnames = ["山田", "佐藤", "鈴木", "高橋", "伊藤", "小林", "加藤", "吉田", "中村", "渡辺",
                "松本", "井上", "木村", "林", "清水", "山本", "石川", "森", "池田", "橋本"]
    given_names = ["太郎", "一郎", "健太", "翔", "優斗", "大輔", "直樹", "拓海", "陽介", "和也",
                   "誠", "真司", "悠真", "亮", "徹", "翔太", "遼", "健司", "弘樹", "淳"]
    foreign_names = [
        "John Smith", "Carlos González", "Mike Johnson", "David Brown", "Alex Wilson",
        "Chris Taylor", "Robert Davis", "Daniel Martinez", "Kevin White", "Thomas Anderson"
    ]

    prefectures = list(models.PrefectureEnum)
    pitching_sides = list(models.DominantHandEnum)
    batting_sides = list(models.DominantHandEnum)

    for i in range(1, 101):
        # 1割くらいは外国人名
        if i % 10 == 0:
            name = random.choice(foreign_names)
        else:
            name = random.choice(surnames) + " " + random.choice(given_names)

        person = models.Person(
            name=name,
            pitching_side=random.choice(pitching_sides),
            batting_side=random.choice(batting_sides),
            photo_url=f"https://example.com/players/player{i:03d}.png",
            height_cm=random.randint(160, 190),
            weight_kg=random.randint(55, 95),
            birthday=date(
                random.randint(1995, 2006),   # 年
                random.randint(1, 12),        # 月
                random.randint(1, 28)         # 日
            ),
            prefecture=random.choice(prefectures)
        )
        people.append(person)

    db.add_all(people)
    db.commit()