/**
 * File: frontend/js/clients/team/getTeamList.js
 */

import { apiFetch } from "../base.js"

export async function getTeamList(filters = {}) {
    try {
        let query = "/api/teams/"

        query += `?category=${filters.categoryId}`

        const data = await apiFetch(query)
        return data
    } catch (err) {
        console.error(`getTeamList() failed: ${err.message}`)
        throw err
    }
}
