/**
 * File: frontend/js/clients/team/getTeamList.js
 */

import { apiFetch, buildQuery } from "../base.js"

export async function getTeamList(categoryId, leagueId) {
    try {
        const filters = {
            category_id: categoryId,
            league_id: leagueId
        }
        const endpoint = buildQuery("/api/teams/", filters)
        const data = await apiFetch(endpoint)

        return data
    } catch (err) {
        console.error(`getTeamList() failed: ${err.message}`)
        throw err
    }
}
