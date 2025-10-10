/**
 * File: frontend/js/components/view/league/createLeagueCard.js
 */

export function createLeagueCard(league) {
    const leagueCard = document.createElement("div")
    leagueCard.classList.add("league-card")

    const leagueName = document.createElement("div")
    leagueName.classList.add("league-card__name")
    leagueName.textContent = league.name
    leagueCard.append(leagueName)

    const leagueTeamList = document.createElement("div")
    leagueTeamList.classList.add("league-card__team-list")

    league.teams.forEach(team => {
        const leagueTeamCard = document.createElement("div")
        leagueTeamCard.classList.add("league-card__team-card")
        leagueTeamCard.textContent = team.name
        leagueTeamList.append(leagueTeamCard)
    })

    leagueCard.append(leagueTeamList)

    return leagueCard
}
