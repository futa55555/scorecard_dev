/**
 * File: frontend/js/renders/view/team/renderTeamSections.js
 */

import { createTeamSectionTitle } from "../../../components/view/team/createTeamSectionTitle.js"
import { createTeamFilter } from "../../../components/view/team/createTeamFilter.js"
import { createTeamList } from "../../../components/view/team/createTeamList.js"

export async function renderTeamSection(categoryId) {
    const teamSection = document.querySelector(".team-section")

    if (!teamSection) {
        console.error(`[renderTeamSection] Error: <section class="team-section"> not found`)
    }


    teamSection.innerHTML = ""

    const teamSectionTitle = createTeamSectionTitle()
    const teamFilter = createTeamFilter(categoryId)
    const teamList = await createTeamList(categoryId)

    teamSection.append(teamSectionTitle, teamList)
}
