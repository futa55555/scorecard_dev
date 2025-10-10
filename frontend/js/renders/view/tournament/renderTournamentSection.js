/**
 * File: frontend/js/renders/common/renderTournamentSection.js
 */

import { createTournamentSectionTitle } from "../../../components/view/tournament/createTournamentSectionTitle.js"
import { createTournamentList } from "../../../components/view/tournament/createTournamentList.js"

export async function renderTournamentSection(categoryId) {
    const tournamentSection = document.querySelector(".tournament-section")

    if (!tournamentSection) {
        console.error(`Error: <section id=tournament-section> not found`)
    }

    tournamentSection.innerHTML = ""

    const tournamentSectionTitle = createTournamentSectionTitle()
    const tournamentList = await createTournamentList(categoryId)

    tournamentSection.append(tournamentSectionTitle, tournamentList)
}
