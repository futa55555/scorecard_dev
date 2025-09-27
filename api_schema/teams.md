# Teams API Schema

## GET /teams

特定のカテゴリーのチーム一覧を取得

**Request**

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| tournament_id | int | 大会ID | ❌ |

**Response**

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
    ]
}
```

------------------------------------------------------------------------

## GET /teams/{team_id}/detail

チームの詳細情報を取得

**Response**

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
    }
}
```

------------------------------------------------------------------------

## GET /teams/{team_id}/active_people

チームの現役の所属人物を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "team_id": 1,
        "active_people": [
            {
                "person_id": 1,
                "last_name": "石井",
                "first_name": "徹",
                "middle_name": "",
                "person_profiles": [
                    {
                        "person_profile_id": 2,
                        "since_date": "2023-01-26",
                        "until_date": null,
                        "uniform_number": 66,
                        "role": "選手"
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
}
```

------------------------------------------------------------------------

## GET /teams/{team_id}/retired_people

チームの過去の所属人物を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "team_id": 1,
        "retired_people": [
            {
                "person_id": 12,
                "last_name": "後藤",
                "first_name": "優斗",
                "middle_name": "",
                "person_profiles": [
                    {
                        "person_profile_id": 23,
                        "since_date": "2024-05-20",
                        "until_date": "2024-10-12",
                        "uniform_number":94,
                        "role": "選手"
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
}
```

------------------------------------------------------------------------

## POST /teams

新しいチームを作成

**Request**

``` json
{
    "name": "日本大学ソフトボール部",
    "short_name": "日大",
    "category_id": 1,
    "league_id": 1,
    "prefecture": "Tokyo",
    "photo_url": "https://example.com/new_team.png",
    "color": "#cb4cb0ff",
    "admin_user_id": 11
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "team_id": 27
    }
}
```

------------------------------------------------------------------------

## PATCH /teams/{team_id}

既存チームの情報を更新

**Request**

``` json
{
    "admin_user_id": 12
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "team_id": 27,
        "admin_user_id": 12
    }
}
```

------------------------------------------------------------------------

## DELETE /teams/{team_id}

チームを削除

**Response**

``` json
{
    "status": "success",
    "data": null
}
```
