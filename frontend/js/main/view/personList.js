/**
 * File: frontend/js/main/category/people.js
 */

import { renderHeader } from "../../renders/common/renderHeader.js"
import { renderNavbar } from "../../renders/common/renderNavbar.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))

    await renderHeader(categoryId)
    renderNavbar(categoryId)
}

async function init() {
    await renderInitial()
}

init()
