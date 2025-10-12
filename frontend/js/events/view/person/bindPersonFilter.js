/**
 * File: frontend/js/events/view/person/bindPersonFilter.js
 */

import { filterPage } from "../common/filterPage.js"

export async function bindPersonFilter(personFilter) {
    const leagueSelector = personFilter.querySelector(".league-selector")
    const filterButton = personFilter.querySelector(".filter-button")

    filterButton.addEventListener("click", () => {
        const categoryId = Number(personFilter.dataset.categoryId)
        const leagueId = Number(leagueSelector.value)

        const queryParams = [
            { type: "category", value: categoryId },
            { type: "league", value: leagueId },
            { type: "page", value: 1 }
        ]

        filterPage(queryParams)
    })
}
