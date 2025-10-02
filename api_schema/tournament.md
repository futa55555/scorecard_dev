# Tournament API Schema

## GET /tournaments

大会一覧を取得。  
カテゴリー、リーグ、チーム、お気に入りでフィルター可。

### Request

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| team_id | int | チームID | ❌ |
| favorite | bool | true, false | ❌ |

### Response
**成功**
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

## GET /tournaments/{tournament_id}

大会詳細を取得。

### Response
**成功**
``` json
{
    "status": "success",
    "data": {
        "tournament_id": 1,
        "name": "2025年春季リーグ",
        "since_date": "2025-04-01",
        "until_date": "2025-05-31",
        "games": [
            {
                "game_id": 1,
                "date": "2025-04-08",
                "top_team": {
                    "team_id": 1,
                    "name": "東京大学ソフトボール部"
                },
                "bottom_team": {
                    "team_id": 2,
                    "name": "早稲田大学男子ソフトボール部"
                }
            },
            {
                ...
            }
        ],
        "categories": [
            {
                "category_id": 1,
                "name": "大学男子"
            },
            {
                ...
            }
        ],
        "teams": [
            {
                "team_id": 1,
                "name": "東京大学ソフトボール部"
            },
            {
                ...
            }
        ],
        "locations": [
            {
                "location_id": 1,
                "name": "東京大学駒場キャンパス野球場"
            },
            {
                ...
            }
        ]
    }
}
```

------------------------------------------------------------------------

## POST /tournaments

新しい大会を作成

### Request

``` json
{
    "name": "2026年春季リーグ",
    "since_date": "2026-04-01",
    "until_date": "2026-05-31"
}
```

### Response

``` json
{
    "status": "success",
    "data": {
        "tournament_id": 4
    }
}
```

------------------------------------------------------------------------

## PATCH /tournaments/{tournament_id}

大会情報を更新

### Request

``` json
{
    "until_date": "2026-06-10"
}
```

### Response

``` json
{
    "status": "success",
    "data": {
        "tournament_id": 4
    }
}
```

------------------------------------------------------------------------

## DELETE /tournaments/{tournament_id}

大会を削除

### Response

``` json
{
    "status": "success",
    "data": null
}
```
