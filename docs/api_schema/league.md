# League API Schema

## GET /leagues

リーグ一覧を取得。  
フィルター用で、最低限の情報のみ。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |

### Response
**成功**
``` json
{
    "status": "success",
    "data": [
        {
            "league_id": 1,
            "name": "東京都大学ソフトボール連盟"
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /leagues/{league_id}

リーグの詳細情報を取得。
管理者、所属チーム、カテゴリーも合わせて取得。

### Response
**成功**
``` json
{
    "status": "success",
    "data": {
        "league_id": 1,
        "name": "東京都大学ソフトボール連盟",
        "chief_admin_user": {
            "user_id": 1,
            "name": "aoi_takahashi"
        },
        "teams": [
            {
                "team_id": 1,
                "name": "東京大学ソフトボール部",
                "prefecture": "東京"
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
            },
        ]
    }
}
```

------------------------------------------------------------------------

## PATCH /leagues/{league_id}

リーグの情報を一部更新

### Request
``` json
{
    "name": "関西大学ソフトボール連盟"
}
```

### Response
**成功**
``` json
{
    "status": "success",
    "data": {
        "league_id": 3
    },
    "message": "League updated successfully",
    "code": null
}
```
