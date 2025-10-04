# backend/tests/cruds/test_tournaments.py

from datetime import date
from backend import models
from backend.cruds import tournaments as crud


def test_list_tournaments_filter_by_category(db_session):
    """
    カテゴリーでフィルターできることを確認
    """
    # --- Arrange ---
    user = models.User(user_id=1, name="tester", password="testtest")  # created_by_user_id が必要
    cat1 = models.Category(category_id=1, name="大学")
    cat2 = models.Category(category_id=2, name="社会人")

    t1 = models.Tournament(
        tournament_id=1,
        name="大学選手権",
        since_date=date(2025, 4, 1),
        until_date=date(2025, 4, 10),
        is_official=True,
        created_by_user_id=1
    )
    t2 = models.Tournament(
        tournament_id=2,
        name="社会人大会",
        since_date=date(2025, 5, 1),
        until_date=date(2025, 5, 10),
        is_official=False,
        created_by_user_id=1
    )

    # 多対多リレーション設定
    t1.categories.append(cat1)
    t2.categories.append(cat2)

    db_session.add_all([user, cat1, cat2, t1, t2])
    db_session.commit()

    # --- Act ---
    result = crud.list_tournaments(db=db_session, category_id=1)

    # --- Assert ---
    assert len(result) == 1
    assert result[0].name == "大学選手権"


def test_get_tournament_with_relations(db_session):
    """
    大会詳細がリレーションを含めて取得できることを確認
    """
    user = models.User(user_id=1, name="creator", password="testtest")
    cat = models.Category(category_id=1, name="高校")
    league = models.League(league_id=1, name="東日本リーグ")
    loc = models.Location(
        location_id=1,
        name="東京ドーム",
        prefecture="Tokyo",
        created_by_user_id=1
    )
    t = models.Tournament(
        tournament_id=10,
        name="春季大会",
        since_date=date(2025, 3, 20),
        until_date=date(2025, 3, 30),
        is_official=True,
        created_by_user_id=1
    )

    # 関連づけ
    t.categories.append(cat)
    t.leagues.append(league)
    t.locations.append(loc)

    db_session.add_all([user, cat, league, loc, t])
    db_session.commit()

    # --- Act ---
    result = crud.get_tournament(db=db_session, tournament_id=10)

    # --- Assert ---
    assert result is not None
    assert result.name == "春季大会"
    assert result.categories[0].name == "高校"
    assert result.leagues[0].name == "東日本リーグ"
    assert result.locations[0].name == "東京ドーム"
