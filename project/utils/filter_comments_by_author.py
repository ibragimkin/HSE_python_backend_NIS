from typing import List, Dict, Any
def filter_comments_by_author(comments: List[Dict[str, Any]], author: int) -> List[Dict[str, Any]]:
    """
    Отфильтровывает комментарии, оставленные автором с заданным ID.
    :param comments: Список комментариев (словарей), где каждый комментарий имеет ключ 'author_id'.
    :param author: ID автора, по которому выполняется фильтрация.
    :return: Список комментариев, принадлежащих заданному автору.
    """
    return [comment for comment in comments if comment.get('author_id') == author]
