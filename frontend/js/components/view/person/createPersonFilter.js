/**
 * File: frontend/js/components/view/person/createPersonFilter.js
 */

import { createFilterButton } from "../common/createFilterButton.js"

export function createPersonFilter(leagueSummaries) {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))
    const leagueId = Number(params.get("league"))


    const personFilter = document.createElement("div")
    personFilter.classList.add("person-filter")


    personFilter.dataset.categoryId = categoryId


    const leagueSet = document.createElement("div")
    leagueSet.classList.add("league-set")

    const leagueLabel = document.createElement("label")
    leagueLabel.htmlFor = "league-selector"
    leagueLabel.classList.add("league-label")
    leagueLabel.textContent = "リーグ"
    leagueSet.append(leagueLabel)

    const leagueSelector = document.createElement("select")
    leagueSelector.id = "league-selector"
    leagueSelector.classList.add("league-selector")

    const leagueOptionAll = document.createElement("option")
    leagueOptionAll.classList.add("option")
    leagueOptionAll.value = 0
    leagueOptionAll.textContent = "すべてのリーグ"
    if (leagueId === 0) {
        leagueOptionAll.selected = true
    }

    leagueSelector.append(leagueOptionAll)

    leagueSummaries.forEach(leagueSummary => {
        const leagueOption = document.createElement("option")
        leagueOption.classList.add("league-option")
        leagueOption.value = leagueSummary.league_id
        leagueOption.textContent = leagueSummary.name
        if (leagueId === leagueSummary.league_id) {
            leagueOption.selected = true
        }
        leagueSelector.append(leagueOption)
    })

    leagueSet.append(leagueSelector)


    personFilter.append(leagueSet)


    const filterButton = createFilterButton()
    personFilter.append(filterButton)


    return personFilter
}
