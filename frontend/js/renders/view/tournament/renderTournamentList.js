/**
 * File: frontend/js/renders/view/tournament/renderTournamentList.js
 */

import { getTournamentList } from "../../../clients/tournament/getTournamentList.js"
import { createTournamentCard } from "../../../components/view/tournament/createTournamentCard.js"

export async function renderTournamentList(tournamentList, categoryId) {
    const tournamentData = await getTournamentList(categoryId)

    tournamentData.forEach(tournament => {
        const tournamentCard = createTournamentCard(tournament)
        tournamentList.append(tournamentCard)
    })
}
