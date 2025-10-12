/**
 * File: frontend/js/renders/common/renderNavbar.js
 */

export function renderNavbar(categoryId) {
    const navbar = document.querySelector(".navbar")

    if (!navbar) {
        console.error(`[renderNavbar] Error: <nav class="navbar"> not found`)
    }

    const navList = [
        { text: "トップ", link: "index" },
        { text: "試合日程", link: "game_list" },
        { text: "チーム一覧", link: "team_list" },
        { text: "メンバー一覧", link: "person_list" }
    ]

    const currentPath = window.location.pathname
    const afterCategory = currentPath.split("/view/")[1]
    const currentPage = afterCategory.split(/[/.]/)[0]

    navList.forEach(nav => {
        const a = document.createElement("a")
        a.textContent = nav.text

        // ===== 共通URL構築 =====
        const params = new URLSearchParams()

        // category があれば
        if (categoryId) params.set("category", categoryId)

        // index 以外なら page=1 を付与
        if (nav.link !== "index") params.set("page", 1)

        // クエリが存在すれば ? を付けて結合
        const queryString = params.toString() ? `?${params.toString()}` : ""

        // 絶対パス構築
        a.href = `./${nav.link}.html${queryString}`

        // 現在ページをハイライト
        if (currentPage === nav.link) a.classList.add("active")

        navbar.append(a)
    })
}
