import functools
from . import state


def cache(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        key = (
            func.__name__,
            args,
            tuple(sorted(kwargs.items()))
        )

        if key in state._cache:
            state._hits += 1
            return state._cache[key]

        state._misses += 1

        result = func(*args, **kwargs)

        state._cache[key] = result

        return result

    return wrapper