/**
 * File: frontend/js/components/view/league/createLeagueList.js
 */

import { renderLeagueList } from "../../../renders/view/league/renderLeagueList.js"

export async function createLeagueList(categoryId) {
    const leagueList = document.createElement("div")

    leagueList.classList.add("league-list")


    renderLeagueList(leagueList, categoryId)

    return leagueList
}
