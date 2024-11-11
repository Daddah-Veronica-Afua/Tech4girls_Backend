#Integer Conversion
user_input = input("Enter a number: ")
converted_number = int(user_input)
print("The number you entered is:", converted_number)


# Potential error that can arise is when user enters a value that cannot be converted to an integer, such as a string or a floating-point number.
#One can handle such error using try and except block

try:
    user_input = input("Enter a number: ")
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
