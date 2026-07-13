import functools
import time
from . import state


def cache(func=None, *, expire=None):
    """
    Cache function results in memory with optional expiration.

    Args:
        func: The function being decorated.
        expire (float, optional): Seconds before cached values expire.
            If None, values never expire.
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            key = (
                f.__name__,
                args,
                tuple(sorted(kwargs.items()))
            )

            if key in state._cache:
                cached_value, created_time = state._cache[key]

                if expire is None or (time.time() - created_time) < expire:
                    state._hits += 1
                    return cached_value

                # Cache expired
                del state._cache[key]

            state._misses += 1
            result = f(*args, **kwargs)
            state._cache[key] = (result, time.time())
            return result

        return wrapper

    # Case 1: Used without parentheses -> @cache
    if func is not None and callable(func):
        return decorator(func)

    # Case 2: Used with parentheses -> @cache() or @cache(expire=60)
    return decorator
