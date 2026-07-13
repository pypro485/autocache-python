from . import state
from .utils import make_key


def clear_cache():
    """
    Remove all cached values and reset statistics.
    """

    state._cache.clear()
    state._hits = 0
    state._misses = 0


def cache_remove(func, *args, **kwargs):
    """
    Remove one specific cached function result.
    """

    key = make_key(func, args, kwargs)

    if key in state._cache:
        del state._cache[key]