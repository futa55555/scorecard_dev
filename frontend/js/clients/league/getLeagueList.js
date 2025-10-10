/**
 * File: frontend/js/clients/league/getLeagueList.js
 */

import { apiFetch } from "../base.js"
import { buildQuery } from "../base.js"

export async function getLeagueList(categoryId) {
    try {
        const filters = {
            category_id: categoryId
        }

        const endpoint = buildQuery("/api/leagues/", filters)

        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`[getLeagueList] Error: ${err.message}`)
        throw err
    }
}
