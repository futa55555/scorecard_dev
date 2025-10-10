/**
 * File: frontend/js/components/view/team/createTeamSectionTitle.js
 */

export function createTeamSectionTitle() {
    const teamSectionTitle = document.createElement("div")

    teamSectionTitle.classList.add("team-section-title")
    teamSectionTitle.textContent = "チーム一覧"

    return teamSectionTitle
}
