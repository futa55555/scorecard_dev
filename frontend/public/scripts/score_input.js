// frontend/public/scripts/score_input.js

const urlParams = new URLSearchParams(window.location.search);
const gameId = urlParams.get("game_id");
const confirmWalkButton = document.getElementById("confirmWalkButton");
const advanceModal = document.getElementById("advanceModal");
const advanceChoices = document.getElementById("advanceChoices");
const advanceForm = document.getElementById("advanceForm");

function fetchAtBats() {
    fetch(`/api/games/${gameId}/all_atbats`)
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById("atbat-list");
            ul.innerHTML = "";

            // --- ゲーム状況の表示 ---
            const stateDiv = document.getElementById("game-state");
            if (stateDiv && data.state) {
                const st = data.state;
                stateDiv.textContent =
                    `アウト:${st.outs}  カウント:${st.balls}-${st.strikes}  ` +
                    `ランナー:${st.runners_str}`;
            }

            // --- 打席一覧の描画 ---
            data.atbats.forEach(atbat => {
                const li = document.createElement("li");
                li.innerHTML = `
                    ${atbat.id}番
                    ${atbat.inning}回${atbat.top_bottom === "top" ? "表" : "裏"}
                    #${atbat.batter_id}
                    ${atbat.result || ""}
                `;

                const pitchUl = document.createElement("ul");

                if (atbat.pitch_events && atbat.pitch_events.length > 0) {
                    atbat.pitch_events.forEach(pitch => {
                        const pitchLi = document.createElement("li");
                        pitchLi.innerHTML = `
                            ${pitch.id}球目
                            ${pitch.description || "不明"}
                        `;

                        if (pitch.advance_events && pitch.advance_events.length > 0) {
                            const advUl = document.createElement("ul");
                            pitch.advance_events.forEach(adv => {
                                const advLi = document.createElement("li");
                                advLi.textContent =
                                    `runner#${adv.runner_id}: ` +
                                    `${adv.from_base || 0}塁→${adv.to_base || 0}塁 ` +
                                    `${adv.is_out ? "アウト" : ""}`;
                                advUl.appendChild(advLi);
                            });
                            pitchLi.appendChild(advUl);
                        }

                        pitchUl.appendChild(pitchLi);
                    });
                }

                li.appendChild(pitchUl);
                ul.appendChild(li);
            });
        });
}

// --- 投球フォーム送信処理 ---
document.getElementById("scoreInput").addEventListener("submit", async function (e) {
    e.preventDefault();
    const description = document.getElementById("description").value;

    await submitPitch(description);
});

// --- 共通投球送信処理 ---
async function submitPitch(description) {
    const res = await fetch(`/api/score-input/${gameId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
    });

    const data = await res.json();
    console.log("サーバー返答:", data);

    if (!res.ok) {
        alert("登録失敗: " + (data.detail || "不明なエラー"));
        return;
    }

    document.getElementById("description").value = "ball"; // 初期化

    // --- pitch_event_id を保存 ---
    latestPitchEventId = data.pitch_event_id;

    // --- requires_advance が true の場合のみモーダル表示 ---
    if (data.requires_confirmation && data.advance_candidates && data.advance_candidates.length > 0) {
        // pitch_id をグローバルに保持（confirm用）
        window.latestPitchId = data.pitch_id;
        showAdvanceModal(data.advance_candidates);
    } else {
        fetchAtBats(); // 進塁不要なら即一覧更新
    }
}

// --- 進塁候補モーダルを表示 ---
function showAdvanceModal(candidates) {
    advanceChoices.innerHTML = "";

    candidates.forEach(c => {
        const div = document.createElement("div");
        div.style.marginBottom = "10px";

        // 候補内容を文字列にまとめる
        const lines = c.advances.map(a => {
            const outTxt = a.is_out ? "アウト" : "";
            return `runner#${a.runner_id} ${a.from_base}塁→${a.to_base}塁 ${outTxt}`;
        });

        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = "advanceCandidate";
        radio.value = c.candidate_id;

        div.appendChild(radio);
        div.appendChild(document.createTextNode(" " + lines.join(" / ")));
        advanceChoices.appendChild(div);
    });

    advanceModal.style.display = "flex";
}

// --- 進塁候補確定処理 ---
advanceForm.addEventListener("submit", async function (e) {
    e.preventDefault();

    const selected = document.querySelector('input[name="advanceCandidate"]:checked');
    if (!selected) {
        alert("候補を選択してください");
        return;
    }

    const candidateId = parseInt(selected.value);

    const res = await fetch(`/api/score-input/${gameId}/confirm`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            pitch_event_id: latestPitchEventId,
            candidate_id: candidateId
        }),
    });

    const data = await res.json();
    console.log("進塁確定:", data);

    advanceModal.style.display = "none";
    fetchAtBats(); // 最新状況を再取得
});

fetchAtBats();
