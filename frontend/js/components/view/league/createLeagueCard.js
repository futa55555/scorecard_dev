/**
 * File: frontend/js/components/view/league/createLeagueCard.js
 */

import { createToggleButton } from "../common/createToggleButton.js"

export function createLeagueCard(league) {
    const currentPath = window.location.pathname
    const baseUrl = currentPath.split("/index")[0]


    const leagueCard = document.createElement("div")
    leagueCard.classList.add("league-card")


    const leagueHeader = document.createElement("div")
    leagueHeader.classList.add("league-header")

    const leagueName = document.createElement("div")
    leagueName.classList.add("league-card__name")

    const leagueLink = document.createElement("a")
    leagueLink.classList.add("league-link")
    leagueLink.href = `${baseUrl}/league_detail.html?league=${league.league_id}`
    leagueLink.textContent = league.name
    leagueName.append(leagueLink)

    leagueHeader.append(leagueName)


    const leagueToggleButton = createToggleButton("league")
    leagueHeader.append(leagueToggleButton)


    leagueCard.append(leagueHeader)


    const leagueTeamList = document.createElement("div")
    leagueTeamList.classList.add("list", "league-card__team-list")
    leagueTeamList.style.display = "none"

    league.teams.forEach(team => {
        const leagueTeamCard = document.createElement("div")
        leagueTeamCard.classList.add("league-card__team-card")
        leagueTeamCard.textContent = team.name
        leagueTeamList.append(leagueTeamCard)
    })

    leagueCard.append(leagueTeamList)

    return leagueCard
}
