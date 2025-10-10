/**
 * File: frontend/js/main/view/teamList.js
 */

import { renderHeader } from "../../renders/view/common/renderHeader.js"
import { renderNavbar } from "../../renders/view/common/renderNavbar.js"
import { renderTeamSection } from "../../renders/view/team/renderTeamSection.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))

    await renderHeader(categoryId)
    renderNavbar(categoryId)

    renderTeamSection(categoryId)
}

async function init() {
    await renderInitial()
}

init()
