# backend/constants/play_mapping/outfield_ground.py

# ------------------------
# 外野ゴロ（単打想定）
# ------------------------

play_mapping_outfield_ground = {}

positions_outfield = [7, 8, 9]

for pos in positions_outfield:
    # ゴロ処理（単打）
    key = (pos, 0, 0, 0)
    play_mapping_outfield_ground[key] = [
        {
            "play": f"{pos}前ヒット",
            "initial_runners": "xxx",
            "outs": 0,
            "expected_advances": [
                (0, 1, "batter_id", True)
            ]
        }
    ]

# print(f"Total plays: {len(play_mapping_outfield_ground)}")
# for k, v in list(play_mapping_outfield_ground.items())[:5]:
#     print(k, v)
