/**
 * File: frontend/js/clients/team/getTeamList.js
 */

import { apiFetch } from "../base.js"
import { buildQuery } from "../base.js"

export async function getTeamList(filters = {}) {
    try {
        const endpoint = buildQuery("/api/teams/", filters)

        const data = await apiFetch(endpoint)
        return data
    } catch (err) {
        console.error(`getTeamList() failed: ${err.message}`)
        throw err
    }
}
