# backend/schemas/person.py

from pydantic import BaseModel, ConfigDict
from backend import models
from . import common, user, person_profile, player_position

class PersonBase(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    middle_name: str | None = None
    prefecture: models.PrefectureEnum

    model_config = ConfigDict(from_attributes=True)


class PersonListItem(PersonBase):
    person_profiles: list[person_profile.PersonProfileListItem]
    player_positions: list[player_position.PlayerPositionListItem]

    model_config = ConfigDict(from_attributes=True)


class PersonListResponse(common.CommonResponse[list[PersonListItem]]):
    pass


class PersonDetail(PersonBase):
    created_by_user: user.UserBase
    person_profiles: list[person_profile.PersonProfileListItem]
    player_positions: list[player_position.PlayerPositionListItem]
    own_user: user.UserBase

    model_config = ConfigDict(from_attributes=True)


class PersonDetailResponse(common.CommonResponse[PersonDetail]):
    pass
