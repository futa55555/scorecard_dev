# Team API Schema

## GET /teams

特定のカテゴリーのチーム一覧を取得

**Request**

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |

**Response**

``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 1,
            "name": "東京大学ソフトボール部",
            "short_name": "東大",
            "league": "東京都大学ソフトボール連盟",
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

## GET /teams/{user_id}/favorite

お気に入りのチーム一覧を取得

**Response**

``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 1,
            "name": "東京大学ソフトボール部",
            "short_name": "東大",
            "category": "大学男子",
            "league": "東京都大学ソフトボール連盟",
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

## GET /teams/{team_id}

特定のチーム詳細を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "team_id": 1,
        "name": "東京大学ソフトボール部",
        "short_name": "東大",
        "category": "大学男子",
        "league": "東京都大学ソフトボール連盟",
        "prefecture": "東京",
        "photo_url": "https://example.com/team_1.png",
        "color": "#2681eaff"
    }
}
```

------------------------------------------------------------------------

## GET /teams/{person_id}

所属したチームを取得

**Response**

``` json
{
    "status": "success",
    "data": [
        {
            "team_id": 8,
            "since_date": "2021-10-13",
            "until_date": "2023-01-25",
            "uniform_number": 37,
            "role": "選手"
        },
        {
            ...
        }
    ]
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
