# Person API Schema

## GET /people

人物一覧を取得。  
カテゴリー、リーグ、チーム、出身都道府県、ポジション、お気に入りでフィルター可。  
現在の所属チームと背番号、役割とポジションを合わせて取得。

### Request
| Parameter | Type | Description | Required |
| --------- | ---- | ----------- | -------- |
| category_id | int | カテゴリーID | ❌ |
| league_id | int | リーグID | ❌ |
| team_id | int | チームID | ❌ |
| prefecture | str | 出身都道府県 | ❌ |
| position_type | str | ポジション区分 | ❌ |
| user_id | int | ユーザーID | ❌ |

### Response
**成功**
``` json
{
    "status": "success",
    "data": [
        {
            "person_id": 1,
            "last_name": "石井",
            "first_name": "徹",
            "middle_name": null,
            "prefecture": "東京",
            "person_profile": [
                {
                    "uniform_number": 66,
                    "role": "選手",
                    "since_date": "2021-05-03",
                    "until_date": null
                    "team": {
                        "name": "東京大学ソフトボール部"
                    }
                },
                {
                    ...
                }
            ],
            "player_position": [
                {
                    "position_type": "投手",
                    "since_date": "2021-05-03",
                    "until_date": null
                },
                {
                    ...
                }
            ]
        },
        {
            ...
        }
    ],
    "message": "People fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /people/{person_id}

人物の詳細情報を取得。  
過去のチーム遍歴やポジションの変遷も合わせて取得。

### Response
**成功**
``` json
{
    "status": "success",
    "data": {
        "person_id": 1,
        "last_name": "石井",
        "first_name": "徹",
        "middle_name": null,
        "prefecture": "北海道",
        "person_profiles": [
            {
                "uniform_number": 16,
                "role": "選手",
                "since_date": "2021-05-03",
                "until_date": "2023-04-01",
                "team": {
                    "team_id": 1,
                    "name": "東京大学ソフトボール部"
                },
                "created_by_user": {
                    "name": "aoi_takahashi"
                }
            },
            {
                ...
            }
        ],
        "player_positions": [
            {
                "position_type": "投手",
                "since_date": "2021-05-03",
                "until_date": null
            },
            {
                ...
            }
        ]
    },
    "message": "Person information fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## POST /people

新規の人物を作成。

### Request
``` json
{
    "last_name": "新庄",
	"first_name": "剛志",
	"middle_name": "",
    "prefecture": "Nagasaki"
}
```

### Response
**成功**
``` json
{
	"status": "success",
	"data": {
		"person_id": 601
	},
    "message": "Person created successfully",
    "code": null
}
```

------------------------------------------------------------------------

## PATCH /people/{person_id}

人物の情報を一部更新。

### Request
``` json
{
    "last_name": "BIG",
	"first_name": "BOSS"
}
```

### Response
**成功**
``` json
{
	"status": "success",
	"data": {
		"person_id": 601,
	},
    "message": "Person information updated successfully",
    "code": null
}
```
