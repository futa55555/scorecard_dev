# backend/services/games.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_game_list(
    db: Session
) -> schemas.GameList:
    """

    """


def get_game_detail(
    db: Session,
    game_id: int
) -> schemas.GameDetail:
    """

    """
