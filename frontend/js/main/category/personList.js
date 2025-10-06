/**
 * File: frontend/js/main/category/people.js
 */

import { renderHeader } from "../../renders/common/renderHeader.js"
import { renderNavbar } from "../../renders/common/renderNavbar.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const currentCategoryId = Number(params.get("category"))

    await renderHeader(currentCategoryId)
    renderNavbar(currentCategoryId)
}

async function init() {
    await renderInitial()
}

init()
