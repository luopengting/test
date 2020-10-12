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

j = jsonify({"b": b})
print(j)
