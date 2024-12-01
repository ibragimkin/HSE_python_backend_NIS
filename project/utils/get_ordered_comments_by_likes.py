from typing import List, Dict, Any
def get_ordered_comments_by_likes(comments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Возвращает список комментариев, отсортированных по убыванию числа лайков.
    :param comments: Список комментариев (словарей), где каждый комментарий имеет ключ 'like_count'.
    :return: Упорядоченный список комментариев.
    """
    return sorted(comments, key=lambda comment: comment.get('like_count', 0), reverse=True)
