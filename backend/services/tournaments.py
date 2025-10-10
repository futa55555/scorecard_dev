# backend/services/tournaments.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_tournament_list(
    db: Session,
    category_id: int | None = None
) -> list[schemas.TournamentListItem]:
    """
    大会一覧を取得
    """
    tournament_list = cruds.get_tournament_list(db, category_id)

    adapter = TypeAdapter(list[schemas.TournamentListItem])
    return adapter.validate_python(tournament_list)
