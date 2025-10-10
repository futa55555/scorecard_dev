/**
 * File: frontend/js/renders/view/person/renderPersonList.js
 */

import { getPersonList } from "../../../clients/person/getPersonList.js"
import { createPersonCard } from "../../../components/view/person/createPersonCard.js"

export async function renderPersonList(categoryId, leagueId) {
    const personList = document.querySelector(".person-list")
    if (!personList) {
        console.error(`[renderPersonList] Error: <div class="person-list"> not found`)
    }


    personList.innerHTML = ""


    const personListData = await getPersonList(categoryId, leagueId)

    personListData.forEach(personData => {
        const person = createPersonCard(personData)
        personList.append(person)
    })
}
