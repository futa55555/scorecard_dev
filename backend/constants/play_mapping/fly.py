# backend/constants/play_mapping/fly.py

# ------------------------
# フライ
# ------------------------

play_mapping_fly = {}

positions_infield = [1, 2, 3, 4, 5, 6]
positions_outfield = [7, 8, 9]

for pos in positions_outfield:
    # フライ処理
    key = (pos, 0, 0, 0)
    play_mapping_fly[key] = [
        {
            "play": f"{pos}前ヒット",
            "initial_runners": "xxx",
            "outs": 0,
            "expected_advances": [
                (0, 1, "batter_id", True)
            ]
        }
    ]

# print(f"Total plays: {len(play_mapping_fly)}")
# for k, v in list(play_mapping_fly.items())[:5]:
#     print(k, v)
