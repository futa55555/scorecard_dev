# Auth API Schema

## POST /signup

Sign up.

### Request

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| username | str | ユーザー名 | ✅ |
| password | str | パスワード | ✅ |

### Response

**Success**
```json
{
    "status": "success",
    "data": null,
    "msg": "User created successfully"
}
```

------------------------------------------------------------------------

## POST /login

Log in.

### Request

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| username | str | ユーザー名 | ✅ |
| password | str | パスワード | ✅ |

### Response

```json
{
    "status": "success",
    "data": {
        "access_token": "sample_token",
        "token_type": "bearer"
    },
    "msg": "Logged in successfully"
}
```

------------------------------------------------------------------------

## POST /logout

Log out.

### Request

| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| token | str | 認証トークン | ✅ |

### Response

```json
{
    "status": "success",
    "data": null,
    "msg": "Logged out successfully"
}
```


------------------------------------------------------------------------
