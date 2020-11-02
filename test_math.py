import math


def _in_range(num, low, high):
    # num in [low, high)
    return low <= num < high


def include_integer(low, high):
    if _in_range(math.ceil(low), low, high) or _in_range(math.floor(high), low, high):
        return True
    return False

low = 1
high = 1.1
print(include_integer(low, high))

low = 1.1
high = 1.2
print(include_integer(low, high))


print(include_integer(0.9, 0.8))

print(include_integer(0.01, 0.1))

print(include_integer(-0.01, 1))


