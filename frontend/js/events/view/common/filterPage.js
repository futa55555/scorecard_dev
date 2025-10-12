/**
 * File: frontend/js/events/view/common/filterPage.js
 */

export function filterPage(queryParams) {
    const currentUrl = window.location
    const params = new URLSearchParams(currentUrl.search)

    queryParams.forEach(({ type, value }) => {
        if (value) {
            params.set(type, value)
        }
    })

    const newUrl = `${currentUrl.pathname}?${params.toString()}`

    window.location.href = newUrl
}
