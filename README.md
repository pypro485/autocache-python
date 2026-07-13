# AutoCache

A lightweight and easy-to-use caching library for Python with support for automatic cache expiration.

## Features

- Simple `@cache()` decorator
-  Optional cache expiration (TTL)
- Cache hit/miss statistics
- Clear the cache at any time
- Lightweight with no external dependencies

## Installation

```bash
pip install autocache
```

## Quick Start

```python
from autocache import cache

@cache()
def slow_function(x):
    print("Running...")
    return x * 2

print(slow_function(5))
print(slow_function(5))
```

Output:

```
Running...
10
10
```

Notice that `"Running..."` is only printed once because the second call is returned from the cache.

## Cache Expiration

```python
from autocache import cache

@cache(expire=5)
def get_data():
    print("Fetching data...")
    return "Hello"

get_data()
```

After 5 seconds, the cached value expires and the function will run again.

## Cache Statistics

```python
from autocache import cache_info

cache_info()
```

Example output:

```
Autocache
----------------
Entries: 2
Hits: 5
Misses: 3
```

## Clearing the Cache

```python
from autocache import clear_cache

clear_cache()
```

## Roadmap

- [x] In-memory caching
- [x] Cache expiration
- [x] Cache statistics
- [x] Clear cache
- [ ] Support both `@cache` and `@cache(...)`
- [ ] Maximum cache size
- [ ] Disk caching
- [ ] Async support

## License

MIT License