# List Index Access
items = ["apple", "banana", "cherry"]
index = int(input("Enter the index of the item you want to access: "))
print("You selected:", items[index])


# Invalid input - Occurs if the user inputs value that is not an integer.
# Index out of bounds - This is when user inputs an index that does not exist in the list.
# One can use try and except blocks to handle these potential errors.

items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter the index of the item you want to access: "))
    print("You selected:", items[index])
except ValueError:
    print("Invalid input! Please enter a numeric value.")
except IndexError:
    print("Index out of bounds! Please enter a valid index.")
