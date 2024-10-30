#tuple are immutable, meaning it can't be changed or modified.
#Turple are similar to list but instead of square brackets they use parenthesis.

my_tuple_gadgets = ["Kettle", 4.5, "True", "blender", 50]
print(my_tuple_gadgets)
print (my_tuple_gadgets[0])
print (my_tuple_gadgets[-1])

print (my_tuple_gadgets.count("blender"))

print(my_tuple_gadgets.index('True'))

#conversion
num = 6
dec = 1.2
whole = "100"

num1= float(num)
print(num1)

dec1 = int(dec)
print(dec1)

whole1 = int(whole)
print(whole1)

Ghana = ["gold","bauxite","timber","oil","silver"]
print(Ghana)
print(" , ".join(Ghana))