import functools
import time
from . import state
from .utils import make_key


def cache(func=None, *, expire=None):
    """
    Cache function results in memory with an optional expiration time.

    Args:
        expire (float, optional): Time in seconds after which the cache entry
        expires. If None, entries never expire.
    """

    def decorator(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):

            key = make_key(f, args, kwargs)

            if key in state._cache:
                cached_value, created_time = state._cache[key]

                if expire is None or (time.time() - created_time) < expire:
                    state._hits += 1
                    return cached_value

                # Cache expired
                del state._cache[key]

            state._misses += 1

            result = f(*args, **kwargs)

            state._cache[key] = (
                result,
                time.time()
            )

            return result

        return wrapper

    # Allows:
    # @cache
    if func is not None and callable(func):
        return decorator(func)

    # Allows:
    # @cache()
    # @cache(expire=60)
    return decorator