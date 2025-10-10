/**
 * File: frontend/js/clients/categories/getCategorySummaries.js
 */

import { apiFetch, buildQuery } from "../base.js"

export async function getCategorySummaries() {
    try {
        const filters = {}
        const endpoint = buildQuery("/api/categories/summary/", filters)
        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`[getCategorySummaries] Error: ${err.message}`)
        throw err
    }
}
