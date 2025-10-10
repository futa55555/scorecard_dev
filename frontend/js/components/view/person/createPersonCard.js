/**
 * File: frontend/js/components/view/person/createPersonCard.js
 */

export function createPersonCard(personData) {
    const currentPath = window.location.pathname
    const baseUrl = currentPath.split("/person")[0]


    const personCard = document.createElement("div")
    personCard.classList.add("person-card")


    const personName = document.createElement("div")
    personName.classList.add("person-name")

    const personNameLink = document.createElement("a")
    personNameLink.classList.add("person-name-link")

    personNameLink.textContent = personData.last_name + personData.first_name
    personNameLink.href = `${baseUrl}/person_detail.html?person=${personData.person_id}`
    personName.append(personNameLink)
    personCard.append(personName)


    return personCard
}
