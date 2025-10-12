/**
 * File: frontend/js/components/category/createCategoryBar.js
 */

export async function createCategoryBar(categoryList) {
    const params = new URLSearchParams(window.location.search)
    const categoryId = Number(params.get("category"))
    const currentPage = Number(params.get("page"))
    const currentPath = window.location.pathname

    // 「すべて」カテゴリを先頭に追加
    const allCategories = [{ category_id: 0, name: "すべて" }, ...categoryList]


    const categoryBar = document.createElement("div")

    allCategories.forEach(({ category_id, name }) => {
        const link = document.createElement("a")
        link.textContent = name

        // ===== クエリパラメータ構築 =====
        const newParams = new URLSearchParams()

        // category が 0 以外なら追加
        if (category_id !== 0) newParams.set("category", category_id)

        // page は常に維持（またはリセットしたい場合はここで1に）
        if (currentPage !== 0) newParams.set("page", 1)

        // クエリ文字列生成
        const queryString = newParams.toString() ? `?${newParams.toString()}` : ""

        // href設定
        link.href = `${currentPath}${queryString}`

        // 現在選択中のカテゴリを強調
        if (category_id === categoryId) link.classList.add("active")

        categoryBar.append(link)
    })

    return categoryBar
}
