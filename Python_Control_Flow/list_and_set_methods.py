list = ["rat", "cat", "dog", "pig", "owl"]
print(list)

print(list.append('hen'))

print(list.remove('rat'))

pooped_list = list.pop(0)
print(pooped_list)

print(list.sort())

print(list.reverse())

print(list.extend(('cow','ant')))

my_set = {10, 3.5, 1000.6, "5"}
print("my_set")

print(my_set.add(55))

print(my_set.remove(1000.6))

my_other_set = {5, 7, 2}
print("my_other_set")
print(my_set.union("my_other_set"))

print(my_set.intersection("my_other_set"))

print(my_set.difference("my_other_set"))