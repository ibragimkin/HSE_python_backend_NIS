from typing import List, Dict, Any
def get_ordered_products_by_price(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Возвращает список продуктов, отсортированных по убыванию цены.
    :param products: Список словарей, где каждый словарь представляет продукт с ключом 'price'.
    :return: Упорядоченный список продуктов.
    """
    return sorted(products, key=lambda product: product.get('price', 0), reverse=True)
