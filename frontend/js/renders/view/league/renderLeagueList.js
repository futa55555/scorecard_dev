/**
 * File: frontend/js/renders/view/league/renderLeagueList.js
 */

import { getLeagueList } from "../../../clients/league/getLeagueList.js"
import { createLeagueCard } from "../../../components/view/league/createLeagueCard.js"

export async function renderLeagueList(leagueList, categoryId) {
    const leagueData = await getLeagueList(categoryId)

    leagueData.forEach(league => {
        const leagueCard = createLeagueCard(league)
        leagueList.append(leagueCard)
    })
}
