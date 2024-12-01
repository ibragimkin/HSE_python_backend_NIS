from typing import List, Dict, Any
def extract_prices(products: List[Dict[str, Any]]) -> List[float]:
    """
    Возвращает список цен из списка продуктов.
    :param products: Список словарей, где каждый словарь представляет продукт с ключом 'price'.
    :return: Список цен продуктов.
    """
    return [product['price'] for product in products if 'price' in product]