# Common API Schema

## 共通レスポンス形式

### 成功
``` json
{
    "status": "success",
    "data": { ... },
    "message": "User created successfully",
    "code": null
}
```

### 失敗
```json
{
    "status": "error",
    "data": null,
    "message": "Invalid username or password",
    "code": "VALIDATION_ERROR"
}
```

-   `status`: API呼び出しの結果
-   `data`: 成功時の返却データ
-   `message`: 詳細メッセージやコード（開発者向け）
-   `code`: エラーコード（機械向け）

------------------------------------------------------------------------

## 共通スキーマ

あれば追加

（例）
### Team Schema

| Field | Type | Description |
| ----- | ---- | ----------- |
| id | int | チームID |
| name | str | チーム名 |
| member_count | int | メンバー人数 |

------------------------------------------------------------------------

## エラーコード例

| Code | Description |
| ---- | ----------- |
| `NOT_FOUND` | データが存在しない |
| `VALIDATION_ERROR` | 入力データ不正 |
| `UNAUTHORIZED` | 認証が必要 |
| `FORBIDDEN` | 権限不足 |
