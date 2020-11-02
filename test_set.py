
added_info = {
    "tag": 1,
    "remark": "lalala"
}

print(added_info.keys())

added_info_keys = ["tag", "remark"]
keys = set(added_info.keys())
if not keys.issubset(added_info_keys):
    raise Exception


list1 = ["network", "loss", "epoch"]
set1 = set(list1)
list2 = ["network", "version", "version-info"]
set2 = set(list2)

in_set = set2 & set1
print(set1, set2, in_set)

print(list(in_set))

print(set1-set2)



# ===
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")
print(fruits)

list1 = ["method"]
set1 = set(list1)
list2 = ["method"]
set2 = set(list2)

if set1.issubset(list2):
    print("yes")


