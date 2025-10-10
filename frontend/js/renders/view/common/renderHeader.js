/**
 * File: frontend/js/renders/common/renderHeader.js
 */

import { getCategorySummaries } from "../../../clients/category/getCategorySummaries.js"
import { createCategoryBar } from "../../../components/view/common/createCategoryBar.js"

export async function renderHeader(categoryId) {
    const header = document.querySelector(".header")

    if (!header) {
        console.error("[renderHeader] Error: <header class='header'> not found")
        return
    }


    header.innerHTML = ""


    const title = document.createElement("h1")

    const titleLink = document.createElement("a")
    titleLink.textContent = "ソフナビ"
    titleLink.href = "index.html"
    title.append(titleLink)

    header.append(title)


    let categoryList = await getCategorySummaries()
    const bar = await createCategoryBar(categoryList)
    header.append(bar)
}
