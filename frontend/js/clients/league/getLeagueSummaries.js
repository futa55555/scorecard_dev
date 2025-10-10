/**
 * File: frontend/js/clients/league/getLeagueSummaries.js
 */

import { apiFetch, buildQuery } from "../base.js"

export async function getLeagueSummaries(categoryId) {
    try {
        const filters = {
            category_id: categoryId
        }
        const endpoint = buildQuery("/api/leagues/summary/", filters)
        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`[getLeagueSummaries] Error: ${err.message}`)
        throw err
    }
}
