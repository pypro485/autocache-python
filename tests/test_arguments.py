from autocache import cache, clear_cache


calls = 0


@cache
def square(x):
    global calls
    calls += 1
    return x * x


def test_different_arguments():
    global calls

    clear_cache()
    calls = 0

    assert square(2) == 4
    assert square(3) == 9

    assert calls == 2