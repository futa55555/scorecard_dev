/**
 * File: frontend/js/components/view/common/createPageBar.js
 */

export function createPageBar(whichList, currentPage, totalPage) {
    const pageBar = document.createElement("div")
    pageBar.classList.add("page-bar", `${whichList}-page-bar`)

    pageBar.dataset.currentPage = currentPage


    const pageBackButton = document.createElement("button")
    pageBackButton.classList.add("page-back-button")

    const pageBackImg = document.createElement("img")
    pageBackImg.src = "/frontend/img/components/arrow-left.svg"
    pageBackImg.alt = "1つ前のページへ戻る"
    if (currentPage === 1) {
        pageBackButton.disabled = true
    }

    pageBackButton.append(pageBackImg)

    pageBar.append(pageBackButton)


    const pageShowBox = document.createElement("div")
    pageShowBox.classList.add("page-show-box")
    pageShowBox.textContent = `${currentPage} / ${totalPage}`
    pageBar.append(pageShowBox)


    const pageForwardButton = document.createElement("button")
    pageForwardButton.classList.add("page-forward-button")

    const pageForwardImg = document.createElement("img")
    pageForwardImg.src = "/frontend/img/components/arrow-right.svg"
    pageForwardImg.alt = "1つ先のページへ進む"
    if (currentPage === totalPage) {
        pageForwardButton.disabled = true
    }

    pageForwardButton.append(pageForwardImg)

    pageBar.append(pageForwardButton)


    return pageBar
}
