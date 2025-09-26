# Tournaments API Schema

## GET /tournaments

大会一覧を取得

**Request**

  Parameter     Type   Description            Required
  ------------- ------ ---------------------- ----------
  category_id   int    カテゴリID   ❌
  year          int    開催年       ❌

**Response**

``` json
{
    "status": "success",
    "data": [
        { "id": 1, "name": "春季リーグ戦", "category_id": 1, "start_date": "2025-04-01", "end_date": "2025-06-01" }
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
        "id": 1,
        "name": "春季リーグ戦",
        "category_id": 1,
        "start_date": "2025-04-01",
        "end_date": "2025-06-01",
        "teams": [
            { "id": 1, "name": "東京大学" },
            { "id": 2, "name": "国士舘大学" }
        ]
    }
}
```

------------------------------------------------------------------------

## POST /tournaments

新しい大会を作成

**Request**

``` json
{
    "name": "秋季リーグ戦",
    "category_id": 1,
    "start_date": "2025-09-01",
    "end_date": "2025-11-01"
}
```

**Response**

``` json
{
    "status": "success",
    "data": { "id": 2, "name": "秋季リーグ戦" }
}
```

------------------------------------------------------------------------

## PATCH /tournaments/{tournament_id}

大会情報を更新

**Request**

``` json
{
    "name": "大会名変更",
    "end_date": "2025-11-10"
}
```

**Response**

``` json
{
    "status": "success",
    "data": { "id": 2, "name": "大会名変更", "end_date": "2025-11-10" }
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
