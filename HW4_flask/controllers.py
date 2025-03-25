def operation(a: int, b: int) -> int:
    """
    Функция складывает два числа.
    Если одно из чисел не передано (None), возвращается None.
    """
    if a is None or b is None:
        return None  # возвращаем None, если параметры не заданы
    return a + b
