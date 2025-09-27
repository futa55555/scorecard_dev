# Tournaments API Schema

## GET /tournaments

大会一覧を取得

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
            "tournament_id": 1,
            "name": "2025年春季リーグ",
            "since_date": "2025-04-01",
            "until_date": "2025-05-31"
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /tournaments/{tournament_id}

大会詳細を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "tournament_id": 1,
        "name": "2025年春季リーグ",
        "since_date": "2025-04-01",
        "until_date": "2025-05-31",
    }
}
```

------------------------------------------------------------------------

## POST /tournaments

新しい大会を作成

**Request**

``` json
{
    "name": "2026年春季リーグ",
    "since_date": "2026-04-01",
    "until_date": "2026-05-31"
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "tournament_id": 4
    }
}
```

------------------------------------------------------------------------

## PATCH /tournaments/{tournament_id}

大会情報を更新

**Request**

``` json
{
    "until_date": "2026-06-10"
}
```

**Response**

``` json
{
    "status": "success",
    "data": {
        "tournament_id": 4
    }
}
```

------------------------------------------------------------------------

## DELETE /tournaments/{tournament_id}

大会を削除

**Response**

``` json
{
    "status": "success",
    "data": null
}
```
