/**
 * File: frontend/js/clients/base.js
 */

export const API_BASE_URL = "http://localhost:8000"


export async function apiFetch(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;

    const defaultHeaders = { "Content-Type": "application/json" };
    const config = {
        headers: { ...defaultHeaders, ...options.headers },
        ...options,
    };

    let res;
    try {
        res = await fetch(url, config);
    } catch (err) {
        const msg = `[${endpoint}] FETCH Error: ${err.message}`;
        console.error(msg);
        throw new Error(msg);
    }

    let json = null;
    try {
        json = await res.json();
    } catch {
        json = { detail: "Invalid JSON response" };
    }

    if (!res.ok) {
        const message = json.detail || res.statusText || "HTTP request failed";
        const msg = `[${endpoint}] HTTP Error (${res.status}): ${message}`;
        console.error(msg);
        throw new Error(msg);
    }

    if (json.status && json.status !== "success") {
        const msg = `[${endpoint}] API Error: ${json.message || "Unknown API error"}`;
        console.error(msg);
        throw new Error(msg);
    }

    console.log(`[${endpoint}] Success: ${json.message || "Request completed"}`);
    return json.data ?? json;
}
