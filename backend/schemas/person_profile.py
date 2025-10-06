# backend/schemas/person_profile.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import user, team, person
from datetime import date

class PersonProfileItem(BaseModel):
    person_profile_id: int
    uniform_number: int
    role: models.RoleEnum
    since_date: date
    until_date: date
    person: person.PersonSummary
    team: team.TeamSummary
    created_by_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)
