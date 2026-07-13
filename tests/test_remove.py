from autocache import cache
from autocache import cache_remove, clear_cache


calls = 0


@cache
def multiply(x):
    global calls
    calls += 1
    return x * 2


def test_cache_remove():
    global calls

    clear_cache()
    calls = 0

    # First call should run the function
    assert multiply(5) == 10
    assert calls == 1

    # Second call should use the cache
    assert multiply(5) == 10
    assert calls == 1

    # Remove only this cached value
    cache_remove(multiply, 5)

    # Should run again because it was removed
    assert multiply(5) == 10
    assert calls == 2