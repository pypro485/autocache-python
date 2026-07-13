from . import state

def clear_cache():
    state._cache.clear()
    state._hits = 0
    state._misses = 0

