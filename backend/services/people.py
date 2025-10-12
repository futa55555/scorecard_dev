# backend/services/people.py

from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from backend import schemas, cruds

def get_person_list(
    db: Session,
    category_id: int | None = None,
    league_id: int | None = None
) -> list[schemas.PersonListItem]:
    """
    メンバー一覧を取得
    """
    person_list = cruds.get_person_list(db, category_id, league_id)

    # ✅ ここでPersonListItemを再構築（依存を含めて再解決）
    schemas.PersonListItem.model_rebuild(force=True)

    adapter = TypeAdapter(list[schemas.PersonListItem])
    return adapter.validate_python(person_list)


def get_person_list_with_page(
    db: Session,
    current_page: int,
    limit: int,
    category_id: int | None = None,
    league_id: int | None = None
) -> schemas.PersonListWithPage:
    """
    ページ付きのメンバー一覧を取得
    """
    person_list, person_total_count = cruds.get_person_list_with_page(db, current_page, limit, category_id, league_id)

    # ✅ ここでPersonListItemを再構築（依存を含めて再解決）
    schemas.PersonListItem.model_rebuild(force=True)

    adapter = TypeAdapter(list[schemas.PersonListItem])
    people = adapter.validate_python(person_list)

    return schemas.PersonListWithPage(
        people=people,
        current_page=current_page,
        total_page=(person_total_count // limit) + 1
    )


def get_person_detail(
    db: Session,
    person_id: int
) -> schemas.PersonDetail:
    """
    メンバーの詳細情報を取得
    """
    person_detail = cruds.get_person_detail(db, person_id)

    adapter = TypeAdapter(schemas.PersonDetail)
    return adapter.validate_python(person_detail)
