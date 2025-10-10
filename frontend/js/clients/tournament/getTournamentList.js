/**
 * File: frontend/js/clients/tournament/getTournamentList.js
 */

import { apiFetch } from "../base.js"
import { buildQuery } from "../base.js"

export async function getTournamentList(categoryId) {
    try {
        const filters = {
            category_id: categoryId
        }

        const endpoint = buildQuery("/api/tournaments/", filters)

        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`[getTournamentList] Error: ${err.message}`)
        throw err
    }
}
