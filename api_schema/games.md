# Games API Schema

## GET /games

試合一覧を取得

**Request**

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| tournament_id | int | 大会ID | ❌ |
| team_id | int | チームID | ❌ |

**Response**

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
                    },
                    "score": {
                        "top_team": 2,
                        "bottom_team": 4,
                    },
                    "status": "試合中"
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

## GET /games/{game_id}/detail

試合の詳細情報を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "game_id": 1,
        "tournament": {
            "tournament_id": 2,
            "name": "2025年秋季リーグ"
        },
        "top_team": {
            "team_id": 2,
            "name": "早稲田大学男子ソフトボール部",
            "short_name": "早稲田"
        },
        "bottom_team": {
            "team_id": 5,
            "name": "立教大学ソフトボール部",
            "short_name": "立教"
        },
        "date": "2025-10-19",
        "start_time": "15:00:00",
        "location": "大類ソフトボールパーク",
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
    }
}
```

------------------------------------------------------------------------

## POST /games

試合を新規作成

**Request**

``` json
{
    "tournament_id": 3,
    "top_team_id": 16,
    "bottom_team_id": 23,
    "date": "2025-10-31",
    "start_time": "11:00:00",
    "end_time": "13:00:00",
    "location": "掛川市いこいの広場野球場",
    "status": "draft"
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "game_id": 101
    }
}
```

------------------------------------------------------------------------

## PATCH /games/{game_id}

試合情報を更新

**Request**

``` json
{
  "location": "サーティーフォー保土ケ谷球場",
  "status": "ongoing"
}
```

**Response**

``` json
{
  "status": "success",
  "data": {
    "id": 101,
    "location": "サーティーフォー保土ケ谷球場",
    "status": "進行中"
  }
}
```

------------------------------------------------------------------------

## DELETE /games/{game_id}

試合を削除

**Response**

``` json
{
  "status": "success",
  "data": null
}
```
