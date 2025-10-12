/**
 * File: frontend/js/renders/team/renderTeamList.js
 */

import { getTeamList } from "../../../clients/team/getTeamList.js"
import { createPageBar } from "../../../components/view/common/createPageBar.js"
import { createTeamCard } from "../../../components/view/team/createTeamCard.js"
import { bindPagination } from "../../../events/view/common/bindPagination.js"

export async function renderTeamList() {
    const teamList = document.querySelector(".team-list")
    if (!teamList) {
        console.error(`[renderTeamList] Error: <div class="team-list"> not found`)
    }


    teamList.innerHTML = ""


    const params = new URLSearchParams(window.location.search)
    const currentPage = Number(params.get("page"))
    const categoryId = Number(params.get("category"))
    const leagueId = Number(params.get("league"))

    const limit = 30


    const teamListData = await getTeamList(currentPage, limit, categoryId, leagueId)

    teamListData.teams.forEach(teamData => {
        const team = createTeamCard(teamData)
        teamList.append(team)
    })

    const teamListPageBar = createPageBar("team", currentPage, teamListData.total_page)
    teamList.append(teamListPageBar)

    bindPagination(teamListPageBar)
}
