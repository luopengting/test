x = 5


def func1():
    x = 6
    def func2():
        x *= x
        return x
    return func2()


def func3():
    x = [6]
    def func2():
        x[0] *= x[0]
        return x[0]
    return func2()


if __name__ == "__main__":
    print(func1())  # 堆变量未释放
    print(func3())
