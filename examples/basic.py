import time
from autocache import cache


@cache(expire=5)
def slow(x):
    print("Running function...")
    time.sleep(2)
    return x * 2


print(slow(5))
print(slow(5))

time.sleep(6)

print(slow(5))