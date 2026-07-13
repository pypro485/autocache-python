from autocache import cache
import time


@cache
def slow_function(x):
    print("Running function...")
    time.sleep(2)
    return x * 2


print(slow_function(5))
print(slow_function(5))
print(slow_function(10))