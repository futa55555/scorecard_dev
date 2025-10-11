/**
 * File: frontend/js/components/view/common/createToggleButton.js
 */

export function createToggleButton(whichList) {
    const toggleButton = document.createElement("button")
    toggleButton.classList.add("toggle-button", `${whichList}-toggle-button`)

    const image = document.createElement("img")
    image.classList.add(`${whichList}-toggle-button-img`)
    image.src = "/frontend/img/components/chevron-right.svg"
    image.alt = "一覧を表示"
    toggleButton.append(image)

    return toggleButton
}
