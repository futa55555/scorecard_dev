/**
 * File: frontend/js/renders/view/team/renderTeamSections.js
 */

import { getLeagueSummaries } from "../../../clients/league/getLeagueSummaries.js"
import { createTeamFilter } from "../../../components/view/team/createTeamFilter.js"
import { bindTeamFilter } from "../../../events/view/team/bindTeamFilter.js"
import { renderTeamList } from "./renderTeamList.js"

export async function renderTeamSection(categoryId) {
    const teamSection = document.querySelector(".team-section")
    if (!teamSection) {
        console.error(`[renderTeamSection] Error: <section class="team-section"> not found`)
    }


    teamSection.innerHTML = ""


    const teamSectionTitle = document.createElement("div")
    teamSectionTitle.classList.add("team-section-title")
    teamSectionTitle.textContent = "チーム一覧"
    teamSection.append(teamSectionTitle)


    const leagueSummaries = await getLeagueSummaries(categoryId)
    const teamFilter = createTeamFilter(categoryId, leagueSummaries)
    teamSection.append(teamFilter)

    bindTeamFilter(teamFilter)


    const teamList = document.createElement("div")
    teamList.classList.add("team-list")
    teamSection.append(teamList)

    renderTeamList(categoryId, 0)
}
