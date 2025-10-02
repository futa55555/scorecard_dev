# Location API Schema

## GET /locations

試合会場一覧を取得。
都道府県でフィルター可。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| prefecture | str | 都道府県名 | ❌ |

### Response
**成功**
```json
{
    "status": "success",
    "data": [
        {
            "location_id": 1,
            "name": "東京大学駒場キャンパス野球場",
            "prefecture": "東京"
        },
        {
            ...
        }
    ],
    "message": "Locations fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /locations/{location_id}

試合会場の詳細情報を取得。
将来的に口コミなども追加予定。

### Response
**成功**
```json
{
    "status": "success",
    "data": {
        "location_id": 1,
        "name": "東京大学駒場キャンパス野球場",
        "prefecture": "東京",
        "created_by_user": "aoi_takahashi"
    }
}
```
