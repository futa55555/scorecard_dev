/**
 * File: frontend/js/components/common/createCategoryBar.js
 */

export async function createCategoryBar(categoryList) {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))

    categoryList = [
        { category_id: 0, name: "すべて" },
        ...categoryList
    ]

    const currentPath = window.location.pathname


    const categoryBar = document.createElement("div")


    categoryList.forEach(category => {
        const link = document.createElement("a")
        link.textContent = category.name

        if (category.category_id !== 0) {
            link.href = `${currentPath}?category=${category.category_id}`
        } else {
            link.href = `${currentPath}`
        }

        if (category.category_id === categoryId) {
            link.classList.add("active")
        }

        categoryBar.append(link)
    })


    return categoryBar
}
