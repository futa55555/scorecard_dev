// frontend/public/scripts/team_add.js

document.getElementById("teamForm").addEventListener("submit", async function(e) {
    e.preventDefault(); // ページ遷移を止める

    // フォームデータをJSON化
    const formData = new FormData(e.target);
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    try {
        // JSONをPOST
        const res = await fetch("/api/teams/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(jsonData),
        });

        const data = await res.json();
        console.log("サーバーからの返答:", data);

        if (res.ok) {
            // 登録成功 → チーム一覧ページに遷移
            window.location.href = "/pages/teams.html";
        } else {
            alert("登録失敗: " + (data.detail || "不明なエラー"));
        }
    } catch (err) {
        console.error("通信エラー:", err);
        alert("通信エラーが発生しました");
    }
});
