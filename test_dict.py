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
