/**
 * File: frontend/js/renders/view/person/renderPersonList.js
 */

import { getPersonList } from "../../../clients/person/getPersonList.js"
import { createPageBar } from "../../../components/view/common/createPageBar.js"
import { createPersonCard } from "../../../components/view/person/createPersonCard.js"
import { bindPagination } from "../../../events/view/common/bindPagination.js"

export async function renderPersonList() {
    const personList = document.querySelector(".person-list")
    if (!personList) {
        console.error(`[renderPersonList] Error: <div class="person-list"> not found`)
    }


    personList.innerHTML = ""


    const params = new URLSearchParams(window.location.search)
    const currentPage = Number(params.get("page"))
    const categoryId = Number(params.get("category"))
    const leagueId = Number(params.get("league"))

    const limit = 30


    const personListData = await getPersonList(currentPage, limit, categoryId, leagueId)

    personListData.people.forEach(personData => {
        const person = createPersonCard(personData)
        personList.append(person)
    })

    const personListPageBar = createPageBar("person", currentPage, personListData.total_page)
    personList.append(personListPageBar)

    bindPagination(personListPageBar)
}
