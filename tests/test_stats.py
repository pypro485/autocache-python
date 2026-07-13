from autocache import cache, clear_cache

calls = 0

@cache()
def double(x):
    global calls
    calls += 1
    return x * 2


def test_different_arguments_create_new_cache_entries():
    global calls

    clear_cache()
    calls = 0

    double(5)
    double(10)

    assert calls == 2