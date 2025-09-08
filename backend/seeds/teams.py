# backend/seeds/teams.py

from backend import models

def seed_teams(db):
    teams = [
        models.Team(
            name = "東京大学ソフトボール部",
            short_name = "東大",
            is_myteam = True,
            is_favorite = True,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/tokyo_daigaku_m.png",
            color = "#5377EF"
        ),
        models.Team(
            name = "早稲田大学男子ソフトボール部",
            short_name = "早大",
            is_myteam = False,
            is_favorite = True,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/waseda_daigaku_m.png",
            color = "#6E0C0C"
        ),
        models.Team(
            name = "慶應義塾大学ソフトボール部",
            short_name = "慶應",
            is_myteam = False,
            is_favorite = False,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/keio_daigaku_m.png",
            color = "#1A2B5F"
        ),
        models.Team(
            name = "立教大学ソフトボール部",
            short_name = "立教",
            is_myteam = False,
            is_favorite = False,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/rikkyo_daigaku_m.png",
            color = "#22003A"
        ),
        models.Team(
            name = "明治大学ソフトボール部",
            short_name = "明治",
            is_myteam = False,
            is_favorite = False,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/meiji_daigaku_m.png",
            color = "#641775"
        ),
        models.Team(
            name = "学習院大学ソフトボール部",
            short_name = "学習",
            is_myteam = False,
            is_favorite = False,
            prefecture = models.PrefectureEnum.Tokyo,
            league = "東京都大学ソフトボール連盟",
            photo_url = "https://example.com/gakusyu_daigaku_m.png",
            color = "#5E5E5E"
        )
    ]
    db.add_all(teams)
    db.commit()
