/**
 * File: frontend/js/renders/view/league/renderLeagueList.js
 */

import { getLeagueList } from "../../../clients/league/getLeagueList.js"
import { createLeagueCard } from "../../../components/view/league/createLeagueCard.js"
import { bindListToggle } from "../../../events/view/common/bindListToggle.js"

export async function renderLeagueList(categoryId) {
    const leagueList = document.querySelector(".league-list")
    if (!leagueList) {
        console.error(`[renderLeagueList] Error: <div class="league-list"> not found`)
    }


    leagueList.innerHTML = ""


    const leagueData = await getLeagueList(categoryId)

    leagueData.forEach(league => {
        const leagueCard = createLeagueCard(league)
        bindListToggle(leagueCard)
        leagueList.append(leagueCard)
    })
}
