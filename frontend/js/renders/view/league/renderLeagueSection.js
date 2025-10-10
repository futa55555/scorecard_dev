/**
 * File: frontend/js/renders/view/league/renderLeagueSection.js
 */

import { createLeagueSectionTitle } from "../../../components/view/league/createLeagueSectionTitle.js"
import { createLeagueList } from "../../../components/view/league/createLeagueList.js"

export async function renderLeagueSection(categoryId) {
    const leagueSection = document.querySelector(".league-section")

    if (!leagueSection) {
        console.error(`[renderLeagueSection] Error: <section id=league-section> not found`)
    }


    leagueSection.innerHTML = ""

    const leagueSectionTitle = createLeagueSectionTitle()
    const leagueList = await createLeagueList(categoryId)

    leagueSection.append(leagueSectionTitle, leagueList)
}
