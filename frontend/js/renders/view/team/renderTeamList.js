/**
 * File: frontend/js/renders/team/renderTeamList.js
 */

import { getTeamList } from "../../../clients/team/getTeamList.js"
import { createTeamItem } from "../../../components/view/team/createTeamItem.js"

export async function renderTeamList(teamList, filters) {
    const teamListData = await getTeamList(filters)

    teamListData.forEach(teamData => {
        const team = createTeamItem(teamData)
        teamList.append(team)
    })
}
