from autocache import cache, clear_cache
from autocache.management import cache_remove


calls = 0


@cache
def double(x):
    global calls
    calls += 1
    return x * 2


def test_cache_remove_only_removes_one():
    global calls

    clear_cache()
    calls = 0

    double(5)
    double(10)

    assert calls == 2

    cache_remove(double, 5)

    double(5)
    assert calls == 3

    double(10)
    assert calls == 3