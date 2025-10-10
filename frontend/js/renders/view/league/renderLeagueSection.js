/**
 * File: frontend/js/renders/view/league/renderLeagueSection.js
 */

import { renderLeagueList } from "./renderLeagueList.js"

export async function renderLeagueSection(categoryId) {
    const leagueSection = document.querySelector(".league-section")
    if (!leagueSection) {
        console.error(`[renderLeagueSection] Error: <section id=league-section> not found`)
    }


    leagueSection.innerHTML = ""


    const leagueSectionTitle = document.createElement("div")
    leagueSectionTitle.classList.add("league-section-title")
    leagueSectionTitle.textContent = "リーグ一覧"
    leagueSection.append(leagueSectionTitle)


    const leagueList = document.createElement("div")
    leagueList.classList.add("league-list")
    leagueSection.append(leagueList)

    renderLeagueList(categoryId)
}
