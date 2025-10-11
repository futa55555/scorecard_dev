/**
 * File: frontend/js/events/view/common/bindListToggle.js
 */

export function bindListToggle(card) {
    const toggleButton = card.querySelector(".toggle-button")
    toggleButton.addEventListener("click", () => {
        const image = toggleButton.querySelector("img")
        const list = card.querySelector(".list")


        const isHidden = (list.style.display === "none")

        if (isHidden) {
            image.src = "/frontend/img/components/chevron-down.svg"
            image.alt = "一覧を非表示"
            list.style.display = "block"
        } else {
            image.src = "/frontend/img/components/chevron-right.svg"
            image.alt = "一覧を表示"
            list.style.display = "none"
        }
    })
}
