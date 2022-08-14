def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    result = []
    for element in range(1000, 2000):
        if element % 7 == 0 and element % 5 != 0:
            result.append(element)
    return result
    raise NotImplementedError

print(get_numbers())
