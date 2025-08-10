// frontend/public/scripts/games.js

// 試合一覧を取得して表示
function fetchGames() {
    fetch("/api/games")
        .then(res => res.json())
        .then(data => {
            const tbody = document.querySelector("#games-table tbody");
            tbody.innerHTML = "";

            data.forEach(game => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${game.date}</td>
                    <td>${game.team1_name}</td>
                    <td>${game.team2_name}</td>
                    <td>${game.status}</td>
                    <td>
                        <button onclick="deleteGame(${game.id})">削除</button>
                        ${game.status === "draft" ? `<button onclick="startGame(${game.id})">試合開始</button>` : ""}
                    </td>
                `;
                tbody.appendChild(tr);
            });
        });
}

// チーム一覧を取得してセレクトボックスに表示
function fetchTeamsForSelect() {
    fetch("/api/teams")
        .then(res => res.json())
        .then(teams => {
            const team1Select = document.getElementById("team1-select");
            const team2Select = document.getElementById("team2-select");
            team1Select.innerHTML = "";
            team2Select.innerHTML = "";

            teams.forEach(team => {
                const opt1 = document.createElement("option");
                opt1.value = team.id;
                opt1.textContent = team.name;
                team1Select.appendChild(opt1);

                const opt2 = document.createElement("option");
                opt2.value = team.id;
                opt2.textContent = team.name;
                team2Select.appendChild(opt2);
            });
        });
}

// 試合追加
document.getElementById("add-game-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {
        date: formData.get("date"),
        team1_id: parseInt(formData.get("team1_id")),
        team2_id: parseInt(formData.get("team2_id"))
    };

    fetch("/api/games", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(() => {
        this.reset();
        fetchGames();
    });
});

// 試合削除
function deleteGame(id) {
    if (!confirm("本当に削除しますか？")) return;
    fetch(`/api/games/${id}`, { method: "DELETE" })
        .then(() => fetchGames());
}

// 試合開始
function startGame(id) {
    fetch(`/api/games/${id}/start`, { method: "POST" })
        .then(() => fetchGames());
}

// 初期化
fetchTeamsForSelect();
fetchGames();
