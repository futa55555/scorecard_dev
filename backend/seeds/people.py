# backend/seeds/people.py

import json

from backend import models


def seed_people(db):
    with open("backend/seeds/data/people.json", "r", encoding="utf-8") as f:
        person_data = json.load(f)

    people = [
        models.Person(
            person_id=person["person_id"],
            last_name=person["last_name"],
            first_name=person["first_name"],
            middle_name=person["middle_name"],
            gender=models.GenderEnum[person["gender"]],
            height_cm=person["height_cm"],
            weight_kg=person["weight_kg"],
            birthday=person["birthday"],
            prefecture=models.PrefectureEnum[person["prefecture"]],
            pitching_side=models.DominantHandEnum[person["pitching_side"]],
            batting_side=models.DominantHandEnum[person["batting_side"]],
            photo_url=person["photo_url"]
        )
        for person in person_data
    ]

    db.add_all(people)
    db.commit()
