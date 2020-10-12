bound = [1, 7, 8, 10]
vals = 6.5
print(min(bound, key=lambda x: abs(x - vals)))


import numpy as np

a = np.array(
    [[1, 5, 6],
     [1, 4, 10],
     [2, -1, 8]]
)

bound = np.array([np.min(a, axis=0), np.max(a, axis=0)]).T
print(bound)

b = np.array(
    [1, 5, 6]
)

bound = np.array([np.min(b, axis=0), np.max(b, axis=0)]).T
print(bound)


a = np.array(
    [[1, 5, 6],
     [1, 4, 10],
     [2, -1, np.nan]]
)

print(np.isnan(a[:, -1]))
print(np.sum(np.isnan(a[:, -1])))
print(a[~np.isnan(a[:, -1])])


print(np.isnan(a))
print(a[~np.isnan(a)])
print(~np.isnan(a).any(axis=1))
print(a[~np.isnan(a).any(axis=1)])

print(np.nanmin(a, axis=0))


try:
    print('try……')
    r = 10 / 2
    print('结果：%s' % r)
except ZeroDivisionError as e:
    print('发生了异常：',e)
finally:
    print('最后执行……')

