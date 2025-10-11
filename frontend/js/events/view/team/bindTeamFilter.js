/**
 * File: frontend/js/events/team/bindTeamFilter.js
 */

import { renderTeamList } from "../../../renders/view/team/renderTeamList.js"

export async function bindTeamFilter(teamFilter) {
    const leagueSelector = teamFilter.querySelector(".league-selector")
    const filterButton = teamFilter.querySelector(".filter-button")

    filterButton.addEventListener("click", () => {
        const categoryId = Number(teamFilter.dataset.categoryId)
        const leagueId = Number(leagueSelector.value)

        renderTeamList(categoryId, leagueId)
    })

}
