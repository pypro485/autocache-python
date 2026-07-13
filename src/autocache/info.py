from . import state
def cache_info():
    info = {
        "entries": len(state._cache),
        "hits": state._hits,
        "misses": state._misses,
    }

    print("Autocache")
    print("----------------")
    print(f"Entries: {info['entries']}")
    print(f"Hits: {info['hits']}")
    print(f"Misses: {info['misses']}")

    return info