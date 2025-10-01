# People API Schema

------------------------------------------------------------------------

## GET /teams/{team_id}/active_people

Get active people of a specific team.

### Response

``` json
{
    "status": "success",
    "data": {
        "team_id": 1,
        "active_people": [
            {
                "person_id": 1,
                "last_name": "石井",
                "first_name": "徹",
                "middle_name": "",
                "person_profiles": [
                    {
                        "person_profile_id": 2,
                        "since_date": "2023-01-26",
                        "until_date": null,
                        "uniform_number": 66,
                        "role": "選手"
                    },
                    {
                        ...
                    }
                ]
            },
            {
                ...
            }
        ]
    },
    "message": "People fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## GET /people/{person_id}

Get detailed information of a specific person.

### Response

``` json
{
    "status": "success",
    "data": {
        "person_id": 1,
        "last_name": "石井",
        "first_name": "徹",
        "middle_name": "",
        "gender": "男性",
        "height_cm": 161,
        "weight_kg": 93,
        "birthday": "2006-09-03",
        "prefecture": "北海道",
        "pitching_side": "右投",
        "batting_side": "右打",
        "photo_url": "https://example.com/people/001.png"
    },
    "message": "Person information fetched successfully",
    "code": null
}
```

------------------------------------------------------------------------

## POST /people

Create a new person.

### Request

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

### Response

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

Update information of a specific person.

### Request

``` json
{
    "last_name": "BIG",
	"first_name": "BOSS"
}
```

### Response

``` json
{
	"status": "success",
	"data": {
		"person_id": 601,
		"last_name": "BIG",
		"first_name": "BOSS"
	},
    "message": "Person information updated successfully",
    "code": null
}
```

------------------------------------------------------------------------

## DELETE /people/{person_id}

Delete a specific person.

### Response

``` json
{
	"status": "success",
	"data": null,
    "message": "Person deleted successfully",
    "code": null
}
```
