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
        const link = document.createElement("a")
        link.textContent = nav.text

        if (categoryId !== 0) {
            link.href = `./${nav.link}.html?category=${categoryId}`
        } else {
            link.href = `./${nav.link}.html`
        }

        if (currentPage === nav.link) {
            link.classList.add("active")
        }

        navbar.append(link)
    })
}
