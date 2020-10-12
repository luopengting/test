# 二分查找
def binary_search(a, key):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low+high) // 2
        if key < a[mid]:
            high = mid - 1
        elif key > a[mid]:
            low = mid + 1
        else:
            return mid

    return high + 1


my_list = [1, 3, 4, 6, 7, 8, 9]
print(binary_search(my_list, 9)) # 6
#
my_list = [1, 3, 4, 6, 7, 8, 9, 10]
print(binary_search(my_list, 9)) # 6

my_list = [1, 3, 4, 6, 7, 8, 9, 10]
print(binary_search(my_list, 8.5)) # 6

my_list = [1, 3, 4, 6, 7, 8, 9, 10]
print(binary_search(my_list, 0)) # 0

my_list = [1, 3, 4, 6, 7, 8, 9, 10]
print(binary_search(my_list, 1.5)) # 1

my_list = [1, 3, 4, 6, 7, 8, 9, 10]
print(binary_search(my_list, 11)) # 8

my_list = []
print(binary_search(my_list, 11)) # 0
my_list.insert(0, 11)
print(my_list)