from tasks.common import MyException

def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    cache = {}

    def wrapper(value):

        if isinstance(value, int) and value >=0:
            if value in cache:
                return cache[value]

            result = func(value)
            cache[value] = result
            return result
        else:
            raise MyException

    return wrapper

    raise NotImplementedError