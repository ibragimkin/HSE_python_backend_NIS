import uuid


class User:
    def __init__(self, name: str):
        """
        Инициализирует объект пользователя.
        :param name: Имя пользователя.
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.comments_count: int = 0
        self.rate: int = 0
        self.is_banned: bool = False

    def edit_name(self, new_name: str) -> None:
        """
        Изменяет имя пользователя.
        :param new_name: Новое имя пользователя.
        """
        self.name = new_name

    def increment_rate(self) -> None:
        """
        Увеличивает рейтинг пользователя на 1.
        """
        self.rate += 1

    def ban_user(self) -> None:
        """
        Блокирует пользователя.
        """
        self.is_banned = True

    def unban_user(self) -> None:
        """
        Разблокирует пользователя.
        """
        self.is_banned = False

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта User.
        """
        ban_status = "banned" if self.is_banned else "active"
        return (
            f"User(id={self.id}, name='{self.name}', comments_count={self.comments_count}, "
            f"rate={self.rate}, status={ban_status})"
        )
