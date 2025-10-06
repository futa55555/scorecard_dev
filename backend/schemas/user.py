# backend/schemas/user.py

from pydantic import BaseModel, ConfigDict

class UserSummary(BaseModel):
    user_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
