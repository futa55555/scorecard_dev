/**
 * File: frontend/js/renders/view/favorite/renderFavoriteSection.js
 */

export async function renderFavoriteSection(categoryId) {
    const favoriteSection = document.querySelector(".favorite-section")

    if (!favoriteSection) {
        console.error(`[renderFavoriteSection] Error: <section id=favoriteSection> not found`)
    }

    console.log(`favorite-section pass`)
}
