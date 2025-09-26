# People API Schema

## GET /people/{team_id}

チームに所属する人物一覧を取得

**Response**

``` json
{
    "status": "success",
    "data": [
        {
            "person_id": 1,
            "last_name": "石井",
            "first_name": "徹",
            "middle_name": "",
            "uniform_number": 66,
            "role": "選手"
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /people/{person_id}

特定の人物詳細を取得

**Response**

``` json
{
    "status": "success",
    "data": {
        "person_id": 1,
        "last_name": "石井",
        "first_name": "徹",
        "middle_name": "",
        "gender": "男",
        "height_cm": 161,
        "weight_kg": 93,
        "birthday": "2006-09-03",
        "prefecture": "北海道",
        "pitching_side": "右投",
        "batting_side": "右打",
        "photo_url": "https://example.com/people/001.png"
    }
}
```

------------------------------------------------------------------------

## POST /people

新しい人物を作成

**Request**

``` json
{
    "last_name": "新庄",
	"first_name": "剛志",
	"middle_name": "",
    "gender": "male",
	"height_cm": 181,
	"weight_kg": 76,
	"birthday": "2002-01-28",
    "prefecture": "Nagasaki",
	"pitching_side": "right",
	"batting_side": "right",
    "photo_url": "https://example.com/perople/601.png"
}
```

**Response**

``` json
{
	"status": "success",
	"data": {
		"person_id": 601
	}
}
```

------------------------------------------------------------------------

## PATCH /people/{person_id}

既存人物のプロフィールを更新

**Request**

``` json
{
    "last_name": "BIG",
	"first_name": "BOSS"
}
```

**Response**

``` json
{
	"status": "success",
	"data": {
		"person_id": 601,
		"last_name": "BIG",
		"first_name": "BOSS"
	}
}
```

------------------------------------------------------------------------

## DELETE /people/{person_id}

人物を削除

**Response**

``` json
{
	"status": "success",
	"data": null
}
```
