# Teams API Schema

## GET /teams

Get all teams.

### Response

``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 1,
            "name": "東京大学ソフトボール部",
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
    ],
    "message": "Teams fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /teams/{team_id}/detail

Get detailed information of a specific team.

### Response

``` json
{
    "status": "success",
    "data": {
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
        "photo_url": "https://example.com/team_1.png",
        "color": "#2681eaff"
    },
    "message": "Game information fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## PATCH /teams/{team_id}

Update information of a specific team.

### Request

``` json
{
    "admin_user_id": 12
}
```

### Response

``` json
{
    "status": "success",
    "data": {
        "team_id": 27,
        "admin_user_id": 12
    },
    "message": "Team information updated successfully",
    "code": null
}
```
