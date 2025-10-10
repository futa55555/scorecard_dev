/**
 * File: frontend/js/components/view/tournament/createTournamentSectionTitle.js
 */

export function createTournamentSectionTitle() {
    const tournamentSectionTitle = document.createElement("div")

    tournamentSectionTitle.classList.add("tournament-section-title")
    tournamentSectionTitle.textContent = "大会一覧"

    return tournamentSectionTitle
}
