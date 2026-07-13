from autocache import cache, clear_cache


calls = 0


@cache
def greet(name, age):
    global calls
    calls += 1
    return f"{name} is {age}"


def test_keyword_arguments():
    global calls

    clear_cache()
    calls = 0

    assert greet(name="Bob", age=10) == "Bob is 10"
    assert calls == 1

    # Same arguments, different order
    assert greet(age=10, name="Bob") == "Bob is 10"
    assert calls == 1