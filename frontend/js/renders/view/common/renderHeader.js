/**
 * File: frontend/js/renders/common/renderHeader.js
 */

import { createCategoryBar } from "../../../components/view/common/createCategoryBar.js"

export async function renderHeader(categoryId) {
    const header = document.querySelector(".header")

    if (!header) {
        console.error("[renderHeader] Error: <header id='header'> not found")
        return
    }


    header.innerHTML = ""


    const title = document.createElement("h1")

    const titleLink = document.createElement("a")
    titleLink.textContent = "ソフナビ"
    titleLink.href = "index.html"
    title.append(titleLink)

    header.append(title)


    const bar = await createCategoryBar(categoryId)
    header.append(bar)
}
