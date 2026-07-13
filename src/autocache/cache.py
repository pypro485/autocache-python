import functools
import time
from . import state


def cache(expire=None):
    """
    Cache function results in memory with an optional expiration time.

    Args:
    expire (float, optional): The time in seconds after which the cache entry will expire. 
                                  If None, the cache entry will not expire.
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            key = (
                func.__name__,
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

            result = func(*args, **kwargs)

            state._cache[key] = (
                result,
                time.time()
            )

            return result

        return wrapper

    return decorator