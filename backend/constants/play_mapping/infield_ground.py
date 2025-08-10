# backend/constants/play_mapping/infield_ground.py

# ------------------------
# 内野ゴロ
# ------------------------

play_mapping_infield_ground = {}

positions_infield = [1, 2, 3, 4, 5, 6]  # 内野

for pos in positions_infield:
    # ゴロ正面・捕球成功
    key = (pos, 0, 0, 0)  # (ポジション, 方向, ゴロ, 捕った)
    play_mapping_infield_ground[key] = [
        {
            "play": f"{pos}ゴロ1塁アウト",
            "initial_runners": "1xx",
            "outs": 0,
            "expected_advances": [
                (0, 1, "batter_id", False),
            ]
        },
        {
            "play": f"{pos}ゴロ2塁封殺",
            "initial_runners": "1xx",
            "outs": 0,
            "expected_advances": [
                (1, 2, f"{pos}-4FO", False),
            ]
        },
        {
            "play": f"{pos}ゴロダブルプレー",
            "initial_runners": "1xx",
            "outs": 0,
            "expected_advances": [
                (0, 1, "batter_id", False),
                (1, 2, f"{pos}-4-3DP", False),
            ]
        },
    ]

    # ゴロ正面・エラー
    key_error = (pos, 0, 0, 1)
    play_mapping_infield_ground[key_error] = [
        {
            "play": f"内野安打（{pos}方向）",
            "initial_runners": "xxx",
            "outs": 0,
            "expected_advances": [
                (0, 1, "batter_id", True),
            ]
        },
    ]

# print(f"Total plays: {len(play_mapping_infield_ground)}")
# for k, v in list(play_mapping_infield_ground.items())[:5]:
#     print(k, v)
