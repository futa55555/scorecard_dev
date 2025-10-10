/**
 * File: frontend/js/clients/league/getLeagueSummary.js
 */

import { apiFetch } from "../base.js"

export async function getLeagueSummary(categoryId) {
    try {
        let endpoint = "/api/leagues/summary"

        if (categoryId) {
            endpoint += `?category=${categoryId}`
        }
        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`[getLeagueSummary] Error: ${err.message}`)
        throw err
    }
}
