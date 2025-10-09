/**
 * File: frontend/js/clients/categories/getCategoryList.js
 */

import { apiFetch } from "../base.js"

export async function getCategoryList() {
    try {
        const data = await apiFetch("/api/categories/summary/")
        return data
    } catch (err) {
        console.error(`getCategoryList() failed: ${err.message}`)
        throw err
    }
}
