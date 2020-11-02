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

print("================dropna=====================")
data = pd.DataFrame({
    'a': [1, 3, 5, np.nan, 7, 9],
    'b': ['a', 'b', np.nan, np.nan, 'd', 'e'],
    'c': [1, 3, 5, 7, 9, 11],
    'd': [np.nan, 2, 4, np.nan, np.nan, 6],
    'e': [np.nan, 7, np.nan, np.nan, np.nan, np.nan]
})

data = data.dropna(axis=0, how='any')
print(data)

print(data['bb'])
