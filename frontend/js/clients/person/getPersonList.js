/**
 * File: frontend/js/clients/person/getPersonList.js
 */

import { apiFetch, buildQuery } from "../base.js"

export async function getPersonList(currentPage, limit, categoryId, leagueId) {
    try {
        const filters = {
            current_page: currentPage,
            limit: limit,
            category_id: categoryId,
            league_id: leagueId
        }
        const endpoint = buildQuery("/api/people/", filters)
        const data = await apiFetch(endpoint)

        return data
    } catch (err) {
        console.error(`getPersonList() failed: ${err.message}`)
        throw err
    }
}
