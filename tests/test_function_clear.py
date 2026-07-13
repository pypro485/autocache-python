from autocache import cache, clear_cache


calls = 0


@cache
def multiply(x):
    global calls
    calls += 1
    return x * 2


def test_function_cache_clear():
    global calls

    clear_cache()
    calls = 0

    # First call runs the function
    assert multiply(5) == 10
    assert calls == 1

    # Second call uses the cache
    assert multiply(5) == 10
    assert calls == 1

    # Clear only multiply's cache
    multiply.cache_clear()

    # Should run again
    assert multiply(5) == 10
    assert calls == 2