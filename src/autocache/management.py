from . import state

def clear_cache():
    """
    Clear all cached entries and reset hit/miss counters.
    """
    state._cache.clear()
    state._hits = 0
    state._misses = 0

