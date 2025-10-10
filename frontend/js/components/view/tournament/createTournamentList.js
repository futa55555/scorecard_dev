/**
 * File: frontend/js/components/view/tournament/createTournamentList.js
 */

import { renderTournamentList } from "../../../renders/view/tournament/renderTournamentList.js"

export async function createTournamentList(categoryId) {
    const tournamentList = document.createElement("div")

    tournamentList.classList.add("tournament-list")


    renderTournamentList(tournamentList, categoryId)

    return tournamentList
}
