# backend/services/games.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_game_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[schemas.GameListItem]:
    """
    試合一覧を取得
    """
    game_list = cruds.get_game_list(db, category_id, league_id)

    adapter = TypeAdapter(list[schemas.GameListItem])
    return adapter.validate_python(game_list)


def get_game_detail(
    db: Session,
    game_id: int
) -> schemas.GameDetail:
    """
    試合の詳細情報を取得
    """
    game_detail = cruds.get_game_detail(db, game_id)

    adapter = TypeAdapter(schemas.GameDetail)
    return adapter.validate_python(game_detail)
