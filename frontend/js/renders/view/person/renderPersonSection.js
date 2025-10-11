/**
 * File: frontend/js/renders/view/person/renderPersonSection.js
 */

import { getLeagueSummaries } from "../../../clients/league/getLeagueSummaries.js"
import { createPersonFilter } from "../../../components/view/person/createPersonFilter.js"
import { bindPersonFilter } from "../../../events/view/person/bindPersonFilter.js"
import { renderPersonList } from "./renderPersonList.js"

export async function renderPersonSection(categoryId) {
    const personSection = document.querySelector(".person-section")
    if (!personSection) {
        console.error(`[renderPersonSection] Error: <section class="person-section"> not found`)
    }


    personSection.innerHTML = ""


    const personSectionTitle = document.createElement("div")
    personSectionTitle.classList.add("person-section-title")
    personSectionTitle.textContent = "チーム一覧"
    personSection.append(personSectionTitle)


    const leagueSummaries = await getLeagueSummaries(categoryId)
    const personFilter = createPersonFilter(categoryId, leagueSummaries)
    personSection.append(personFilter)

    bindPersonFilter(personFilter)


    const personList = document.createElement("div")
    personList.classList.add("person-list")
    personSection.append(personList)

    renderPersonList(categoryId, 0)
}
