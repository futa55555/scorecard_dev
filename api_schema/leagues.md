# Leagues API Schema

## GET /leagues

リーグ一覧を取得

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
            "league_id": 1,
            "name": "東京都大学ソフトボール連盟",
            "category_id": 1
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /leagues/{league_id}

リーグ詳細を取得

**Request**

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| league_id | int | リーグID | ✅ |

**Response**

``` json
{
    "status": "success",
    "data": {
        "league_id": 1,
        "name": "東京都大学ソフトボール連盟",
        "category_id": 1
    }
}
```

------------------------------------------------------------------------

## POST /leagues

新しいリーグを作成

**Request**

``` json
{
    "name": "関東大学ソフトボール連盟",
    "category_id": 1
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "league_id": 3
    }
}
```

------------------------------------------------------------------------

## PATCH /leagues/{league_id}

リーグ情報を更新

**Request**

``` json
{
    "name": "関西大学ソフトボール連盟"
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "league_id": 3
    }
}
```

------------------------------------------------------------------------

## DELETE /leagues/{league_id}

リーグを削除

**Response**

``` json
{
    "status": "success",
    "data": null
}
```
