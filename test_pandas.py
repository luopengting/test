import pandas as pd
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
# 输出排名序号
print(obj.rank())


import numpy as np


def get_rank(arr):
    indexes = arr.argsort()
    rank = np.zeros(shape=indexes.shape, dtype=int)
    latest = None
    tmp_rank = 0
    for index in indexes:
        value = arr[index]
        if latest != value:
            tmp_rank += 1
        latest = value
        rank[index] = tmp_rank

    return rank


arr = np.array([7, -5, 7, 4, 2, 0, 4])
print(get_rank(arr))

from pandas import DataFrame
import pandas as pd

cols = ['a', 'b', 'u/a', 'u/b']
df = DataFrame(np.arange(12).reshape((3, 4)), index=['one', 'two', 'thr'], columns=cols)

print(df[['a', 'u/b']])


import pandas as pd
inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}]
df = pd.DataFrame(inp)
print(df)

print(df["c1"].tolist())

