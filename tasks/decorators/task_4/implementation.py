from time import sleep
import random

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)
    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal times

            while times != 0:
                result = func(*args, **kwargs)
                if result:
                    return result
                times-=1
                sleep(delay)
            raise MyException
        return wrapper
    return decorator
    raise NotImplementedError

def random_choice():   
    return random.choice([True, False])

res = decorator_maker(3, 1)(random_choice)

print(res())