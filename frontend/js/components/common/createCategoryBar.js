/**
 * File: frontend/js/components/common/createCategoryBar.js
 */

import { getCategoryList } from "../../clients/category/getCategoryList.js"

export async function createCategoryBar(currentCategoryId) {
    const categoryBar = document.createElement("div")


    let categoryList = await getCategoryList()
    categoryList = [
        { category_id: 0, name: "すべて" },
        ...categoryList
    ]


    const currentPath = window.location.pathname

    categoryList.forEach(category => {
        const link = document.createElement("a")
        link.textContent = category.name

        if (category.category_id !== 0) {
            link.href = `${currentPath}?category=${category.category_id}`
        } else {
            link.href = `${currentPath}`
        }

        if (category.category_id === currentCategoryId) {
            link.classList.add("active")
        }

        categoryBar.append(link)
    })


    return categoryBar
}
