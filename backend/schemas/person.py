# backend/schemas/person.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import common, user, person_profile, player_position

class PersonSummary(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    middle_name: str

    model_config = ConfigDict(from_attributes=True)


class PersonItem(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    middle_name: str
    prefecture: models.PrefectureEnum
    created_by_user: user.UserSummary
    person_profile: person_profile.PersonProfileItem
    player_position: player_position.PlayerPositionItem
    own_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)


class PersonList(list[PersonItem]):
    pass


class PersonListResponse(common.CommonResponse[PersonList]):
    pass


class PersonDetail(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    middle_name: str
    prefecture: models.PrefectureEnum
    created_by_user: user.UserSummary
    person_profiles: list[person_profile.PersonProfileItem]
    player_positions: list[player_position.PlayerPositionItem]
    own_user: user.UserSummary

    model_config = ConfigDict(from_attributes=True)


class PersonDetailResponse(common.CommonResponse[PersonDetail]):
    pass
