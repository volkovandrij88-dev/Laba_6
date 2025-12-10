def repeat(n):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return inner
    return wrapper
