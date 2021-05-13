class A:
    def __del__(self):
        print("over")

    def hello(self):
        print('hello')


a = A()
b = a

a.hello()
del a
b.hello()
print("aaaaa")
del b
