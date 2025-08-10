from . import play_mapping

def find_candidates(key, runner_state, outs):
    """
    key: (position_id, direction_id, ball_type_id, play_result_id)
    runner_state: 文字列 '1x0' のように1=ランナー有,0=無,x=ワイルドカード
    outs: int (0,1,2)
    """
    candidates = []

    if key not in play_mapping:
        return candidates

    for play in play_mapping[key]:
        init_runners = play["initial_runners"]
        # アウト数を入れた場合、play に "outs" を追加するのも良い
        if all(
            r == 'x' or r == s
            for r, s in zip(init_runners, runner_state)
        ):
            candidates.append(play)

    return candidates

# デバッグ用
if __name__ == "__main__":
    key = (6, 0, 0, 0)  # 遊ゴロ正面捕球
    print(find_candidates(key, "100", 0))
