from autocache import cache, clear_cache, cache_info

def test_cache_info_returns_data():
    clear_cache()

    @cache
    def test_func(x):
        return x * 2

    test_func(5)
    test_func(5)

    info = cache_info()

    assert info["entries"] == 1
    assert info["hits"] == 1
    assert info["misses"] == 1