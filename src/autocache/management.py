from . import state

def clear_cache():
    """
    Clear all cached entries and reset hit/miss counters.
    """
    state._cache.clear()
    state._hits = 0
    state._misses = 0


def cache_remove(func, *args, **kwargs):
    """
    Remove a specific cache entry for a given function and its arguments.
    """
    key = (
        func.__name__,
        args,
        tuple(sorted(kwargs.items()))
        )

    if key in state._cache:
        del state._cache[key]

