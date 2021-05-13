from flask import jsonify
import numpy as np

a = np.arange(15).reshape([3, 5])

print(a)

# a[2][3] = np.nan
# print(a)

b = np.full((2, 2), np.nan)
print(b)

b[1][0] = 1
print(b)

b[0][1] = 2
print(b)

# j = jsonify({"b": b})
# print(j)

import json
data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
print(data2)

from json import JSONDecodeError
try:
    raise JSONDecodeError("error message", "s", 0)
except ValueError:
    print("Catch ValueError OK!")


try:
    with open('test_list.py', 'r') as f:
        json.load(f)
except ValueError:
    print("Json load failed.")
