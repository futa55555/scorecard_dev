# Game Records API Schema

## GET /game_records/{game_record_id}/common

試合記録の共通情報を取得

**Response**

```json
{
    "status": "sccess",
    "data": {
        "game_record_id": 1,
        "user_id": 1,
        "start_time": "15:06:10",
		"end_time": "17:34:59"
    }
}
```

------------------------------------------------------------------------

## GET /game_records/{game_record_id}/scoreboard

試合記録の得点板を取得

**Response**

```json
{
    "status": "success",
    "data": {
        "top_team": {
            "team_id": 2,
            "short_name": "早稲田",
            "innings": [0, 0, 1, 1, 0],
            "total": {
                "run": 2,
                "hit": 5,
                "error": 1
            }
        },
        "bottom_team": {
            "team_id": 5,
            "short_name": "立教",
            "innings": [0, 2, 0, 1],
            "total": {
                "run": 3,
                "hit": 6,
                "error": 0
            }
        }
    }
}
```

------------------------------------------------------------------------

## GET /game_records/{game_record_id}/starting_members

試合記録のスタメンを取得

**Response**

```json
{
    "status": "success",
    "data": {
        "top_team": {
            "team_id": 2,
            "short_name": "早稲田",
            "starting_members": [
                {
                    "order": "1番",
                    "position": "ライト",
                    "person": {
                        "person_id": 1,
                        "last_name": "石井",
                        "first_name": "徹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ]
        },
        "bottom_team": {
            "team_id": 5,
            "short_name": "立教",
            "starting_members": [
                {
                    "order": "1番",
                    "position": "ライト",
                    "person": {
                        "person_id": 2,
                        "last_name": "佐藤",
                        "first_name": "直樹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ]
        }
    }
}
```

------------------------------------------------------------------------

## GET /game_records/{game_record_id}/bench_members

試合記録の控え選手を取得

**Response**

```json
{
    "status": "success",
    "data": {
        "top_team": {
            "team_id": 2,
            "short_name": "早稲田",
            "bench_members": [
                {
                    "person": {
                        "person_id": 1,
                        "last_name": "石井",
                        "first_name": "徹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ]
        },
        "bottom_team": {
            "team_id": 5,
            "short_name": "立教",
            "bench_members": [
                {
                    "person": {
                        "person_id": 2,
                        "last_name": "佐藤",
                        "first_name": "直樹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ]
        }
    }
}
```

------------------------------------------------------------------------

## GET /game_records/{game_record_id}/progress

試合記録の経過情報を取得

**Response**

```json
{
    "status": "success",
    "data": [
        {
            "game_event_id": 1,
            "substitution_events": [
                {
                    "substitution_event_id": 1,
                    "out_member_id": 1,
                    "in_member_id": 2
                },
                {
                    ...
                }
            ],
            "pitch_event": {
                "pitch_event_id": 1,
                "batter_id": 1,
                "pitch_event_type": "strike",
            },
            "advance_events": [
                {
                    "advance_event_id": 1,
                    "runner_id": 1,
                    "to_base": 4,
                    "out_type": "safe"
                },
                {
                    ...
                }
            ],
            "defence_players": {
                "before_game_event": [
                    {
                        "position": "投手",
                        "person": {
                            "person_id": 1,
                            "last_name": "石井",
                            "first_name": "徹",
                            "middle_name": ""
                        }
                    },
                    {
                        ...
                    }
                ],
                "after_game_event": [
                    {
                        "position": "投手",
                        "person": {
                            "person_id": 1,
                            "last_name": "石井",
                            "first_name": "徹",
                            "middle_name": ""
                        }
                    },
                    {
                        ...
                    }
                ]
            },
            "offence_players": {
                "before_game_event": {
                    "batter": {
                        "order": "1番",
                        "person": {
                            "person_id": 1,
                            "last_name": "石井",
                            "first_name": "徹",
                            "middle_name": ""
                        }
                    },
                    "runners": [
                        {
                            "base": 1,
                            "person": {
                                "person_id": 1,
                                "last_name": "石井",
                                "first_name": "徹",
                                "middle_name": ""
                            }
                        },
                        {
                            ...
                        }
                    ]
                }
            }
        },
        {
            ...
        }
    ]
}
```

------------------------------------------------------------------------

## GET /game_records/{game_record_id}/situation

試合記録の最新の状況を取得

**Response**

```json
{
    "status": "success",
    "data": {
        "ball_count": {
            "balls": 3,
            "strike": 1,
            "outs": 2
        },
        "defence_players": {
            "before_game_event": [
                {
                    "position": "投手",
                    "person": {
                        "person_id": 1,
                        "last_name": "石井",
                        "first_name": "徹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ],
            "after_game_event": [
                {
                    "position": "投手",
                    "person": {
                        "person_id": 1,
                        "last_name": "石井",
                        "first_name": "徹",
                        "middle_name": ""
                    }
                },
                {
                    ...
                }
            ]
        },
        "offence_players": {
            "before_game_event": {
                "batter": {
                    "order": "1番",
                    "person": {
                        "person_id": 1,
                        "last_name": "石井",
                        "first_name": "徹",
                        "middle_name": ""
                    }
                },
                "runners": [
                    {
                        "base": 1,
                        "person": {
                            "person_id": 1,
                            "last_name": "石井",
                            "first_name": "徹",
                            "middle_name": ""
                        }
                    },
                    {
                        ...
                    }
                ]
            }
        }
    }
}
```

------------------------------------------------------------------------

## POST /game_records

新しい試合記録を作成

**Request**

```json
{
    "game_id": 1,
    "user_id": 2
}
```

**Response**

```json
{
    "status": "success",
    "data": {
        "game_record_id": 1
    }
}
```

------------------------------------------------------------------------

## PATCH /game_records

既存の試合記録を更新

**Request**

```json
{
    "game_id": 2,
}
```

**Response**

```json
{
    "status": "success",
    "data": {
        "game_record_id": 1,
        "game_id": 2
    }
}
```

------------------------------------------------------------------------

## DELETE /game_records

試合記録を削除

**Request**

```json
{
    "game_id": 1
}
```

**Response**

```json
{
    "status": "success",
    "data": null
}
```
