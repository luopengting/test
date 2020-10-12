import numpy as np
choice = [10, 20, 30]
value = 14
v = min(choice, key=lambda x: abs(x - value))
print(v)

nearest_index = int(np.argmin(np.fabs(np.array(choice) - value)))
print(choice[nearest_index])


a = [[1, 2, 3],
     [4, 5, 6]]

b = [[1, 2, 3],
     [4, 5, 6]]

c = [[4, 5, 6],
     [1, 2, 3]]

a, b, c = np.array(a), np.array(b), np.array(c)

print((a == b).all())

print((a == c).all())


import pandas as pd

df1 = pd.DataFrame(a)
df2 = pd.DataFrame(b)
df3 = pd.DataFrame(c)
print(df1 == df2)
print(df1 == df3)
