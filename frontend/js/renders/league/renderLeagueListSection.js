/**
 * File: frontend/js/renders/league/renderLeagueListSection.js
 */

import { createLeagueListItem } from "../../components/league/createLeagueListItem.js"

export async function renderLeagueList(currentCategoryId) {
    const leagueListSection = document.getElementById("league-list-section")

    if (!leagueListSection) {
        console.error("Error: <div id='league-list-section'> not found")
    }


    leagueListSection.innerHTML = ""


    const title = document.createElement("div")
    title.textContent = "リーグ一覧"
    leagueListSection.append(title)


}
