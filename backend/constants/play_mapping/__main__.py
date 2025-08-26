# check_and_search_rules.py
# 目的:
# 1) YAMLを読み込んで中身をざっと確認する (confirm_rules)
# 2) position / batted_ball_type / runner_state / outs で候補検索する (search_candidates)

from typing import Any, Dict, List, Optional, Sequence, Union
from pprint import pprint
import yaml


# =========
# 0) YAML読み込み
# =========
def load_rules(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        raise ValueError("Top-level YAML must be a list of rules.")
    return data


# =========
# 1) 簡単確認関数
# =========
def confirm_rules(rules: List[Dict[str, Any]], *, show_first: int = 1) -> None:
    """
    ルール件数と、先頭N件の key/candidates ラベルを軽く出すだけの確認関数
    """
    print(f"# of rules: {len(rules)}")

    # 各ルールのkeyサマリ
    print("\n== Rule keys summary ==")
    for idx, r in enumerate(rules[:show_first]):
        k = r.get("key", {})
        positions = k.get("position", [])
        bbt = k.get("batted_ball_type", [])
        print(f"[{idx}] position={positions}, batted_ball_type={bbt}")

    # ラベル一覧（先頭N件分の候補のみ）
    print("\n== Candidate labels (first rule(s)) ==")
    for idx, r in enumerate(rules[:show_first]):
        for c in r.get("candidates", []) or []:
            label = c.get("label") or c.get("lable")  # typoフォールバック
            print(f"[rule {idx}] {label}")


# =========
# 2) ランナー状態のパターンマッチ (xはワイルドカード)
# =========
def to_runner_string(runner_state: Union[str, Sequence[int]]) -> str:
    """
    '1xx' のような3文字 or (1,0,1) / [1,0,1] を '101' に正規化
    """
    if isinstance(runner_state, str):
        s = runner_state.strip()
        if len(s) != 3 or any(ch not in "10x" for ch in s):
            raise ValueError("runner_state string must be length-3 and use only '1','0','x'.")
        return s
    if isinstance(runner_state, (tuple, list)) and len(runner_state) == 3:
        return "".join("1" if int(v) else "0" for v in runner_state)
    raise ValueError("runner_state must be a length-3 string ('1/0/x') or a 3-length tuple/list of 0/1.")


def runner_pattern_match(pattern: Optional[str], current: Optional[Union[str, Sequence[int]]]) -> bool:
    """
    pattern: YAML側 (例 '1xx' / 'x1x' / None)
    current: 現在 (例 '101' / (1,0,1) / None)
    """
    if pattern is None:
        return True
    if current is None:
        return False

    pat = to_runner_string(pattern)
    cur = to_runner_string(current)  # '1'/'0'のみ

    for pch, cch in zip(pat, cur):
        if pch == "x":
            continue
        if pch != cch:
            return False
    return True


# =========
# 3) outsフィルタ (YAMLの out_condition をサポート)
# =========
def outs_match(out_condition: Optional[int], current_outs: Optional[int]) -> bool:
    if isinstance(out_condition, int):
        if out_condition >= current_outs:
            return True
    else:
        return True
    return False


# =========
# 4) 検索本体
# =========
def search_candidates(
    rules: List[Dict[str, Any]],
    *,
    position: str,
    batted_ball_type: str,
    runner_state: Optional[Union[str, Sequence[int]]] = None,
    outs: Optional[int] = None,
) -> List[Dict[str, Any]]:
    print("\n{0}, {1}, runner_state={2}, outs={3} ==".format(
        position, batted_ball_type, runner_state, outs
    ))

    
    pos = position.strip()
    bbt = batted_ball_type.strip()
    matched: List[Dict[str, Any]] = []

    for rule in rules:
        key = rule.get("key", {})
        positions = key.get("position", [])
        bbt_list = key.get("batted_ball_type", [])

        if pos not in positions:
            continue
        if bbt not in bbt_list:
            continue

        for cand in rule.get("candidates", []) or []:
            if "label" not in cand and "lable" in cand:
                cand["label"] = cand["lable"]

            if not runner_pattern_match(cand.get("runner_condition"), runner_state):
                continue
            if not outs_match(cand.get("out_condition"), outs):
                continue
            matched.append(cand)

    return matched


def print_adv(adv: Dict[str, Any], runner_state: Optional[Union[str, Sequence[int]]] = None):
    fielding_sequence = adv['fielding_sequence']
    print("fielding_sequence: {0}".format(fielding_sequence))
    
    print("advances:")
    advances = adv['advances']
    for a in advances:
        runner = a.get('runners')
        out_type = a.get('out_type')
        step = a.get('step')
        
        for r in runner:
            if r == 0 or runner_state[r - 1] == 1:
                if out_type:
                    print("  - runner: {0}, out_type: {1}".format(r, out_type))
                if step:
                    print("  - runner: {0}, step: {1}".format(r, step))
                


# =========
# 5) お試し実行
# =========
if __name__ == "__main__":
    rules = load_rules("backend/constants/play_mapping/main_suggestion.yml")
    
    print("########################################################################")
    print("########################################################################")
    print("########################################################################")

    for outs in [0, 1, 2]:
        for runner_state in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]:
            res = search_candidates(
                rules,
                position="TB",
                batted_ball_type="ground",
                runner_state=runner_state,
                outs=outs,
            )
            for c in res:
                events = c.get("events")
                print(c['label'])
                for event in events:
                    print_adv(event, runner_state)
                print()
