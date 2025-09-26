# Leagues API Schema

## GET /leagues

リーグ一覧を取得

**Request**

  Parameter     Type   Description            Required
  ------------- ------ ---------------------- ----------
  category_id   int    カテゴリIDでフィルタ   ❌

**Response**

``` json
{
    "status": "success",
    "data": [
        { "id": 1, "name": "東京都大学ソフトボール連盟", "category_id": 1, "category_name": "大学" },
        { "id": 2, "name": "関東社会人リーグ", "category_id": 2, "category_name": "社会人" }
    ]
}
```

------------------------------------------------------------------------

## GET /leagues/{league_id}

リーグ詳細を取得

**Request**

  Parameter   Type   Description   Required
  ----------- ------ ------------- ----------
  league_id   int    リーグID      ✅

**Response**

``` json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "東京都大学ソフトボール連盟",
        "category_id": 1,
        "category_name": "大学",
        "teams": [
            { "id": 1, "name": "東京大学" },
            { "id": 2, "name": "国士舘大学" }
        ]
    }
}
```

------------------------------------------------------------------------

## POST /leagues

新しいリーグを作成

**Request**

``` json
{
    "name": "新リーグ名",
    "category_id": 1
}
```

**Response**

``` json
{
    "status": "success",
    "data": { "id": 3, "name": "新リーグ名", "category_id": 1 }
}
```

------------------------------------------------------------------------

## PATCH /leagues/{league_id}

リーグ情報を更新

**Request**

``` json
{
  "name": "リーグ名変更"
}
```

**Response**

``` json
{
    "status": "success",
    "data": { "id": 3, "name": "リーグ名変更" }
}
```

------------------------------------------------------------------------

## DELETE /leagues/{league_id}

リーグを削除（論理削除推奨）

**Response**

``` json
{
    "status": "success",
    "data": null
}
```
