/**
 * File: frontend/js/components/view/common/createFilterButton.js
 */

export function createFilterButton() {
    const filterButton = document.createElement("button")
    filterButton.classList.add("filter-button")
    filterButton.textContent = "絞り込み"
    return filterButton
}
