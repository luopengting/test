
def deal(val):
    val += 1


value = 1
deal(value)


v = dict()
print(v.items())
v.update({'1': 1})
v.update({'2': 2})
print(v.items())
for key, value in v.items():
    print(key, value)


print(type(None))

a = set()
a.add("float")
a.add("int")
print(a == set(["int", "float"]))


a = {
    '1': 1,
    '2': 2
}

b = {
    '3': 3,
    '4': 4
}

c = {}
c.update({'a': a})
c.update({'b': b})

c_new = c.items()
for i in c_new:
    print(type(i[1]))


str = "runoob"
print(len(str))

print(len("你真棒".encode("utf-8")))


a_list = ['a_', 'a', 'b', 'c', 'hello']
a_index = a_list.index('a')
print(a_index)

a = ['a', 'a', 'b', 'c']
b = ['c', 'a', 'b', 'c', 'a']

assert set(a) == set(b)
