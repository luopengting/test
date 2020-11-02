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


class dynamic(dict):
    def __init__(self, d=None):
        super().__init__()
        if d is not None:
            for k,v in d.items():
                self[k] = v

    def __key(self, key):
        return "" if key is None else key

    def __setattr__(self, key, value):
        self[self.__key(key)] = value

    def __getattr__(self, key):
        print("get attr")
        return self.get(self.__key(key))

    def __getitem__(self, key):
        return super().get(self.__key(key))

    def __setitem__(self, key, value):
        return super().__setitem__(self.__key(key), value)


a = {
    'k': 1
}

b = dynamic(a)
print(b.k)
