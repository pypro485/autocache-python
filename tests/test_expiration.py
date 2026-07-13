import time

from autocache import cache, clear_cache

calls = 0

@cache(expire=1)
def double(x):
    global calls
    calls += 1
    return x * 2


def test_cache_expires():
    global calls

    clear_cache()
    calls = 0

    double(5)

    time.sleep(1.2)

    double(5)

    assert calls == 2