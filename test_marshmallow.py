
a = ["1", "2"]

# if "3" not in a:
#     raise ValueError("It should be in %s" % a)


b = {
    "1": 1,
    "2": 2,
    "3": 3
}

c = {
    "3": 4,
    "5": 6
}

b.pop("1")
print(b)

d = b
d.update(c)
print(d)
print(b)

my_set = set()
my_set.add("1")
my_set.add("10")
my_set.add("5")
my_set.add("1")
my_set.add("2")
print(my_set)

lineage_type = {
    "in": ["model", "dataset"]
}

print(list(lineage_type.values()))

lineage_type = {
    "eq": "model"
}

print(list(lineage_type.values()))


print(set().issubset(["in", "eq"]))
