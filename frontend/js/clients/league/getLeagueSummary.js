/**
 * File: frontend/js/clients/getLeagueSummary.js
 */

import { apiFetch } from "../base.js"

export async function getLeagueSummary(categoryId) {
    try {
        const data = await apiFetch("/api/leagues")
        return data
    } catch (err) {
        console.error(`getLeagueSummary() failed: ${err.message}`)
        throw err
    }
}
