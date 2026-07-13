from . import state


def cache_info():
    """
    Display cache entires, hits, and misses.
    """
    print("Autocache")
    print("----------------")
    print(f"Entries: {len(state._cache)}")
    print(f"Hits: {state._hits}")
    print(f"Misses: {state._misses}")