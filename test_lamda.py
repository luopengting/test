a = [1, -1, 2, 1.0]

res = filter(lambda x: x < 0 or not isinstance(x, int), a)

print(res)

for i in res:
    print(i)


print(int == type(1.0))
