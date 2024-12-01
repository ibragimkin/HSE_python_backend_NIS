class Product:
    def __init__(self, name: str, category: str, price: float):
        """
        Инициализирует объект продукта.
        :param name: Название продукта.
        :param category: Категория продукта.
        :param price: Цена продукта.
        """
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.sale: float = 0.0  # Скидка в процентах (0-100)

    def edit_category(self, new_category: str) -> None:
        """
        Изменяет категорию продукта.
        :param new_category: Новая категория продукта.
        """
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        """
        Изменяет цену продукта.
        :param new_price: Новая цена продукта.
        """
        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Цена не может быть отрицательной.")

    def set_sale(self, sale: float) -> None:
        """
        Устанавливает скидку на продукт.
        :param sale: Скидка в процентах (0-100).
        """
        if 0 <= sale <= 100:
            self.sale = sale
        else:
            raise ValueError("Скидка должна быть в пределах от 0 до 100.")

    def cancel_sale(self) -> None:
        """
        Отменяет скидку на продукт.
        """
        self.sale = 0.0

    def get_price(self) -> float:
        """
        Возвращает цену продукта с учетом скидки.
        :return: Цена продукта после применения скидки.
        """
        discounted_price = self.price * (1 - self.sale / 100)
        return round(discounted_price, 2)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Product.
        """
        sale_info = f", sale={self.sale}%" if self.sale > 0 else ""
        return f"Product(name='{self.name}', category='{self.category}', price={self.price}{sale_info})"
