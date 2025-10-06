/**
 * File: frontend/js/renders/team/renderTeamList.js
 */

import { getTeamList } from "../../clients/team/getTeamList.js"
import { createTeamItem } from "../../components/team/createTeamItem.js"

export async function renderTeamList(filters = {}) {
    const teamListData = await getTeamList(filters)

    const teamList = document.getElementById("team-list")

    teamListData.forEach(teamData => {
        const team = createTeamItem(teamData)
        teamList.append(team)
    })
}
