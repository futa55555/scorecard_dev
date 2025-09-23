# backend/seeds/teams.py

from backend import models

def seed_teams(db):
    teams = [
        models.Team(
            name = "東京大学ソフトボール部",
            short_name = "東大",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/tokyo_daigaku_m.png",
            color = "#5377EF",
            admin_user_id = 1
        ),
        models.Team(
            name = "早稲田大学男子ソフトボール部",
            short_name = "早大",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/waseda_daigaku_m.png",
            color = "#6E0C0C",
            admin_user_id = 1
        ),
        models.Team(
            name = "慶應義塾大学ソフトボール部",
            short_name = "慶應",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/keio_daigaku_m.png",
            color = "#1A2B5F",
            admin_user_id = 1
        ),
        models.Team(
            name = "立教大学ソフトボール部",
            short_name = "立教",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/rikkyo_daigaku_m.png",
            color = "#22003A",
            admin_user_id = 1
        ),
        models.Team(
            name = "明治大学ソフトボール部",
            short_name = "明治",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/meiji_daigaku_m.png",
            color = "#641775",
            admin_user_id = 1
        ),
        models.Team(
            name = "学習院大学ソフトボール部",
            short_name = "学習",
            category_id = 1,
            league_id = 1,
            prefecture = models.PrefectureEnum.Tokyo,
            photo_url = "https://example.com/gakusyu_daigaku_m.png",
            color = "#5E5E5E",
            admin_user_id = 1
        )
    ]
    db.add_all(teams)
    db.commit()
