// frontend/public/scripts/index.js

// ページ読み込み後にマイチーム情報を取得して表示
window.addEventListener("DOMContentLoaded", () => {
    fetch("/api/myteam")
        .then(response => {
            if (!response.ok) throw new Error("APIエラー");
            return response.json();
        })
        .then(data => {
            const display = document.getElementById("myteam-name");
            if (data && data.name) {
                display.textContent = data.name;
            } else {
                display.textContent = "未設定";
            }
        })
        .catch(error => {
            document.getElementById("myteam-name").textContent = "取得失敗";
            console.error("マイチーム取得エラー:", error);
        });
});
