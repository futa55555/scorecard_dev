# Favorites API Schema

## GET /favorites/games

お気に入りのチームによる試合一覧を取得

### Response

``` json
{
    "status": "success",
    "data": [
        {
            "game_id": 1,
            "tournament": {
                "tournament_id": 2,
                "name": "2025年秋季リーグ"
            },
            "top_team": {
                "team_id": 2,
                "short_name": "早稲田"
            },
            "bottom_team": {
                "team_id": 5,
                "short_name": "立教"
            },
            "date": "2025-10-19",
            "game_records": [
                {
                    "game_record_id": 1,
                    "user": {
                        "user_id": 1,
                        "name": "aoi_ishikawa"
                    }
                },
                {
                    ...
                }
            ]
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /favorites/teams

お気に入りのチーム一覧を取得

### Response

``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 1,
            "name": "東京大学ソフトボール部",
            "short_name": "東大",
            "category": {
                "category_id": 1,
                "name": "大学男子"
            },
            "league": {
                "league_id": 1,
                "name": "東京都大学ソフトボール連盟"
            },
            "prefecture": "東京",
            "color": "#2681eaff"
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /favorites/tournaments

お気に入りの大会一覧を取得

### Response

``` json
{
    "status": "success",
    "data": [
        {
            "tournament_id": 1,
            "name": "2025年春季リーグ",
            "since_date": "2025-04-01",
		    "until_date": "2025-05-31"
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /favorites/people

お気に入りの人物一覧を取得

### Response

```json
{
    "status": "success",
    "data": [
        {
            "person_id": 1,
            "last_name": "石井",
            "first_name": "徹",
            "middle_name": "",
            "team": {
                "team_id": 1,
                "name": "東京大学ソフトボール部"
            }
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## POST /favorites//{_id}

新しいをお気に入りに登録

### Request

```json
{
    "user_id": 1,
    "
}
```

### Response

```json
{
    "status": "success",
    "data": {

    }
}
```
