from autocache import cache, clear_cache

calls = 0

@cache()
def double(x):
    global calls
    calls += 1
    return x * 2


def test_clear_cache():
    global calls

    clear_cache()
    calls = 0

    double(5)
    clear_cache()
    double(5)

    assert calls == 2