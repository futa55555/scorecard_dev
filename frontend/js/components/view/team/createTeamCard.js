/**
 * File: frontend/js/components/team/createTeamCard.js
 */

export function createTeamCard(teamData) {
    const currentPath = window.location.pathname
    const baseUrl = currentPath.split("/team")[0]


    const teamCard = document.createElement("div")
    teamCard.classList.add("team-card")


    const teamName = document.createElement("div")
    teamName.classList.add("team-name")

    const teamNameLink = document.createElement("a")
    teamNameLink.classList.add("team-name-link")

    teamNameLink.textContent = teamData.name
    teamNameLink.href = `${baseUrl}/team_detail.html?team=${teamData.team_id}`
    teamName.append(teamNameLink)
    teamCard.append(teamName)


    return teamCard
}
