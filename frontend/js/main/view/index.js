/**
 * File: frontend/js/main/view/index.js
 */

import { renderHeader } from "../../renders/common/renderHeader.js"
import { renderNavbar } from "../../renders/common/renderNavbar.js"
import { renderFavoriteSection } from "../../renders/common/renderFavoriteSection.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const currentCategoryId = Number(params.get("category"))

    await renderHeader(currentCategoryId)
    renderNavbar(currentCategoryId)

    await renderFavoriteSection(currentCategoryId)
    await renderPickupSection(currentCategoryId)
    await renderLeagueSection(currentCategoryId)
    await renderTournamentSection(currentCategoryId)
}

async function init() {
    await renderInitial()
}

init()
