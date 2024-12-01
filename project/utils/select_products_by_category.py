from typing import List, Dict, Any
def select_products_by_category(products: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
    """
    Фильтрует продукты по заданной категории.
    :param products: Список продуктов (словарей), где каждый продукт имеет ключ 'category'.
    :param category: Название категории для фильтрации.
    :return: Список продуктов в заданной категории.
    """
    return [product for product in products if product.get('category') == category]
