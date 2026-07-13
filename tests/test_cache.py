from autocache import cache


@cache()
def double(x):
    return x * 2


def test_returns_correct_value():
    assert double(5) == 10