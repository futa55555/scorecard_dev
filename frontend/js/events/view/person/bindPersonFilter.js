/**
 * File: frontend/js/events/view/person/bindPersonFilter.js
 */

import { renderPersonList } from "../../../renders/view/person/renderPersonList.js"

export async function bindPersonFilter(personFilter) {
    const leagueSelector = personFilter.querySelector(".league-selector")
    const filterButton = personFilter.querySelector(".filter-button")

    filterButton.addEventListener("click", () => {
        const categoryId = Number(personFilter.dataset.categoryId)
        const leagueId = Number(leagueSelector.value)

        renderPersonList(categoryId, leagueId)
    })
}
