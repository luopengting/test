a = {
    "network": "lenet",
    "loss": 1,
    "epoch": 10,
    "steps": 1000
}

b = {
    "steps": 1000,
    "network": "lenet",
    "loss": 1,
    "epoch": 10
}

assert a == b

for index, key in enumerate(b):
    print(index, key)


t = {"a": a, "b": b}
print(str(t))


class A:
    _value = 1


t = {"a": a, "b": b, "A": A()}
print(str(t))

import json
try:
    json.dumps(t)
except TypeError as exo:
    print(str(exo))
