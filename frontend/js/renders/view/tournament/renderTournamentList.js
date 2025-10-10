/**
 * File: frontend/js/renders/view/tournament/renderTournamentList.js
 */

import { getTournamentList } from "../../../clients/tournament/getTournamentList.js"
import { createTournamentCard } from "../../../components/view/tournament/createTournamentCard.js"

export async function renderTournamentList(categoryId) {
    const tournamentList = document.querySelector(".tournament-list")
    if (!tournamentList) {
        console.log(`[renderTournamentList] Error: <div class="tournament-list"> not found`)
    }


    tournamentList.innerHTML = ""


    const tournamentData = await getTournamentList(categoryId)


    tournamentData.forEach(tournament => {
        const tournamentCard = createTournamentCard(tournament)
        tournamentList.append(tournamentCard)
    })
}
