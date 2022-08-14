def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает копию словаря.
    """
    copy = {}

    for key in origin_dict.keys():
        copy[key] = origin_dict[key]

    return copy

test = {'a':'b'}
test_copy = copy_dict(test)

print(test, test_copy)

test_copy['a'] = 'c'

print(test, test_copy)
