# backend/seeds/person_profiles.py

import json
from datetime import date

from backend import models


def seed_person_profiles(db):
    with open("backend/seeds/data/person_profiles.json", "r", encoding="utf-8") as f:
        person_profile_data = json.load(f)

    person_profiles = [
        models.PersonProfile(
            person_profile_id=person_profile["person_profile_id"],
            person_id=person_profile["person_id"],
            team_id=person_profile["team_id"],
            since_date=date.fromisoformat(person_profile["since_date"]),
            until_date=date.fromisoformat(person_profile["until_date"]) if person_profile["until_date"] else None,
            uniform_number=person_profile["uniform_number"],
            role=models.RoleEnum[person_profile["role"]]
        )
        for person_profile in person_profile_data
    ]

    db.add_all(person_profiles)
    db.commit()
