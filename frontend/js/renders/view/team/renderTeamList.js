/**
 * File: frontend/js/renders/team/renderTeamList.js
 */

import { getTeamList } from "../../../clients/team/getTeamList.js"
import { createTeamCard } from "../../../components/view/team/createTeamCard.js"

export async function renderTeamList(categoryId, leagueId) {
    const teamList = document.querySelector(".team-list")
    if (!teamList) {
        console.error(`[renderTeamList] Error: <div class="team-list"> not found`)
    }


    teamList.innerHTML = ""


    const teamListData = await getTeamList(categoryId, leagueId)

    teamListData.forEach(teamData => {
        const team = createTeamCard(teamData)
        teamList.append(team)
    })
}
