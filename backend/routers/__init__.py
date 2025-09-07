# backend/routers/__init__.py

from sqlalchemy.orm import Session
from backend import models
from backend.database import engine, SessionLocal
from datetime import date


def init_data():
    db: Session = SessionLocal()

    # 既にチームが存在する場合は何もしない（重複防止）
    if db.query(models.Team).first():
        db.close()
        return


    # チームの初期データ
    teams = [
        models.Team(
            name="東京大学",
            short_name="東大",
            is_myteam=True,
            prefecture="東京",
            league="東京都大学ソフトボール連盟",
            photo_url="https://example.com/",
            color="#4169e1"
        ),
        models.Team(
            name="早稲田大学",
            short_name="早稲田",
            prefecture="東京",
            league="東京都大学ソフトボール連盟",
            photo_url="https://example.com/",
            color="#9B003F"
        )
    ]
    db.add_all(teams)
    db.commit()


    # メンバー(Person)の初期データ
    people_Tokyo = [
        # 47期
        models.Person(
            name="逢坂拓征",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2020/osaka.JPG",
        ),
        
        # 48期
        models.Person(
            name="相川智",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2021/aikawa.JPG",
        ),
        models.Person(
            name="山川楓太",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        
        # 49期
        models.Person(
            name="島崎修一",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2022/shimasaki2.jpg",
        ),
        models.Person(
            name="名和大智",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/nawa.jpg",
        ),
        models.Person(
            name="藤川史帆",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2022/fujikawa.jpg",
        ),
        
        # 50期
        models.Person(
            name="大岡祥也",
            pitching_side="R",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/ohoka.jpg",
        ),
        models.Person(
            name="粕谷侑生",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/kasuya.jpg",
        ),
        models.Person(
            name="永井俊也",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/nagai.jpg",
        ),
        models.Person(
            name="原嶋雄大",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/harashima.jpg",
        ),
        models.Person(
            name="段塚泰",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/dantsuka.jpg",
        ),
        models.Person(
            name="鳥居希実",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/torii.jpg",
        ),
        
        # 51期
        models.Person(
            name="芦谷光太郎",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/asitani.jpg",
        ),
        models.Person(
            name="岩澤優希",
            pitching_side="R",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/iwasawa.jpg",
        ),
        models.Person(
            name="片岡照博",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/kataoka.jpg",
        ),
        models.Person(
            name="木戸潤正",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/kido.jpg",
        ),
        models.Person(
            name="多部田啓",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/tabeta.jpg",
        ),
        models.Person(
            name="寺田優作",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/terada.jpg",
        ),
        models.Person(
            name="中島陶冶",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/nakajima.jpg",
        ),
        models.Person(
            name="永山峻",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/nagayama.jpg",
        ),
        models.Person(
            name="水野瑛護",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="吉村友太",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/yoshimura.jpg",
        ),
        models.Person(
            name="岡本玲来",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="川名麻心",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="小林利央",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        
        # 52期
        models.Person(
            name="野村優空",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        )
    ]
    db.add_all(people_Tokyo)
    db.commit()
    
    # メンバー(Person)の初期データ
    people_Tokyo_copy = [
        # 47期
        models.Person(
            name="2逢坂拓征",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2020/osaka.JPG",
        ),
        
        # 48期
        models.Person(
            name="2相川智",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2021/aikawa.JPG",
        ),
        models.Person(
            name="2山川楓太",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        
        # 49期
        models.Person(
            name="2島崎修一",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2022/shimasaki2.jpg",
        ),
        models.Person(
            name="2名和大智",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/nawa.jpg",
        ),
        models.Person(
            name="2藤川史帆",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2022/fujikawa.jpg",
        ),
        
        # 50期
        models.Person(
            name="2大岡祥也",
            pitching_side="R",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/ohoka.jpg",
        ),
        models.Person(
            name="2粕谷侑生",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/kasuya.jpg",
        ),
        models.Person(
            name="2永井俊也",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/nagai.jpg",
        ),
        models.Person(
            name="2原嶋雄大",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/harashima.jpg",
        ),
        models.Person(
            name="2段塚泰",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/dantsuka.jpg",
        ),
        models.Person(
            name="2鳥居希実",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2023/torii.jpg",
        ),
        
        # 51期
        models.Person(
            name="2芦谷光太郎",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/asitani.jpg",
        ),
        models.Person(
            name="2岩澤優希",
            pitching_side="R",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/iwasawa.jpg",
        ),
        models.Person(
            name="2片岡照博",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/kataoka.jpg",
        ),
        models.Person(
            name="2木戸潤正",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/kido.jpg",
        ),
        models.Person(
            name="2多部田啓",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/tabeta.jpg",
        ),
        models.Person(
            name="2寺田優作",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/terada.jpg",
        ),
        models.Person(
            name="2中島陶冶",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/nakajima.jpg",
        ),
        models.Person(
            name="2永山峻",
            pitching_side="R",
            batting_side="R",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/nagayama.jpg",
        ),
        models.Person(
            name="2水野瑛護",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="2吉村友太",
            pitching_side="L",
            batting_side="L",
            photo_url="https://dp24045870.lolipop.jp/members/photo.html/2024/yoshimura.jpg",
        ),
        models.Person(
            name="2岡本玲来",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="2川名麻心",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        models.Person(
            name="2小林利央",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        ),
        
        # 52期
        models.Person(
            name="2野村優空",
            pitching_side="R",
            batting_side="R",
            photo_url="https://example.com/",
        )
    ]
    db.add_all(people_Tokyo_copy)
    db.commit()
    
    # people_Waseda = [
    #     models.Person(
    #         name="田中雄輔",
    #     ),
    #     models.Person(
    #         name="佐藤玲弥",
    #     ),
    #     models.Person(
    #         name="隄俊介",
    #     ),
    #     models.Person(
    #         name="髙篠翔和",
    #     ),
    #     models.Person(
    #         name="山本颯太",
    #     ),
    #     models.Person(
    #         name="鈴木寛汰朗",
    #     ),
    #     models.Person(
    #         name="野上夏輝",
    #     ),
    #     models.Person(
    #         name="福永隆稀",
    #     ),
    #     models.Person(
    #         name="金丸佳史",
    #     ),
    #     models.Person(
    #         name="武晃平",
    #     ),
    #     models.Person(
    #         name="間宮剛",
    #     ),
    #     models.Person(
    #         name="高木海征",
    #     ),
    #     models.Person(
    #         name="西村優汰",
    #     ),
    #     models.Person(
    #         name="齋藤拓哉",
    #     ),
    #     models.Person(
    #         name="加藤雅隆",
    #     ),
    #     models.Person(
    #         name="高岡信太郎",
    #     )
    # ]
    # db.add_all(people_Waseda)
    # db.commit()
    
    
    # メンバー(MemberProfile)の初期データ
    member_profiles_Tokyo = [
        # 47期
        # 逢坂(30)
        models.MemberProfile(
            person_id=1,
            team_id=1,
            since_date=date(2024, 6, 2),
            until_date=date(2025, 3, 31),
            uniform_number=30,
            role="coach",
        ),
        # 逢坂(31)
        models.MemberProfile(
            person_id=1,
            team_id=1,
            since_date=date(2025, 4, 1),
            uniform_number=31,
            role="coach",
        ),
        
        # 48期
        # 相川(31)
        models.MemberProfile(
            person_id=2,
            team_id=1,
            since_date=date(2024, 6, 2),
            until_date=date(2024, 10, 12),
            uniform_number=31,
            role="coach",
        ),
        # 山川
        models.MemberProfile(
            person_id=3,
            team_id=1,
            since_date=date(2021, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=5,
            role="player",
        ),
        
        # 49期
        # 島崎(17)
        models.MemberProfile(
            person_id=4,
            team_id=1,
            since_date=date(2022, 4, 1),
            until_date=date(2024, 6, 1),
            uniform_number=17,
            role="player",
        ),
        # 島崎(10)
        models.MemberProfile(
            person_id=4,
            team_id=1,
            since_date=date(2024, 6, 2),
            until_date=date(2025, 5, 11),
            uniform_number=10,
            role="player",
        ),
        # 名和(78)
        models.MemberProfile(
            person_id=5,
            team_id=1,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 3, 31),
            uniform_number=78,
            role="player",
        ),
        # 名和(78)
        models.MemberProfile(
            person_id=5,
            team_id=1,
            since_date=date(2025, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=30,
            role="player",
        ),
        # 藤川
        models.MemberProfile(
            person_id=6,
            team_id=1,
            since_date=date(2022, 4, 1),
            until_date=date(2024, 10, 12),
            uniform_number=20,
            role="manager"
        ),
        
        # 50期
        # 大岡(8)
        models.MemberProfile(
            person_id=7,
            team_id=1,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=8,
            role="player"
        ),
        # 大岡(30)
        models.MemberProfile(
            person_id=7,
            team_id=1,
            since_date=date(2025, 5, 12),
            uniform_number=30,
            role="player"
        ),
        # 粕谷
        models.MemberProfile(
            person_id=8,
            team_id=1,
            since_date=date(2023, 4, 1),
            uniform_number=48,
            role="player"
        ),
        # 永井
        models.MemberProfile(
            person_id=9,
            team_id=1,
            since_date=date(2023, 4, 1),
            uniform_number=21,
            role="player"
        ),
        # 原嶋(3)
        models.MemberProfile(
            person_id=10,
            team_id=1,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=3,
            role="player"
        ),
        # 原嶋(10)
        models.MemberProfile(
            person_id=10,
            team_id=1,
            since_date=date(2025, 5, 12),
            uniform_number=10,
            role="player"
        ),
        # 段塚
        models.MemberProfile(
            person_id=11,
            team_id=1,
            since_date=date(2023, 4, 1),
            uniform_number=19,
            role="manager"
        ),
        # 鳥居
        models.MemberProfile(
            person_id=12,
            team_id=1,
            since_date=date(2023, 4, 1),
            uniform_number=26,
            role="manager"
        ),
        
        # 51期
        # 芦谷
        models.MemberProfile(
            person_id=13,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=23,
            role="player"
        ),
        # 岩澤
        models.MemberProfile(
            person_id=14,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=12,
            role="player"
        ),
        # 片岡
        models.MemberProfile(
            person_id=15,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=9,
            role="player"
        ),
        # 木戸
        models.MemberProfile(
            person_id=16,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=61,
            role="player"
        ),
        # 多部田
        models.MemberProfile(
            person_id=17,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=28,
            role="player"
        ),
        # 寺田
        models.MemberProfile(
            person_id=18,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=2,
            role="player"
        ),
        # 中島
        models.MemberProfile(
            person_id=19,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=42,
            role="player"
        ),
        # 永山
        models.MemberProfile(
            person_id=20,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=51,
            role="player"
        ),
        # 水野
        models.MemberProfile(
            person_id=21,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=27,
            role="player"
        ),
        # 吉村
        models.MemberProfile(
            person_id=22,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=11,
            role="player"
        ),
        # 岡村
        models.MemberProfile(
            person_id=23,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=101,
            role="manager"
        ),
        # 川名
        models.MemberProfile(
            person_id=24,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=102,
            role="manager"
        ),
        # 小林
        models.MemberProfile(
            person_id=25,
            team_id=1,
            since_date=date(2024, 4, 1),
            uniform_number=103,
            role="manager"
        ),
        # 野村
        models.MemberProfile(
            person_id=26,
            team_id=1,
            since_date=date(2025, 4, 1),
            uniform_number=32,
            role="player"
        )
    ]
    db.add_all(member_profiles_Tokyo)
    db.commit()
    
    member_profiles_Tokyo_copy = [
        # 47期
        # 逢坂(30)
        models.MemberProfile(
            person_id=27,
            team_id=2,
            since_date=date(2024, 6, 2),
            until_date=date(2025, 3, 31),
            uniform_number=30,
            role="coach",
        ),
        # 逢坂(31)
        models.MemberProfile(
            person_id=27,
            team_id=2,
            since_date=date(2025, 4, 1),
            uniform_number=31,
            role="coach",
        ),
        
        # 48期
        # 相川(31)
        models.MemberProfile(
            person_id=28,
            team_id=2,
            since_date=date(2024, 6, 2),
            until_date=date(2024, 10, 12),
            uniform_number=31,
            role="coach",
        ),
        # 山川
        models.MemberProfile(
            person_id=29,
            team_id=2,
            since_date=date(2021, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=5,
            role="player",
        ),
        
        # 49期
        # 島崎(17)
        models.MemberProfile(
            person_id=30,
            team_id=2,
            since_date=date(2022, 4, 1),
            until_date=date(2024, 6, 1),
            uniform_number=17,
            role="player",
        ),
        # 島崎(10)
        models.MemberProfile(
            person_id=30,
            team_id=2,
            since_date=date(2024, 6, 2),
            until_date=date(2025, 5, 11),
            uniform_number=10,
            role="player",
        ),
        # 名和(78)
        models.MemberProfile(
            person_id=31,
            team_id=2,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 3, 31),
            uniform_number=78,
            role="player",
        ),
        # 名和(78)
        models.MemberProfile(
            person_id=31,
            team_id=2,
            since_date=date(2025, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=30,
            role="player",
        ),
        # 藤川
        models.MemberProfile(
            person_id=32,
            team_id=2,
            since_date=date(2022, 4, 1),
            until_date=date(2024, 10, 12),
            uniform_number=20,
            role="manager"
        ),
        
        # 50期
        # 大岡(8)
        models.MemberProfile(
            person_id=33,
            team_id=2,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=8,
            role="player"
        ),
        # 大岡(30)
        models.MemberProfile(
            person_id=33,
            team_id=2,
            since_date=date(2025, 5, 12),
            uniform_number=30,
            role="player"
        ),
        # 粕谷
        models.MemberProfile(
            person_id=34,
            team_id=2,
            since_date=date(2023, 4, 1),
            uniform_number=48,
            role="player"
        ),
        # 永井
        models.MemberProfile(
            person_id=35,
            team_id=2,
            since_date=date(2023, 4, 1),
            uniform_number=21,
            role="player"
        ),
        # 原嶋(3)
        models.MemberProfile(
            person_id=36,
            team_id=2,
            since_date=date(2023, 4, 1),
            until_date=date(2025, 5, 11),
            uniform_number=3,
            role="player"
        ),
        # 原嶋(10)
        models.MemberProfile(
            person_id=36,
            team_id=2,
            since_date=date(2025, 5, 12),
            uniform_number=10,
            role="player"
        ),
        # 段塚
        models.MemberProfile(
            person_id=37,
            team_id=2,
            since_date=date(2023, 4, 1),
            uniform_number=19,
            role="manager"
        ),
        # 鳥居
        models.MemberProfile(
            person_id=38,
            team_id=2,
            since_date=date(2023, 4, 1),
            uniform_number=26,
            role="manager"
        ),
        
        # 51期
        # 芦谷
        models.MemberProfile(
            person_id=39,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=23,
            role="player"
        ),
        # 岩澤
        models.MemberProfile(
            person_id=40,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=12,
            role="player"
        ),
        # 片岡
        models.MemberProfile(
            person_id=41,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=9,
            role="player"
        ),
        # 木戸
        models.MemberProfile(
            person_id=42,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=61,
            role="player"
        ),
        # 多部田
        models.MemberProfile(
            person_id=43,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=28,
            role="player"
        ),
        # 寺田
        models.MemberProfile(
            person_id=44,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=2,
            role="player"
        ),
        # 中島
        models.MemberProfile(
            person_id=45,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=42,
            role="player"
        ),
        # 永山
        models.MemberProfile(
            person_id=46,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=51,
            role="player"
        ),
        # 水野
        models.MemberProfile(
            person_id=47,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=27,
            role="player"
        ),
        # 吉村
        models.MemberProfile(
            person_id=48,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=11,
            role="player"
        ),
        # 岡村
        models.MemberProfile(
            person_id=49,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=101,
            role="manager"
        ),
        # 川名
        models.MemberProfile(
            person_id=50,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=102,
            role="manager"
        ),
        # 小林
        models.MemberProfile(
            person_id=51,
            team_id=2,
            since_date=date(2024, 4, 1),
            uniform_number=103,
            role="manager"
        ),
        # 野村
        models.MemberProfile(
            person_id=52,
            team_id=2,
            since_date=date(2025, 4, 1),
            uniform_number=32,
            role="player"
        )
    ]
    db.add_all(member_profiles_Tokyo_copy)
    db.commit()


    # 試合の初期データ
    game = models.Game(
        id=1,
        top_team_id=1,
        bottom_team_id=2,
        date=date.today(),
        status=models.GameStatusEnum.ongoing
    )
    db.add(game)
    db.commit()
    
    
    # 試合の登録選手
    game_members_1 = [
        models.GameMember(
            game_id=1,
            team_id=1,
            person_id=i,
            starting_batting_order=i,
            starting_position=i
        ) for i in range(1, 10)
    ] + [
        models.GameMember(
            game_id=1,
            team_id=1,
            person_id=i,
            starting_batting_order=0,
            starting_position=0
        ) for i in range(10, 20)
    ] + [
        models.GameMember(
            game_id=1,
            team_id=2,
            person_id=i,
            starting_batting_order=i-19,
            starting_position=i-19
        ) for i in range(20, 29)
    ] + [
        models.GameMember(
            game_id=1,
            team_id=2,
            person_id=i,
            starting_batting_order=0,
            starting_position=0
        ) for i in range(29, 39)
    ]
    db.add_all(game_members_1)
    db.commit()

    db.close()
    