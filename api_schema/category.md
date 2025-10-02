# Category API Schema

## GET /categories

カテゴリー一覧を取得。  

- `/categories`
フィルター用で、最低限の情報のみ。  

- `/categories?include=leagues`
所属するリーグ一覧も取得。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| include | str | none, leagues | ❌ |

### Response
**成功（`/categories`）**
``` json
{
    "status": "success",
    "data": [
        {
            "category_id": 1,
            "name": "大学男子"
        },
        {
            ...
        }
    ]
}
```

**成功（`/categories?include=leagues`）**
``` json
{
    "status": "success",
    "data": [
        {
            "category_id": 1,
            "name": "大学男子",
            "leagues": [
                {
                    "league_id": 1,
                    "name": "東京都大学ソフトボール連盟"
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

## GET /categories/{category_id}

カテゴリー詳細を取得。
属するリーグ一覧、各リーグに所属するチーム一覧、無所属のチーム一覧も取得。

### Response

``` json
{
    "status": "success",
    "data": {
        "category_id": 1,
        "name": "大学男子",
        "leagues": [
            {
                "league_id": 1,
                "name": "東京都大学ソフトボール連盟",
                "teams": [
                    {
                        "team_id": 1,
                        "name": "東京大学ソフトボール部",
                        "prefecture": "東京"
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
        "unaffiliated_teams": [
            {
                "team_id": 2,
                "name": "新チーム",
                "prefecture": "東京"
            },
            {
                ...
            }
        ]
    }
}
```

------------------------------------------------------------------------

## POST /categories

カテゴリーを新規作成

### Request

```json
{
    "name": "大学女子"
}
```

### Response

```json
{
    "status": "success",
    "data": {
        "category_id": 3
    }
}
```

------------------------------------------------------------------------

## PATCH /categories/{category_id}

カテゴリー情報を更新

### Request

```json
{
    "name": "高校女子"
}
```

### Response

```json
{
    "status": "success",
    "data": {
        "category_id": 3
    }
}
```

------------------------------------------------------------------------

## DELETE /categories/{category_id}

カテゴリーを削除

### Response

```json
{
    "status": "success",
    "data": null
}
```
