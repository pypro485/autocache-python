import functools

_cache = {}

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):


        key = (
            func.__name__,
            args,
            tuple(kwargs.items())
        )

        if key in _cache:
            return _cache[key]

        result = func(*args, **kwargs)

        _cache[key] = result

        return result

    return wrapper
