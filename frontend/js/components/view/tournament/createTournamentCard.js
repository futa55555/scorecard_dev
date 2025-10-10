/**
 * File: frontend/js/components/view/tournament/createTournamentCard.js
 */

export function createTournamentCard(tournament) {
    const tournamentCard = document.createElement("div")
    tournamentCard.classList.add("tournament-card")

    const tournamentName = document.createElement("div")
    tournamentName.classList.add("tournament-card__name")
    tournamentName.textContent = tournament.name
    tournamentCard.append(tournamentName)

    return tournamentCard
}
