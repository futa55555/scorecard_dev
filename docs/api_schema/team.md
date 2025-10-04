# Team API Schema

## GET /teams

チーム一覧を取得。  
カテゴリー、カテゴリーも合わせて取得。  
カテゴリー、リーグ、都道府県、お気に入りでフィルター可。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| prefecture | str | 都道府県 | ❌ |
| user_id | int | ユーザーID | ❌ |

### Response
**成功**
``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 1,
            "name": "東京大学ソフトボール部",
            "prefecture": "東京",
            "league": {
                "league_id": 1,
                "name": "東京都大学ソフトボール連盟"
            },
            "categories": [
                {
                    "category_id": 1,
                    "name": "大学男子"
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
    "message": "Teams fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /teams/{team_id}

チームの詳細情報を取得。
カテゴリー、リーグ、管理者、人物一覧、試合一覧も合わせて取得。

### Response

``` json
{
    "status": "success",
    "data": {
        "team_id": 1,
        "name": "東京大学ソフトボール部",
        "short_name": "東大",
        "prefecture": "東京",
        "chief_admin_user": {
            "user_id": 1,
            "name": "aoi_takahashi"
        },
        "league": {
            "league_id": 1,
            "name": "東京都大学ソフトボール連盟"
        },
        "categories": [
            {
                "category_id": 1,
                "name": "大学男子"
            },
            {
                ...
            }
        ],
        "person_profiles": [
            {
                "person_profile_id": 1,
                "uniform_number": 1,
                "role": "投手",
                "person": {
                    "person_id": 1,
                    "last_name": "石田",
                    "first_name": "徹",
                    "middle_name": null
                }
            },
            {
                ...
            }
        ],
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
        "admin_users": [
            {
                "user_id": 2,
                "name": "shiori_kaneko"
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
    },
    "message": "Team information fetched successfully",
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
