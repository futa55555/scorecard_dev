/**
 * File: frontend/js/main/category/teams.js
 */

import { renderHeader } from "../../renders/common/renderHeader.js"
import { renderNavbar } from "../../renders/common/renderNavbar.js"
import { renderTeamList } from "../../renders/team/renderTeamList.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const currentCategoryId = Number(params.get("category"))

    await renderHeader(currentCategoryId)
    renderNavbar(currentCategoryId)

    const filters = { categoryId: currentCategoryId }
    renderTeamList(filters)
}

async function init() {
    await renderInitial()
}

init()
