from datetime import datetime

def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper (*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

    raise NotImplementedError
