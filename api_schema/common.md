# Common API Schema

## 共通レスポンス形式

``` json
{
    "status": "success",   // or "error"
    "data": { ... },       // 成功時のデータ
    "error": null          // 失敗時のみエラーメッセージ
}
```

-   `status`: API呼び出しの結果
-   `data`: 成功時の返却データ
-   `error`: 失敗時のエラー内容（詳細メッセージやコード）

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
