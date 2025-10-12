/**
 * File: frontend/js/components/team/createTeamFilter.js
 */

import { createFilterButton } from "../../../components/view/common/createFilterButton.js"

export function createTeamFilter(leagueSummaries) {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))
    const leagueId = Number(params.get("league"))


    const teamFilter = document.createElement("div")
    teamFilter.classList.add("team-filter")


    teamFilter.dataset.categoryId = categoryId


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


    teamFilter.append(leagueSet)


    const filterButton = createFilterButton()
    teamFilter.append(filterButton)


    return teamFilter
}
