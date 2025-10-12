/**
 * File: frontend/js/events/team/bindTeamFilter.js
 */

import { filterPage } from "../common/filterPage.js"

export async function bindTeamFilter(teamFilter) {
    const leagueSelector = teamFilter.querySelector(".league-selector")
    const filterButton = teamFilter.querySelector(".filter-button")

    filterButton.addEventListener("click", () => {
        const categoryId = Number(teamFilter.dataset.categoryId)
        const leagueId = Number(leagueSelector.value)

        const queryParams = [
            { type: "category", value: categoryId },
            { type: "league", value: leagueId },
            { type: "page", value: 1 }
        ]

        filterPage(queryParams)
    })
}
