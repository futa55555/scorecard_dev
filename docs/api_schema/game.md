# Game API Schema

## GET /games

試合一覧を取得。  
チーム、会場、大会も合わせて取得。
カテゴリー、リーグ、大会、チーム、お気に入りでフィルター可。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| tournament_id | int | 大会ID | ❌ |
| team_id | int | チームID | ❌ |
| user_id | int | ユーザーID | ❌ |

### Response
**成功**
``` json
{
    "status": "success",
    "data": [
        {
            "game_id": 1,
            "date": "2025-04-08",
            "start_time": "12:00:00",
            "top_team": {
                "team_id": 1,
                "name": "東京大学ソフトボール部"
            },
            "bottom_team": {
                "team_id": 2,
                "name": "早稲田大学男子ソフトボール部"
            },
            "location": {
                "location_id": 1,
                "name": "東京大学駒場キャンパス野球場"
            },
            "tournament": {
                "tournament_id": 1,
                "name": "2025年春季リーグ"
            }
        },
        {
            ...
        }
    ],
    "message": "Games fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /games/{game_id}

試合の詳細情報を取得。
チーム、会場、大会、作成者も合わせて取得。

### Response
**成功**
``` json
{
    "status": "success",
    "data": {
        "game_id": 1,
        "date": "2025-04-08",
        "start_time": "12:00:00",
        "top_team": {
            "team_id": 1,
            "name": "東京大学ソフトボール部"
        },
        "bottom_team": {
            "team_id": 2,
            "name": "早稲田大学男子ソフトボール部"
        },
        "location": {
            "location_id": 1,
            "name": "東京大学駒場キャンパス野球場"
        },
        "tournament": {
            "tournament_id": 1,
            "name": "2025年春季リーグ"
        },
        "created_by_user": {
            "user_id": 1,
            "name": "aoi_takahashi"
        }
    },
    "message": "Game information fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## POST /games

Create a new game.

### Request

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

### Response

``` json
{
    "status": "success",
    "data": {
        "game_id": 101
    },
    "message": "Game Created successfully",
    "code": null
}
```

------------------------------------------------------------------------

## PATCH /games/{game_id}

Update information of a specific game.

### Request

``` json
{
    "location": "サーティーフォー保土ケ谷球場",
    "status": "ongoing"
}
```

### Response

``` json
{
    "status": "success",
    "data": {
        "game_id": 101,
        "location": "サーティーフォー保土ケ谷球場",
        "status": "ongoing"
    },
    "message": "Game updated successfully",
    "code": null
}
```

------------------------------------------------------------------------

## DELETE /games/{game_id}

Delete a specific game.

### Response

``` json
{
    "status": "success",
    "data": null,
    "message": "Game deleted successfully",
    "code": null
}
```
