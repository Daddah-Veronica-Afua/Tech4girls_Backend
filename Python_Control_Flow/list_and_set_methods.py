list = ["rat", "cat", "dog", "pig", "owl"]
print(list)

list.append("hen")
print(list)

list.remove("rat")
print(list)

pooped_list = list.pop(0)
print(pooped_list)

list.sort()
print(list)

list.reverse()
print(list)

list.extend(('cow','ant'))
print(list)

my_set = {10, 3.5, 1000.6, "5"}
print(my_set)

my_set.add(55)
print(my_set)

my_set.remove(1000.6)
print(my_set)

my_other_set = {5, 7, 2}
print(my_other_set)
print(my_set.union(my_other_set))

my_set.intersection(my_other_set)
print(my_set)

my_set.difference(my_other_set)
print(my_set)