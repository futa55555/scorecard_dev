/**
 * File: frontend/js/events/view/common/bindPagination.js
 */

export function bindPagination(pageBar) {
    const pageBackButton = pageBar.querySelector(".page-back-button")
    pageBackButton.addEventListener("click", () => {
        movePage(-1)
    })

    const pageForwardButton = pageBar.querySelector(".page-forward-button")
    pageForwardButton.addEventListener("click", () => {
        movePage(1)
    })
}

function movePage(delta) {
    const currentUrl = window.location
    const params = new URLSearchParams(currentUrl.search)

    const currentPage = Number(params.get("page"))
    const newPage = currentPage + delta

    params.set("page", newPage)

    const newUrl = `${currentUrl.pathname}?${params.toString()}`

    window.location.href = newUrl
}
