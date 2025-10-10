/**
 * File: frontend/js/renders/common/renderTournamentSection.js
 */

import { renderTournamentList } from "./renderTournamentList.js"

export async function renderTournamentSection(categoryId) {
    const tournamentSection = document.querySelector(".tournament-section")
    if (!tournamentSection) {
        console.error(`Error: <section id=tournament-section> not found`)
    }


    tournamentSection.innerHTML = ""


    const tournamentSectionTitle = document.createElement("div")
    tournamentSectionTitle.classList.add("tournament-section-title")
    tournamentSectionTitle.textContent = "大会一覧"
    tournamentSection.append(tournamentSectionTitle)


    const tournamentList = document.createElement("div")
    tournamentList.classList.add("tournament-list")
    tournamentSection.append(tournamentList)

    await renderTournamentList(categoryId)
}
