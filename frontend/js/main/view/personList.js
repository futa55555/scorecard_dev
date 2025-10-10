/**
 * File: frontend/js/main/view/people.js
 */

import { renderHeader } from "../../renders/view/common/renderHeader.js"
import { renderNavbar } from "../../renders/view/common/renderNavbar.js"
import { renderPersonSection } from "../../renders/view/person/renderPersonSection.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))

    await renderHeader(categoryId)
    renderNavbar(categoryId)

    renderPersonSection(categoryId)
}

async function init() {
    await renderInitial()
}

init()
