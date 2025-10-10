/**
 * File: frontend/js/main/view/index.js
 */

import { renderHeader } from "../../renders/view/common/renderHeader.js"
import { renderNavbar } from "../../renders/view/common/renderNavbar.js"
import { renderFavoriteSection } from "../../renders/view/favorite/renderFavoriteSection.js"
import { renderPickupSection } from "../../renders/view/pickup/renderPickupSection.js"
import { renderLeagueSection } from "../../renders/view/league/renderLeagueSection.js"
import { renderTournamentSection } from "../../renders/view/tournament/renderTournamentSection.js"

async function renderInitial() {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))

    await renderHeader(categoryId)
    renderNavbar(categoryId)

    await renderFavoriteSection(categoryId)
    await renderPickupSection(categoryId)
    await renderLeagueSection(categoryId)
    await renderTournamentSection(categoryId)
}

async function init() {
    await renderInitial()
}

init()
