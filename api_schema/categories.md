# Categories API Schema

## GET /categories

カテゴリ一覧を取得

**Response**

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

------------------------------------------------------------------------

## GET /categories/{category_id}

カテゴリー詳細を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "category_id": 1,
        "name": "大学男子",
    }
}
```

------------------------------------------------------------------------

## POST /categories

カテゴリーを新規作成

**Request**

```json
{
    "name": "大学女子"
}
```

**Response**

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

**Request**

```json
{
    "name": "高校女子"
}
```

**Response**

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

**Response**

```json
{
    "status": "success",
    "data": null
}
```
