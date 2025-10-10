/**
 * File: frontend/js/components/view/league/createLeagueSectionTitle.js
 */

export function createLeagueSectionTitle() {
    const leagueSectionTitle = document.createElement("div")

    leagueSectionTitle.classList.add("league-section-title")
    leagueSectionTitle.textContent = "リーグ一覧"

    return leagueSectionTitle
}
