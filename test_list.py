s = [1, 2, 3, 4, 5]

# del s[1:]
print(s)


def find_binary(target_value, object_list, start, end):
    # 找得到的话 index为其要替换的index
    # 找不到的话 index+1为其要插入的index
    print("====", start, end)
    mid = (start + end) // 2
    if object_list[mid] == target_value:
        return mid
    if start + 1 >= end:
        if target_value < object_list[end]:
            return start
        return end
    elif object_list[mid] < target_value:
        return find_binary(target_value, object_list, mid, end)
    else:
        return find_binary(target_value, object_list, start, mid - 1)


# print(find_binary(3, s, 0, len(s) - 1))
# print(find_binary(3, s, 1, 3))

nums = [1.5, 1, 3, 5]
for num in nums:
    print("********", s)
    index = find_binary(num, s, 0, len(s) - 1)
    if s[index] != num:
        print("index: ", index, "==", num)
        s.insert(index+1, num)
    else:
        del s[index:]

print(s)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
s = [1, 2, 3, 4, 5]
def binary_search(find, list1):
  low = 0
  high = len(list1)-1
  while low <= high:
    mid = (low + high) // 2
    print("========== mid ", mid)
    if list1[mid] == find:
      return mid
    #左半边
    elif list1[mid] > find:
      high = mid -1
    #右半边
    else:
      low = mid + 1
    print("=-=-=-=-= ", low, high)
  #未找到返回-1
  if find < list1[high]:
      return low
  return high

# nums = [1.5, 3, 5]
# for num in nums:
#     print("********", s)
#     index = binary_search(num, s)
#     if s[index] != num:
#         print("index: ", index, "==", num)
#         s.insert(index+1, num)
#     else:
#         del s[index:]
#
# print(s)
