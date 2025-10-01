// frontend/public/scripts/people.js

// このスクリプトは、人間一覧ページに表示する人間データをAPI経由で取得し、
// JavaScriptで描画を操作するものです。

// 人間一覧を取得して表示
function fetchPeople() {
    fetch("/api/people") // FastAPIからJSON形式の人間データを取得
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById("person-list");
            ul.innerHTML = ""; // 一度リストをクリア（再描画に備える）

            data.forEach(person => {
                // 各人間の情報を<li>としてHTMLに追加
                const li = document.createElement("li");

                // 人間名
                li.innerHTML = `
                    ${person.name}
                    ${person.pitching_side}
                    ${person.batting_side}
                    ${person.height_cm}
                    ${person.weight_kg}
                    ${person.birthday}
                `;
                ul.appendChild(li);
            });
        });
}

// 初回ページ表示時に一度データを読み込む
fetchPeople();
