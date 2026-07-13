from autocache import cache, clear_cache


calls = 0


@cache
def no_args_cache(x):
    global calls
    calls += 1
    return x * 2


@cache(expire=10)
def args_cache(x):
    global calls
    calls += 1
    return x * 2


def test_cache_without_parentheses():
    clear_cache()

    assert no_args_cache(5) == 10
    assert no_args_cache(5) == 10

    assert calls == 1


def test_cache_with_expire_argument():
    clear_cache()

    assert args_cache(5) == 10
    assert args_cache(5) == 10

    assert calls == 2