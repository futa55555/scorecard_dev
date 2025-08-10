// frontend/public/scripts/teams.js

// このスクリプトは、チーム一覧ページに表示するチームデータをAPI経由で取得し、
// JavaScriptで描画・削除・追加・マイチーム設定を操作するものです。

// チーム一覧を取得して表示
function fetchTeams() {
    fetch("/api/teams") // FastAPIからJSON形式のチームデータを取得
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById("team-list");
            ul.innerHTML = ""; // 一度リストをクリア（再描画に備える）

            data.forEach(team => {
                // 各チームの情報を<li>としてHTMLに追加
                const li = document.createElement("li");

                // チーム名、マイチーム表示、削除ボタン、マイチーム切替ボタン
                li.innerHTML = `
                    <a href="/pages/team_members.html?team_id=${team.id}">${team.name}</a>
                    ${team.is_myteam ? "★" : ""}
                    <button onclick="deleteTeam(${team.id})">削除</button>
                    <button onclick="${team.is_myteam ? `unmarkMyTeam(${team.id})` : `markMyTeam(${team.id})`}">
                        ${team.is_myteam ? "マイチーム解除" : "マイチームに設定"}
                    </button>
                `;
                ul.appendChild(li);
            });
        });
}

// チーム削除の処理（DELETEメソッドで送信）
function deleteTeam(teamId) {
    fetch(`/api/teams/${teamId}`, { method: "DELETE" })
        .then(() => fetchTeams()); // 削除後に再取得して更新
}

// 指定のチームをマイチームに設定
function markMyTeam(teamId) {
    fetch(`/api/teams/${teamId}/mark_myteam`, { method: "POST" })
        .then(() => fetchTeams()); // 更新後に再取得
}

// マイチーム設定を解除
function unmarkMyTeam(teamId) {
    fetch(`/api/teams/${teamId}/unmark_myteam`, { method: "POST" })
        .then(() => fetchTeams()); // 更新後に再取得
}


// 初回ページ表示時に一度データを読み込む
fetchTeams();
