/**
 * File: frontend/js/components/view/team/createTeamList.js
 */

import { renderTeamList } from "../../../renders/view/team/renderTeamList.js"

export async function createTeamList(categoryId) {
    const teamList = document.createElement("div")

    teamList.classList.add("team-list")


    const filters = {
        category_id: categoryId
    }

    renderTeamList(teamList, filters)

    return teamList
}
