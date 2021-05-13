class A:
    def __init__(self):
        self.i = 1

class B(A):
    pass

class C(A):
    pass


a, b, c = A(), B(), C()
b.i = 2
print(a.i, b.i, c.i)

a.i = 3
print(a.i, b.i, c.i)
