# backend/seeds/people.py

import json
from backend import models


def seed_people(db):
    with open("./data/people.json", "r", encoding="utf-8") as f:
        person_data = json.load(f)

    people = [
        models.Person(
            person_id=person["person_id"],
            last_name=person["last_name"],
            first_name=person["first_name"],
            middle_name=person["middle_name"],
            prefecture=models.PrefectureEnum[person["prefecture"]],
            is_official=person["is_official"],
            created_by_user_id=person["created_by_user_id"]
        )
        for person in person_data
    ]

    db.add_all(people)
    db.commit()
