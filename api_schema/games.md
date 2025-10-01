# Games API Schema

## GET /games

Get all games.  
Filter can be applied with optional parameters.

### Request

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | Category ID | ❌ |
| league_id | int | League ID | ❌ |
| tournament_id | int | Tournament ID | ❌ |
| team_id | int | Team ID | ❌ |

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
                    },
                    "score": {
                        "top_team": 2,
                        "bottom_team": 4,
                    },
                    "status": "ongoing"
                },
                {
                    ...
                }
            ]
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

## GET /games/{game_id}/detail

Get detailed information of a specific game.

### Response

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
