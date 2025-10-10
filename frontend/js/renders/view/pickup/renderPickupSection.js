/**
 * File: frontend/js/renders/view/pickup/renderPickupSection.js
 */

export async function renderPickupSection(categoryId) {
    const pickupSection = document.querySelector(".pickup-section")

    if (!pickupSection) {
        console.error(`[renderPickupSection] Error: <section id=pickup-section> not found`)
    }

    console.log(`pickup-section pass`)
}
