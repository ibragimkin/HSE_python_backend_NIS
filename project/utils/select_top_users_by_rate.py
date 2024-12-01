from typing import List, Dict, Any
def select_top_users_by_rate(users: List[Dict[str, Any]], top_size: int) -> List[Dict[str, Any]]:
    """
    Выбирает топ пользователей с максимальным рейтингом.
    :param users: Список пользователей (словарей), где каждый пользователь имеет ключ 'rate'.
    :param top_size: Количество пользователей в топе.
    :return: Список топ-пользователей по рейтингу.
    """
    return sorted(users, key=lambda user: user.get('rate', 0), reverse=True)[:top_size]