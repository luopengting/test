class A:
    def __init__(self):
        self.__i = 1
        self.j = 2

    def print(self):
        print("A.print()")
        print(self.__i, self.j)

class B(A):
    def __init__(self):
        self.__i = 3
        self.j = 7
    def print(self):
        print("B.print()")
        print(self.__i, self.j)


b = B()
b.print()