# backend/services/people.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_person_list(
    db: Session
) -> schemas.PersonList:
    """

    """


def get_person_detail(
    db: Session,
    person_id: int
) -> schemas.PersonDetail:
    """

    """
