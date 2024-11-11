#Division Calculator
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
result = numerator / denominator
print("The result is:", result)



#Possible errors are 
#Invalid - This is when user enters an incorrect datatype (non-integer value) for instance entering a string instead of an integer

#Zero Division - This occurs when user divide numerator number by zero.

#One can use Try , Except, and Finally

try:
    numerator = int(input("Input the numerator: "))
    denominator = int(input("Input the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Invalid input! Please enter numeric values only.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print("The result is:", result)
finally:
    print("Thank you but be careful with your calculation.")
