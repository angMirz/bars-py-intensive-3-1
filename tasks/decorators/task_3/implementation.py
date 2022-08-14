def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.
    Returns:
        int - количество вызовов функции.
    """
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        return count
    return wrapper

    raise NotImplementedError