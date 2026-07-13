from autocache import cache, cache_info
import time


@cache
def slow(x):
    print("Running function...")
    time.sleep(2)
    return x * 2


print(slow(5))
print(slow(5))
print(slow(10))

cache_info()