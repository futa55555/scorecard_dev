/**
 * File: frontend/js/components/team/createTeamItem.js
 */

export function createTeamItem(teamData) {
    const team = document.createElement("div")

    const currentPath = window.location.pathname


    const teamName = document.createElement("p")
    const nameLink = document.createElement("a")

    nameLink.textContent = teamData.name

    nameLink.href = `/pages/teams?team=${teamData.team_id}`

    teamName.append(nameLink)
    team.append(teamName)


    const teamLeague = document.createElement("p")
    const leagueLink = document.createElement("a")

    leagueLink.textContent = teamData.league_id

    leagueLink.href = `/pages/leagues?team=${teamData.league_id}`

    teamLeague.append(leagueLink)
    team.append(teamLeague)


    return team
}
